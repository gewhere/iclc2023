# syntax=docker/dockerfile:experimental
FROM python:3.9-slim as extract-performances
COPY algorave10-performance-list.org /data/algorave10-performance-list.org
COPY src/read-performance-list.py read-performance-list.py
RUN python read-performance-list.py
RUN cat /data/url-performances-algorave-10.txt



# INSTALL PYTHON
FROM python:3.9-slim as download-mp-4
# to redo from start without invalidating the cache mount, change the next ARG manually
ARG aptcache=1
RUN --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt \
    apt-get update && \
    env DEBIAN_FRONTEND=noninteractive apt-get install -yqq --no-install-recommends \
    ca-certificates \
    wget \
    git \
    git-lfs \
    && rm -rf /var/lib/apt/lists/*
COPY --from=extract-performances /data/performances.pkl /data/performances.pkl
COPY --from=extract-performances /data/url-performances-algorave-10.txt /data/url-performances-algorave-10.txt
# COPY _prebuild/test-data/url-performances-algorave-10.txt /data/url-performances-algorave-10.txt
RUN git-lfs --version
RUN git clone https://github.com/gewhere/algorave10-large-files.git
RUN ls -lh /algorave10-large-files



FROM download-mp-4 as convert-to-mp-3
RUN pip install moviepy
# COPY src/convert-mp4-to-mp3.py /src/convert-mp-4-to-mp-3.py
# RUN python /src/convert-mp-4-to-mp-3.py
# RUN ls -lh *.mp3



FROM convert-to-mp-3 as feature-extraction
RUN pip install librosa
RUN --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt \
    apt-get update && \
    env DEBIAN_FRONTEND=noninteractive apt-get install -yqq --no-install-recommends \
    libsndfile1 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*
COPY --from=download-mp-4 algorave10-large-files /data/algorave10-large-files
COPY src/feature-extraction.py /src/feature-extraction.py
COPY src/remove-outliers.py /src/remove-outliers.py
RUN python /src/feature-extraction.py
RUN python /src/remove-outliers.py
RUN ls -lh /data


# JUPYTER
FROM jupyter/base-notebook:latest as notebook-server-base
RUN mamba install --yes \
    matplotlib numpy scipy \
    && mamba clean --all -f -y \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "/home/${NB_USER}"


# RUN JUPYTER NOTEBOOK
FROM notebook-server-base
COPY --from=feature-extraction --chown="${NB_UID}":"${NB_GID}" /data/*.pkl /home/jovyan/work/data/
# COPY --from=feature-extraction --chown="${NB_UID}":"${NB_GID}" /data /home/jovyan/work/data/
COPY --chown="${NB_UID}":"${NB_GID}" /notebooks/* /home/jovyan/work/notebooks/
RUN mkdir /home/jovyan/work/img/
