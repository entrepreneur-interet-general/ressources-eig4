from prefect import task, Flow

@task
def extract() -> list :
    """Get a list of data"""
    data = [1, 2, 3]
    print("Here's your output data: {}".format(data))
    return data

@task
def transform(data: list) -> list :
    """Multiply the input by 10"""
    return [x * 10 for x in data] 

@task
def load(data: list):
    """Print the data to indicate it was received"""
    print("Here's your output data: {}".format(data))

# Set dependency graph
with Flow('ETL') as flow:
    e = extract()
    t = transform(e)
    l = load(t)

# flow.run() # prints "Here's your data: [10, 20, 30]"