# Copyright (c) Facebook, Inc. and its affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from abc import ABC, abstractmethod

import omegaconf
import hydra

from polymetis.robot_client.metadata import RobotClientMetadata


class AbstractRobotClient(ABC):
    """Parent class for all RobotClients.

    An interface for RobotClients which connect to the gRPC server.
    All RobotClients use the RobotClientMetadata object, which is
    instantiated from a Hydra config. Example robot client configs
    are in `../conf/robot_client/`.
    """

    def __init__(self, metadata_cfg: omegaconf.DictConfig):
        # If metadata_cfg doesn't have _target_, add it
        if "_target_" not in metadata_cfg:
            metadata_cfg = omegaconf.OmegaConf.merge(
                {"_target_": "polymetis.robot_client.metadata.RobotClientMetadata"},
                metadata_cfg,
            )

        self.metadata: RobotClientMetadata = hydra.utils.instantiate(metadata_cfg)
        assert isinstance(self.metadata, RobotClientMetadata)

    @abstractmethod
    def run(self):
        """Override this method to connect to the server."""
        pass
