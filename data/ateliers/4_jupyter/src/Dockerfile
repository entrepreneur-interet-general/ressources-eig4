# FROM python:3.8
FROM jupyter/base-notebook

ARG UID

ENV JUPYTER_ENABLE_LAB=yes
ENV NB_UID=$UID
ENV NB_GROUP=$UID
ENV GRANT_SUDO=yes

USER root
# Pyspark
WORKDIR /opt/
RUN apt-get update && \
    apt install default-jdk scala git nodejs npm -y
RUN wget https://downloads.apache.org/spark/spark-3.0.1/spark-3.0.1-bin-hadoop2.7.tgz
RUN tar xvf spark-*
RUN mv spark-3.0.1-bin-hadoop2.7 /opt/spark
ENV SPARK_HOME=/opt/spark
RUN pip install --trusted-host files.pythonhosted.org pyspark findspark pyarrow

# Jupyterlab
RUN pip install --trusted-host files.pythonhosted.org ipywidgets
RUN jupyter nbextension enable --py widgetsnbextension
RUN jupyter labextension install jupyterlab-plotly plotlywidget @jupyter-widgets/jupyterlab-manager

RUN apt-get install -y libpq-dev
# Repos requirements
RUN mkdir -p /home/jovyan/work
WORKDIR /home/jovyan/work
COPY src/requirements.txt .
RUN pip install --trusted-host files.pythonhosted.org -r requirements.txt

ENV PYTHONPATH "${PYTONPATH}:/home/jovyan/work"
USER $NB_UID

# CMD ["bash", "jupyter.sh"]
