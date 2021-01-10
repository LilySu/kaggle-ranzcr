# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=jupyter/tensorflow-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

# USER $NB_UID
USER root

# installs packages without using the cache to save space
RUN pip install --quiet --no-cache-dir \
    'timm==0.3.2' \
    'efficientnet==1.1.1' \
    'kaggle==1.5.10' && \
    conda install --quiet --yes \
        'opencv' \
        'matplotlib-venn' && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

#A Dockerfile defines how an image is built, not how it's used - so you can't specify the bind mount in a Dockerfile.
# In docker-compose:
# Look in .kaggle/kaggle.json for Kaggle API Key
# Error out if not with proper directions
# Download Kaggle Dataset
# unzip and save to /data folder

# CMD ["kaggle competitions download -c ranzcr-clip-catheter-line-classification",
#    "unzip ranzcr-clip-catheter-line-classification.zip"]



# EXPOSE 8888

# Configure container startup
# ENTRYPOINT ["tini", "-g", "--"]
# CMD ["start-notebook.sh"]

# Copy local files as late as possible to avoid cache busting
# COPY start.sh start-notebook.sh start-singleuser.sh /usr/local/bin/
# COPY jupyter_notebook_config.py /etc/jupyter/

# Fix permissions on /etc/jupyter as root
# USER root
# RUN fix-permissions /etc/jupyter/

# Switch back to jovyan to avoid accidental container runs as root
# USER $NB_UID

# WORKDIR $HOME

# To run this file:
# docker build -t <nickname> .
# -t flag tags our image
# The . at the end of the docker build command tells that Docker should look for the Dockerfile in the current directory.

