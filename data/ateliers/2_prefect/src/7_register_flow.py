from flow import flow

from prefect.environments.storage import Docker

# Docker storage
flow.storage = Docker(registry_url="gcr.io/quetzal-omind/flows") #'quetzal-omind'  is the name of GCP project

# Register flow
flow.register(project_name='EIG Demo') # 'Execution Layer Demo'  is the name of Prefect project

# Run agent
flow.run_agent()

