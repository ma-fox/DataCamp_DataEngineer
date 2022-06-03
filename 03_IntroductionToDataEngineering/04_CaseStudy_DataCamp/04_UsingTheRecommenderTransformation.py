## Using the recommender transformation
# Here are the decision rules for producing recommendations:

# - Use technology a student has rated the most.
# - Exclude courses a student has already rated.
# - Find the three top-rated courses from eligible courses.

# Complete the transformation function
def transform_recommendations(avg_course_ratings, courses_to_recommend):
    # Merge both DataFrames
    merged = courses_to_recommend.merge(avg_course_ratings)
    # Sort values by rating and group by user_id
    grouped = merged.sort_values("rating", ascending=False).groupby('user_id')
    # Produce the top 3 values and sort by user_id
    recommendations = grouped.head(3).sort_values("user_id").reset_index()
    final_recommendations = recommendations[["user_id", "course_id", "rating"]]
    # Return final recommendations
    return final_recommendations


# Use the function with the predefined DataFrame objects
recommendations = transform_recommendations(avg_course_ratings,
                                            courses_to_recommend)
