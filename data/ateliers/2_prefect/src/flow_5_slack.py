from datetime import timedelta
import os

from prefect import task, Flow, Parameter, unmapped
from prefect.engine.results import LocalResult
from prefect.triggers import some_successful
from prefect.utilities.notifications import slack_notifier

# this should be secret
# export PREFECT__CONTEXT__SECRETS__SLACK_WEBHOOK_URL='https://hooks.slack.com/services/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'

# Configurable value taken at runtime
factor = Parameter(name="factor", default=10, required=False)

@task
def extract() -> list :
    """Get a list of data"""
    data = [1, 3, 5]
    print("Here's your output data: {}".format(data))
    return data

def DoNotLikeEven(Exception):
    pass

@task(name="multiply input if even", max_retries=1, retry_delay=timedelta(seconds=5))
def transform(x: int, factor: int) -> int :
    """Multiply the input by `factor`"""
    if (x % 2) == 0: 
        raise DoNotLikeEven(f'Do not like even numbers and received {x}')  
    return x * factor

@task(trigger=some_successful(at_least=1, at_most=6), state_handlers=[slack_notifier])
def load(data: list):
    """Print the data to indicate it was received"""
    print("Here's your output data: {}".format(data))

# Set dependency graph
with Flow('ETL') as flow:
    e = extract()
    t = transform.map(e, unmapped(factor))
    l = load(t)


# with prefect.context(secrets=dict(SLACK_WEBHOOK_URL="https://hooks.slack.com/services/XXX" )):
#     flow.run()quit()