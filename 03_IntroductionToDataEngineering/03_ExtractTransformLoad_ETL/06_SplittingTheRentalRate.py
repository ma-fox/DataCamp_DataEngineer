## Splitting the rental rate

# Get the rental rate column as a string
rental_rate_str = film_df.rental_rate.astype(str)

# Split up and expand the column
rental_rate_expanded = rental_rate_str.str.split('.', expand=True)

# Assign the columns to film_df
# The previous splitted string contains two columns
# They are adressed respectively as rental_rate_expanded[0] and rental_rate_expanded[1]
film_df = film_df.assign(
    rental_rate_dollar=rental_rate_expanded[0],
    rental_rate_cents=rental_rate_expanded[1],
)
