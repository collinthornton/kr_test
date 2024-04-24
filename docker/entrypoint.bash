#! /usr/bin/env bash

if [ $# != 1 ]; then
  printf "Usage: entrypoint.bash LAUNCH_FILE_NAME"
  exit 1
fi

source /opt/kr_test/install/setup.bash
ros2 run kr_test $1

