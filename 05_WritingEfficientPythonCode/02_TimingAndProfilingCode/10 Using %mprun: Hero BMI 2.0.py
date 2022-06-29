Using %mprun: Hero BMI 2.0
Let's see if using a different approach to calculate the BMIs can save some memory. If you remember, each hero's height and weight is stored in a numpy array. That means you can use NumPy's handy array indexing capabilities and broadcasting to perform your calculations. A function named calc_bmi_arrays has been created and saved to a file titled bmi_arrays.py. For convenience, it is displayed below:

def calc_bmi_arrays(sample_indices, hts, wts):

    # Gather sample heights and weights as arrays
    s_hts = hts[sample_indices]
    s_wts = wts[sample_indices]

    # Convert heights from cm to m and square with broadcasting
    s_hts_m_sqr = (s_hts / 100) ** 2

    # Calculate BMIs as an array using broadcasting
    bmis = s_wts / s_hts_m_sqr

    return bmis
Notice that this function performs all necessary calculations using arrays.

Let's see if this updated array approach decreases your memory footprint:

Load the memory_profiler package into your IPython session.
Import calc_bmi_arrays from bmi_arrays.
Once you've completed the above steps, use %mprun to profile the calc_bmi_arrays() function acting on your superheroes data. The sample_indices array, hts array, and wts array have been loaded into your session.
After you've finished coding, answer the following question:






In [2]: from bmi_arrays import calc_bmi_arrays

In [3]: %load_ext memory_profiler
The memory_profiler extension is already loaded. To reload it, use:
  %reload_ext memory_profiler

In [4]: %mprun -f calc_bmi_arrays calc_bmi_arrays(sample_indices, hts, wts)
Filename: /tmp/tmp4kivv76j/bmi_arrays.py

Line #    Mem usage    Increment   Line Contents
================================================
     1    107.2 MiB    107.2 MiB   def calc_bmi_arrays(sample_indices, hts, wts):
     2
     3                                 # Gather sample heights and weights as arrays
     4    107.2 MiB      0.0 MiB       s_hts = hts[sample_indices]
     5    107.2 MiB      0.0 MiB       s_wts = wts[sample_indices]
     6
     7                                 # Convert heights from cm to m and square with broadcasting
     8    107.4 MiB      0.2 MiB       s_hts_m_sqr = (s_hts / 100) ** 2
     9
    10                                 # Calculate BMIs as an array using broadcasting
    11    107.4 MiB      0.0 MiB       bmis = s_wts / s_hts_m_sqr
    12
    13    107.4 MiB      0.0 MiB       return bmis



How much memory do the array indexing and broadcasting lines of code consume in the calc_bmi_array() function? (i.e., what is the total sum of the Increment column for these four lines of code?)
10.0 MiB - 15.0 MiB
0.0 MiB
20.0 MiB - 30.0 MiB

#YES - 0.1 MiB - 2.0 MiB
That's right! By implementing an array approach, you were able to shave off a few MiBs. Although this isn't a colossal gain, it still decreases your code's overhead. If your input data grows over time, these small improvements could add up to some major efficiency gains.
