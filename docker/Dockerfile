ARG ROS_DISTRO

# This argument allows us to switch between Ubuntu versions as the basis
FROM osrf/ros:${ROS_DISTRO}-desktop as ros

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive

LABEL maintainer="collin.thornton@swri.org"
LABEL date="February 2024"

USER root

# Bind mount the source directory so as not to unnecessarily copy source code into the docker image
ARG WORKSPACE_DIR=/opt/kr_test

# Get dependencies
RUN --mount=type=bind,target=${WORKSPACE_DIR}/src/kr_test \
    vcs import ${WORKSPACE_DIR}/src < ${WORKSPACE_DIR}/src/kr_test/dependencies.repos --shallow --recursive \
    && sudo apt upgrade \
    && sudo apt update \
    && source /opt/ros/${ROS_DISTRO}/setup.bash \
    && rosdep update --rosdistro=${ROS_DISTRO} \
    && rosdep install --from-paths ${WORKSPACE_DIR}/src -iry \
    && cd ${WORKSPACE_DIR} \
    && colcon build \
    && rm -rf build log

COPY ["docker/entrypoint.bash", "/entrypoint.bash"]
CMD ["/bin/bash"]