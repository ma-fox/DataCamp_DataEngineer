## Read from a database

# Function to extract table to a pandas DataFrame
def extract_table_to_pandas(tablename, db_engine):
    query = "SELECT * FROM {}".format(tablename)
    return pd.read_sql(query, db_engine)

# Connect to the database using the connection URI

# connection_uri is a string that contains the information needed to connect to the database
connection_uri = "postgresql://repl:password@localhost:5432/pagila"

# db_engine is a SQLAlchemy engine object that contains the connection information
db_engine = sqlalchemy.create_engine(connection_uri)

# Extract the film table into a pandas DataFrame
extract_table_to_pandas('film', db_engine)

# Extract the customer table into a pandas DataFrame
extract_table_to_pandas('customer', db_engine)
