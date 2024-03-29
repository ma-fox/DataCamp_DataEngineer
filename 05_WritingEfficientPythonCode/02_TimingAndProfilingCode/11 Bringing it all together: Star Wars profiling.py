Bringing it all together: Star Wars profiling
A list of 480 superheroes has been loaded into your session (called heroes) as well as a list of each hero's corresponding publisher (called publishers).

You'd like to filter the heroes list based on a hero's specific publisher, but are unsure which of the below functions is more efficient.

def get_publisher_heroes(heroes, publishers, desired_publisher):

    desired_heroes = []

    for i,pub in enumerate(publishers):
        if pub == desired_publisher:
            desired_heroes.append(heroes[i])

    return desired_heroes



def get_publisher_heroes_np(heroes, publishers, desired_publisher):

    heroes_np = np.array(heroes)
    pubs_np = np.array(publishers)

    desired_heroes = heroes_np[pubs_np == desired_publisher]

    return desired_heroes





Use the get_publisher_heroes() function and the get_publisher_heroes_np() function to collect heroes from the Star Wars universe. The desired_publisher for Star Wars is 'George Lucas'.
# Use get_publisher_heroes() to gather Star Wars heroes
star_wars_heroes = get_publisher_heroes(heroes, publishers, 'George Lucas')

print(star_wars_heroes)
print(type(star_wars_heroes))

<script.py> output:
    ['Darth Vader', 'Han Solo', 'Luke Skywalker', 'Yoda']
    <class 'list'>



# Use get_publisher_heroes_np() to gather Star Wars heroes
star_wars_heroes_np = get_publisher_heroes_np(heroes, publishers, 'George Lucas')

print(star_wars_heroes_np)
print(type(star_wars_heroes_np))


<script.py> output:
    ['Darth Vader' 'Han Solo' 'Luke Skywalker' 'Yoda']
    <class 'numpy.ndarray'>







Within your IPython console, load the line_profiler and use %lprun to profile the two functions for line-by-line runtime. When using %lprun, use each function to gather the Star Wars heroes as you did in the previous step. After you've finished profiling, answer the following question:
%load_ext line_profiler

%lprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, 'George Lucas')
Timer unit: 1e-06 s

Total time: 0.000303 s
File: <ipython-input-1-5a6bc05c1c55>
Function: get_publisher_heroes at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def get_publisher_heroes(heroes, publishers, desired_publisher):
     2
     3         1          2.0      2.0      0.7      desired_heroes = []
     4
     5       481        151.0      0.3     49.8      for i,pub in enumerate(publishers):
     6       480        136.0      0.3     44.9          if pub == desired_publisher:
     7         4         13.0      3.2      4.3              desired_heroes.append(heroes[i])
     8
     9         1          1.0      1.0      0.3      return desired_heroes




%lprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes, publishers, 'George Lucas')
Timer unit: 1e-06 s

Total time: 0.000134 s
File: <ipython-input-1-5a6bc05c1c55>
Function: get_publisher_heroes_np at line 12

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    12                                           def get_publisher_heroes_np(heroes, publishers, desired_publisher):
    13
    14         1         77.0     77.0     57.5      heroes_np = np.array(heroes)
    15         1         37.0     37.0     27.6      pubs_np = np.array(publishers)
    16
    17         1         19.0     19.0     14.2      desired_heroes = heroes_np[pubs_np == desired_publisher]
    18
    19         1          1.0      1.0      0.7      return desired_heroes




Which function has the fastest runtime?
get_publisher_heroes() is faster.
Both functions have the same runtime.

#YES - get_publisher_heroes_np() is faster.
















Within your IPython console, load the memory_profiler and use %mprun to profile the two functions for line-by-line memory consumption.
The get_publisher_heroes() function and get_publisher_heroes_np() function have been saved within a file titled hero_funcs.py (i.e., you can import both functions from hero_funcs). When using %mprun, use each function to gather the Star Wars heroes as you did in the previous step. After you've finished profiling, answer the following question:

from hero_funcs import get_publisher_heroes, get_publisher_heroes_np
%load_ext memory_profiler

%mprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, 'George Lucas')
Filename: /tmp/tmpysxdmqmm/hero_funcs.py

Line #    Mem usage    Increment   Line Contents
================================================
     4    107.1 MiB    107.1 MiB   def get_publisher_heroes(heroes, publishers, desired_publisher):
     5
     6    107.1 MiB      0.0 MiB       desired_heroes = []
     7
     8    107.1 MiB      0.0 MiB       for i,pub in enumerate(publishers):
     9    107.1 MiB      0.0 MiB           if pub == desired_publisher:
    10    107.1 MiB      0.0 MiB               desired_heroes.append(heroes[i])
    11
    12    107.1 MiB      0.0 MiB       return desired_heroes



%mprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes, publishers, 'George Lucas')
Filename: /tmp/tmpysxdmqmm/hero_funcs.py

Line #    Mem usage    Increment   Line Contents
================================================
    15    107.1 MiB    107.1 MiB   def get_publisher_heroes_np(heroes, publishers, desired_publisher):
    16
    17    107.1 MiB      0.0 MiB       heroes_np = np.array(heroes)
    18    107.1 MiB      0.0 MiB       pubs_np = np.array(publishers)
    19
    20    107.1 MiB      0.0 MiB       desired_heroes = heroes_np[pubs_np == desired_publisher]
    21
    22    107.1 MiB      0.0 MiB       return desired_heroes




Which function uses the least amount of memory?
get_publisher_heroes() consumes less memory.
get_publisher_heroes_np() consumes less memory.

#YES - Both functions have the same memory consumption.


















Based on your runtime profiling and memory allocation profiling, which function would you choose to gather Star Wars heroes?

I would use get_publisher_heroes().
I could use either function since their runtimes, and memory usage were identical.

#YES - I would use get_publisher_heroes_np().
The Force is strong with this one! You're timing and profiling like a true Jedi. Now that you have the tools to evaluate code efficiencies, it's time to put them to use and start writing efficient Python code.
