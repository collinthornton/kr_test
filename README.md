# kr_test

This repository contains a ROS package to test the ROS2 CBun on the Kassow KR1410 Gen 2 robotic manipulator

## Create the Docker image
### Config
Open [docker-compose.yml](./docker/docker-compose.yml) and configure the following environment variables as needed:

| Name            | Default   | Description                           |
|-----------------|-----------|---------------------------------------|
| `ROS_DOMAIN_ID` | 10        | ROS2 domain ID matching CBun settings | 

### Build
Build the Docker image using `docker-compose`:

```commandLine
cd docker
docker compose build
```

## Run the docker image
Run the Docker image using `docker-compose`:

```commandLine
cd docker
CURRENT_UID=$(id -u):$(id -g) docker compose run kr_test NODE_NAME
```

where `NODE_NAME` may be chosen from the following options:

| Name               | Description                                             |
|--------------------|---------------------------------------------------------|
| `velocity_node.py` | Publish sinusoidal command to `/kr/motion/jog_joint`    |
| `position_node.py` | Publish sinusoidal command to `/kr/motion/follow_joint` |

> Note: by default the docker image runs as a non-root user, so the environment variable `CURRENT_UID` must be supplied as shown above
