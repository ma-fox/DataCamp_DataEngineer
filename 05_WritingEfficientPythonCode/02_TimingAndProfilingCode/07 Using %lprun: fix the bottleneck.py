Using %lprun: fix the bottleneck
In the previous exercise, you profiled the convert_units() function and saw that the new_hts list comprehension could be a potential bottleneck. Did you notice that the new_wts list comprehension also accounted for a similar percentage of the runtime? This is an indication that you may want to create the new_hts and new_wts objects using a different technique.

Since the height and weight of each hero is stored in a numpy array, you can use array broadcasting rather than list comprehension to convert the heights and weights. This has been implemented in the below function:

def convert_units_broadcast(heroes, heights, weights):

    # Array broadcasting instead of list comprehension
    new_hts = heights * 0.39370
    new_wts = weights * 2.20462

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data
Load the line_profiler package into your IPython session. Then, use %lprun to profile the convert_units_broadcast() function acting on your superheroes data. The convert_units_broadcast() function, heroes list, hts array, and wts array have been loaded into your session. After you've finished coding, answer the following question:



In [2]: %lprun -f convert_units_broadcast convert_units_broadcast(heroes,hts,wts)
Timer unit: 1e-06 s

Total time: 0.000587 s
File: <ipython-input-4-84e44a6b12f5>
Function: convert_units_broadcast at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def convert_units_broadcast(heroes, heights, weights):
     2
     3                                               # Array broadcasting instead of list comprehension
     4         1         23.0     23.0      3.9      new_hts = heights * 0.39370
     5         1          4.0      4.0      0.7      new_wts = weights * 2.20462
     6
     7         1          1.0      1.0      0.2      hero_data = {}
     8
     9       481        239.0      0.5     40.7      for i,hero in enumerate(heroes):
    10       480        319.0      0.7     54.3          hero_data[hero] = (new_hts[i], new_wts[i])
    11
    12         1          1.0      1.0      0.2      return hero_data



What percentage of time is spent on the new_hts array broadcasting line of code relative to the total amount of time spent in the convert_units_broadcast() function?
11% - 20%
21% - 50%
51% - 100%

#YES - 0% - 10%
That's correct! By profiling the convert_units() function, you were able to see that using list comprehension was not the most efficient solution for creating the new_hts and new_wts objects. You also saw that using array broadcasting in the convert_units_broadcast() function dramatically decreased the percentage of time spent executing these lines of code. You may have noticed that your function still takes a while to iterate through the for loop. Don't worry; you'll cover how to make this loop more efficient in a later chapter.
