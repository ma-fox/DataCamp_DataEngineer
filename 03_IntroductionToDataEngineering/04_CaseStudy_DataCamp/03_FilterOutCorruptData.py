## Filter out corrupt data

course_data = extract_course_data(db_engines)

# Print out the number of missing values per column
print(course_data.isnull().sum())


# The transformation should fill in the missing values
def transform_fill_programming_language(course_data):
    imputed = course_data.fillna({"programming_language": "r"})
    return imputed

# This variable will hold the transformed data
transformed = transform_fill_programming_language(course_data)

# Print out the number of missing values per column of transformed
print(transformed.isnull().sum())
