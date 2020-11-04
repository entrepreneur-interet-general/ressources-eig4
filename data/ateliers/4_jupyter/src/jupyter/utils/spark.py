import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

import pyspark
from pyspark.sql import SQLContext

NUMBER_CORES = int(os.getenv("PYSPARK_NUMBER_CORES", default=4))
MEMORY_GB = int(os.getenv("PYSPARK_MEMORY_GB", default=10))


def get_spark_local_conf(
    app_name: str, number_cores: int, memory_gb: int
) -> pyspark.SparkConf:
    conf = (
        pyspark.SparkConf()
        .setAppName(app_name)
        .setMaster("local[{}]".format(number_cores))
        .set("spark.driver.memory", "{}g".format(memory_gb))
    )
    return conf


def get_spark_context_from_conf(spark_conf: pyspark.SparkConf) -> pyspark.SparkContext:
    sc = pyspark.SparkContext.getOrCreate(conf=spark_conf)
    return sc


def get_spark_context(
    app_name: str = "notebooks",
    number_cores: int = NUMBER_CORES,
    memory_gb: int = MEMORY_GB,
) -> pyspark.SparkContext:
    conf = get_spark_local_conf(app_name, number_cores, memory_gb)
    sc = get_spark_context_from_conf(conf)
    return sc


def get_spark_sql_context(
    app_name: str = "notebooks",
    number_cores: int = NUMBER_CORES,
    memory_gb: int = MEMORY_GB,
) -> pyspark.sql.SQLContext:
    sc = get_spark_context()
    sql_context = SQLContext(sc)
    return sql_context
