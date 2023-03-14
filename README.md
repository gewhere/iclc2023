# ICLC 2023 -- Algorave 10 information retrieval

- Two options:
  - a) Run the prebuilt (recommended)
  - b) Built docker image

NOTE: A separate repo hosts the video files, and depends on git for large files (`git-lfs`): [https://github.com/gewhere/algorave10-large-files](https://github.com/gewhere/algorave10-large-files). No need to install `git-lfs` to run the docker images shown below.

## a) Run the prebuilt from docker-hub (recommended)

The image is available on docker hub: [https://hub.docker.com/r/algorave10/iclc2023](https://hub.docker.com/r/algorave10/iclc2023)

Open a terminal and execute: `docker run --rm -p 8888:8888 algorave10/iclc2023:latest`

### Access the Jupyter Lab notebook

After the image is pulled from docker hub, the terminal output should look like this:

```asciidoc
To access the server, open this file in a browser:
    file:///home/jovyan/.local/share/jupyter/runtime/jpserver-7-open.html
Or copy and paste one of these URLs:
    http://a15f61b09a60:8888/lab?token=381b1ff05fbdd31e760049685ae5317307542
 or http://127.0.0.1:8888/lab?token=381b1ff05fbdd31e760049685ae5317307542b3d
```

To **run the notebook** copy and paste in your browser the last URL (which starts with `http://127.0.0.1:8888`).

_NOTE_: If you cannot access the notebook, make sure the port `8888` is in _not_ used by another python notebook, or another application.

## b) Built the docker image

- Clone this repository: `git clone https://github.com/gewhere/iclc2023.git`
- Go to: `cd iclc2023/docker`
- Step 1: `./build.sh 2>log.txt`
- Step 2: `./run.sh`
