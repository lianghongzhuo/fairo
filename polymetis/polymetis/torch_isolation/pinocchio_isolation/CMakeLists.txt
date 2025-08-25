# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
cmake_minimum_required(VERSION 3.14)
project(pinocchio_isolation)

# Find spdlog (C++ logger)
if(NOT TARGET spdlog)
    find_package(spdlog REQUIRED)
endif()

# Find Eigen
find_package(Eigen3 REQUIRED)

# Find Pinocchio
set(pinocchio_DIR $ENV{CONDA_PREFIX}/lib/cmake/pinocchio)
find_package(pinocchio REQUIRED)

include_directories(
    "include"
    ${EIGEN3_INCLUDE_DIR}
    ${pinocchio_INCLUDE_DIRS} 
)

add_library(pinocchio_wrapper SHARED src/pinocchio_wrapper.cpp)
set_target_properties(pinocchio_wrapper PROPERTIES CXX_VISIBILITY_PRESET hidden)
target_link_libraries(pinocchio_wrapper
    ${pinocchio_LIBRARIES}
    pinocchio::pinocchio_parsers
    spdlog::spdlog
)
