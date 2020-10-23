import time

from prefect.engine.executors import DaskExecutor

from flow_3_parameter import flow


# dask-scheduler --port 8000
# dask-worker {your scheduler host:port}

executor = DaskExecutor(address="172.20.10.4:8000") # change this to yours # LOCAL
# executor = DaskExecutor(address="34.76.194.137:8786") # change this to yours # GCP


length = 100

flow.run(executor=executor, parameters={'factor': 2, 'length': length }) 

