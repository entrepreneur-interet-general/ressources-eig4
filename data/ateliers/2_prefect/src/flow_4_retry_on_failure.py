from datetime import timedelta

from prefect import task, Flow, Parameter, unmapped
from prefect.engine.results import LocalResult
from prefect.triggers import some_successful

# Configurable value taken at runtime
factor = Parameter(name="factor", default=10, required=False)

@task
def extract() -> list :
    """Get a list of data"""
    data = [1, 2, 3]
    print("Here's your output data: {}".format(data))
    return data

def DoNotLikeEven(Exception):
    pass

@task(name="multiply input if even", max_retries=3, retry_delay=timedelta(seconds=5))
def transform(x: int, factor: int) -> int :
    """Multiply the input by `factor`"""
    if (x % 2) == 0: 
        raise DoNotLikeEven(f'Do not like even numbers and received {x}')  
    return x * factor

@task(trigger=some_successful(at_least=1, at_most=6))
def load(data: list):
    """Print the data to indicate it was received"""
    print("Here's your output data: {}".format(data))

# Set dependency graph
with Flow('ETL', result=LocalResult("./local_result")) as flow:
    e = extract()
    t = transform.map(e, unmapped(factor))
    l = load(t)

# flow.run(parameters={'factor': 10}) 
# ValueError: Do not like even numbers and received 2
# ValueError: Do not like even numbers and received 2
# ValueError: Do not like even numbers and received 2
# Here's your output data: [10, ValueError('Do not like even numbers and received 2'), 30]
# <Success: "All reference tasks succeeded.">