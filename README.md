# ICLC 2023 -- Algorave 10 information retrieval
- Two options:
  * a) Run the prebuilt (recommended)
  * b) Built docker image

NOTE: A separate repo hosts the video files, and depends on git for large files (`git-lfs`): [https://github.com/gewhere/algorave10-large-files](https://github.com/gewhere/algorave10-large-files). No need to install `git-lfs` to run the docker images shown below.

## a) Run the prebuilt from docker-hub (recommended)
The image is available on docker hub: [https://hub.docker.com/r/anononymoususer/iclc2023](https://hub.docker.com/r/anononymoususer/iclc2023)

Open a terminal and execute: `docker run --rm -p 8888:8888 anononymoususer/iclc2023:latest`

## b) Built the docker image

- Clone this repository: `git clone https://github.com/gewhere/iclc2023.git`
- Go to: `cd iclc2023/docker`
- Step 1: `./build.sh 2>log.txt`
- Step 2: `./run.sh`
