from prefect import task, Flow, Parameter, unmapped

# Configurable value taken at runtime
length = Parameter(name="length", default=3, required=False)
factor = Parameter(name="factor", default=10, required=False)

@task
def extract(length: int) -> list :
    """Get a list of data"""
    data = list(range(length))
    print("Here's your output data: {}".format(data))
    return data

@task
def transform(x: int, factor: int) -> int :
    """Multiply the input by `factor`"""
    return x * factor

@task
def load(data: list):
    """Print the data to indicate it was received"""
    print("Here's your output data: {}".format(data))

# Set dependency graph
with Flow('ETL') as flow:
    e = extract(length)
    t = transform.map(e, unmapped(factor))
    l = load(t)

# flow.run(parameters={'factor': 2, 'length': 4 }) # "Here's your data: [0, 2, 4, 6]"
