
# Function to apply a function over multiple cores
@print_timing
def parallel_apply(apply_func, groups, nb_cores):
    with Pool(nb_cores) as p:
        results = p.map(apply_func, groups)
    return pd.concat(results)


# Complete the code, so you apply take_mean_age with 1 core first, then 2 and finally 4 cores.
# Parallel apply using 1 core
parallel_apply(take_mean_age, athlete_events.groupby('Year'), nb_cores=1)

# Parallel apply using 2 cores
parallel_apply(take_mean_age, athlete_events.groupby('Year'), nb_cores=2)

# Parallel apply using 4 cores
parallel_apply(take_mean_age, athlete_events.groupby('Year'), nb_cores=4)
