FROM jupyter/base-notebook

ARG UID

ENV JUPYTER_ENABLE_LAB=yes
ENV NB_UID=$UID
ENV NB_GROUP=$UID
ENV GRANT_SUDO=yes

USER root

# Jupyterlab
RUN pip install ipywidgets
RUN jupyter nbextension enable --py widgetsnbextension
RUN jupyter labextension install jupyterlab-plotly plotlywidget @jupyter-widgets/jupyterlab-manager

# Repos requirements
RUN mkdir -p /home/jovyan/work
WORKDIR /home/jovyan/work
COPY jupyter/requirements-base.txt .
RUN pip install -r requirements-base.txt

ENV PYTHONPATH "${PYTONPATH}:/home/jovyan/work"
USER $NB_UID
