# In Airflow, a pipeline is represented as a Directed Acyclic Graph or DAG.
# The nodes of the graph represent tasks that are executed.
# The directed connections between nodes represent dependencies between the tasks.

# Create the DAG object
dag = DAG(dag_id="car_factory_simulation",
          default_args={
              "owner": "airflow",
              "start_date": airflow.utils.dates.days_ago(2)
          },
          schedule_interval="0 * * * *")
