# Sensors
Derives from `BaseSensorOperator`.
Has a `poke_interval` attribute.
`FileSensor`

# Both
Are assigned to DAGs.
Have a `task_id`.

# Operators
`BashOperator`
Only runs once per DAG run.
