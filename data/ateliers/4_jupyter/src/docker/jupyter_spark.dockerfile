FROM jupyter-base

ARG UID

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

RUN apt-get install -y libpq-dev

# Repos requirements
RUN mkdir -p /home/jovyan/work
WORKDIR /home/jovyan/work
COPY jupyter/requirements-spark.txt .
RUN pip install -r requirements-spark.txt

ENV PYTHONPATH "${PYTONPATH}:/home/jovyan/work"
USER $NB_UID

# CMD ["bash", "jupyter.sh"]
