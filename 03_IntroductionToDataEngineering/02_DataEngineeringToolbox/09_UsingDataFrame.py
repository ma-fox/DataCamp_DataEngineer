# A convenient way to parallelize an apply over several groups is using the dask framework
# and its abstraction of the pandas DataFrame, for example.
# The pandas DataFrame, athlete_events, is available in your workspace.


import dask.dataframe as dd

# Set the number of partitions
athlete_events_dask = dd.from_pandas(athlete_events, npartitions=4)
