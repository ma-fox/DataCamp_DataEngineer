# One-time calculation loop

# Import Counter from the collections module.
from collections import Counter

# A list of integers that represents each Pokémon's generation called generations:
generations = [4, 1, 3, 5, 1, 3, 2, 1, 5, 3, 6, 4, 5, 2, 3, 1, 1, 4, 5, 5, 2, 3, 6, 3, 1, 5, 6, 6, 5, 4, 2, 3, 3, 3, 3, 6, 3, 5, 4, 2, 5, 3, 1, 5, 3, 2, 1, 6, 4, 4, 6, 5, 1, 3, 2, 5, 5, 4, 5, 6, 5, 3, 4, 4, 4, 4, 1, 4, 6, 4, 1, 3, 3, 3, 6, 4, 5, 3, 3, 3, 1, 2, 5, 1, 1, 1, 1, 4, 4, 4, 6, 6, 2, 4, 3, 2, 4, 5, 3, 6, 6, 3, 1, 1, 2, 1, 5, 5, 4, 3, 5, 3, 2, 5, 3, 4, 3, 4, 4, 2, 2, 5, 5, 5, 1, 2, 4, 5, 5, 5, 6, 5, 5, 3, 2, 6, 1, 5, 4, 6, 6, 1, 1, 1, 1, 2, 6, 6, 1, 1, 4, 1, 4, 4, 5, 1, 5, 5, 1, 2, 5, 5, 3, 4, 3, 3, 5, 5, 5, 1, 1, 1, 4, 3, 1, 2, 5, 5, 5, 4, 2, 5, 2, 6, 5, 1, 1, 3, 1, 1, 3, 6, 2, 5, 5, 4, 2, 6, 1, 6, 6, 4, 6, 6, 3, 5, 2, 5, 5, 6, 6, 4, 6, 2, 4, 4, 5, 5, 4, 3, 1, 4, 5, 1, 1, 4, 5, 2, 4, 3, 4, 2, 4, 1, 6, 1, 1, 1, 1, 5, 5, 6, 6, 3, 5, 5, 5, 2, 1, 6, 1, 4, 3, 3, 3, 1, 3, 3, 5, 1, 4, 3, 1, 6, 5, 5, 4, 6, 6, 2, 5, 4, 4, 1, 1, 2, 2, 4, 6, 2, 2, 1, 2, 2, 3, 5, 1, 2, 3, 4, 6, 1, 5, 1, 3, 1, 5, 2, 1, 1, 1, 1, 1, 1, 5, 3, 2, 1, 3, 5, 6, 5, 5, 1, 1, 4, 4, 5, 5, 3, 3, 5, 5, 5, 3, 5, 2, 1, 5, 2, 3, 3, 4, 5, 2, 2, 4, 1, 5, 3, 5, 5, 3, 6, 5, 3, 4, 3, 3, 4, 3, 2, 4, 3, 3, 4, 4, 1, 1, 1, 2, 2, 1, 1, 4, 1, 1, 4, 3, 6, 4, 4, 5, 3, 1, 2, 4, 5, 2, 2, 1, 3, 3, 3, 3, 3, 6, 6, 1, 4, 3, 3, 1, 1, 1, 5, 5, 3, 3, 2, 4, 5, 3, 2, 4, 1, 4, 4, 1, 3, 1, 4, 5, 2, 5, 2, 1, 1, 1, 1, 1, 1, 3, 1, 3, 2, 6, 6, 3, 3, 3, 2, 1, 1, 1, 1, 5, 4, 4, 5, 6, 6, 5, 5, 5, 1, 1, 5, 5, 3, 1, 5, 2, 6, 4, 2, 1, 1, 1, 5, 5, 1, 2, 2, 1, 4, 3, 2, 1, 1, 1, 1, 3, 1, 4, 2, 1, 4, 4, 1, 2, 5, 4, 6, 2, 2, 6, 2, 1, 2, 3, 4, 1, 1, 1, 3, 3, 4, 3, 3, 3, 2, 5, 5, 1, 1, 4, 4, 5, 3, 4, 4, 4, 4, 4, 4, 4, 5, 3, 3, 5, 5, 1, 1, 5, 5, 6, 3, 2, 5, 5, 5, 1, 1, 1, 3, 3, 1, 5, 2, 5, 5, 3, 5, 3, 3, 3, 1, 4, 5, 4, 3, 4, 3, 2, 3, 5, 3, 5, 5, 5, 2, 6, 2, 3, 4, 6, 4, 3, 3, 6, 1, 2, 1, 2, 6, 2, 2, 2, 5, 1, 3, 4, 2, 5, 3, 1, 6, 3, 2, 3, 4, 3, 6, 1, 2, 4, 4, 4, 1, 1, 2, 5, 5, 4, 2, 2, 2, 2, 3, 3, 5, 3, 3, 5, 3, 2, 6, 5, 6, 3, 6, 1, 4, 1, 2, 1, 1, 5, 5, 5, 5, 5, 4, 2, 2, 3, 3, 4, 2, 4, 5, 3, 3, 6, 3, 5, 4, 5, 5, 2, 2, 6, 2, 6, 2, 5, 2, 2, 4, 5, 5, 5, 1, 5, 1, 1, 1, 4, 3, 5, 1, 3, 1, 5, 6, 3, 6, 5, 1, 5, 1, 3, 3, 3, 1, 5, 4, 1, 1, 1, 5, 5, 3, 3, 1, 3, 2, 5, 2, 4, 4, 4, 3, 3, 2, 6, 5, 2, 4, 6, 3, 1, 5, 5, 3, 5, 5, 1, 5]

# Collect the count of each generation
gen_counts = Counter(generations)

# In [5]: gen_counts
# Out[5]: Counter({4: 112, 1: 151, 3: 136, 5: 154, 2: 99, 6: 68})

# You'd like to gather the counts of each generation and determine what percentage each generation accounts for out of the total count of integers.
# The below loop was written to accomplish this task:

for gen,count in gen_counts.items():
    total_count = len(generations)
    gen_percent = round(count / total_count * 100, 2)
    print(
      'generation {}: count = {:3} percentage = {}'
      .format(gen, count, gen_percent)
    )
# Let's make this loop more efficient by moving a one-time calculation outside the loop.


# Use Counter() to collect the count of each generation from the generations list. Save this as gen_counts.
# Write a better for loop that places a one-time calculation outside (above) the loop.



# Improve for loop by moving one calculation above the loop
total_count = len(generations)

# In [7]: total_count
# Out[7]: 720

for gen,count in gen_counts.items():
    gen_percent = round(count / total_count * 100, 2)
    print('generation {}: count = {:3} percentage = {}'
          .format(gen, count, gen_percent))
#    output:
# generation 4: count = 112 percentage = 15.56
# generation 1: count = 151 percentage = 20.97
# generation 3: count = 136 percentage = 18.89
# generation 5: count = 154 percentage = 21.39
# generation 2: count =  99 percentage = 13.75
# generation 6: count =  68 percentage = 9.44


# Well done! You spotted a calculation that could be moved outside a loop to make the loop more efficient.
# Since the total count is now calculated just once (and not with each loop iteration), you can expect to see an efficiency gain with your new loop.
# When writing a loop is unavoidable, be sure to analyze the loop and move any one-time calculations outside.
