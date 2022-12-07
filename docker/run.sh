#!/bin/sh
docker run --rm \
    --name="iclc2023" \
    --user $(id -u) --group-add users \
    -p 8888:8888 \
    -v "${PWD}/img":/home/jovyan/work/img \
    -v "${PWD}/notebooks":/home/jovyan/work/notebooks \
    "iclc2023:latest"
