from prefect import Task, Flow

class Extract(Task):
    def run(self) -> list:
        """Get a list of data"""
        data = [1, 2, 3]
        print("Here's your output data: {}".format(data))
        return data


class Transform(Task):
    def run(self, data: list) -> list:
        """Multiply the input by 10"""
        return [x * 10 for x in data] 

class Load(Task):
    def run(self, data: list):
        """Print the data to indicate it was received"""
        print("Here's your output data: {}".format(data))

# Define Tasks in a Flow Context
e = Extract()
t = Transform()
l = Load()
flow = Flow('ETL')

# Set dependency graph
flow.set_dependencies(t, keyword_tasks={'data': e})
flow.set_dependencies(l, keyword_tasks={'data': t})

# flow.run() # prints "Here's your data: [10, 20, 30]"