import sys # Parameter passing
import timeit
import numpy as np # Creating 2 dimensional arrays instead of nesting lists
import matplotlib.pyplot as plt # Graphing
import math #log

# How to run:
# 'import *' causes warning in timeit
# run with: python -W ignore time.py N D
# e.g. python -W ignore time.py 1000 10

N = int(sys.argv[1]) # Size of input 
# Incr-Few input dataset fails on a swap if n<=2
if (N < 29) and (D>9):
  print('Minimum n is 3.')
  exit()
D = int(sys.argv[2]) # How to split up the total input (how many data pts)

# Dictionary for iterating through types of input data
# Random numbers are only pseudo-random...
#random.seed() # If parameter omitted, system time is used
# It is possible to create a "good-enough" (for security purposes) random
# from seeding information about the current state of your computer.
# ...or you can make up a seed for reproducibility.
inputs = { \
          'Increasing' : 's = [i for i in range(N)]',
          'Decreasing' : 's = [i for i in range(N)]; \
                          s.reverse()',
          'Random'     : 'import random; \
                         random.seed("cs350final"); \
                         s = [random.randint(0,N) for i in range(N)]',
          'Incr-3Swap' : 's = [i for i in range(N)]; \
                         mid = len(s)/2; t1 = len(s)/3; t3 = len(s)-t1; \
                         swap(s,0,len(s)-1); \
                         swap(s,mid,mid-1); \
                         swap(s,t1,t3)',
          'Incr-End'   : 's = [i for i in range(N-N/D)]; \
                         import random; \
                         s.extend([random.randint(0,N) for i in range(N/D)]);',
         }

# Dictionary for iterating through algorithms
  #graph label:function call for timeit
sorts = { \
    #'Insert':'ins(a)', 
         'Merge':'mrg(a)',
         'Timsort':'a.sort()',
         'Quick':'qck(a,0,len(a)-1)',
         'Quick(R)':'qcr(a,0,len(a)-1)',
         'Quick(M)':'qcm(a,0,len(a))',
        }

# Functions to compare against
fcts = ['n', 'n*n', 'nlogn']

# 2D array with numpy. Initialize to -1.
rows = len(sorts)+1+3 # 1 for x axis, 3 for n, n^2, nlogn
data = np.full(shape=(rows,D), fill_value=-1.0)
# ...or using nested lists...
#data = [[(i+1)*(N/D) for i in range(D)] for j in range(len(sorts+1))]

# Set up n, n^2, nlogn
n_graph = [float(i+1) for i in range(D)]
n2_graph = [float((i+1)*(i+1)) for i in range(D)]
log_graph = [(i+1)*math.log(i+1) for i in range(D)]
norm = max(n2_graph)
print(data)

t = 7 # trials
i = 100 # iterations per trial

for input_type,input_str in inputs.items():
  print(input_type)

  for d in range(1, D+1):
    n = (N/D)*d
    # n = (total test size N / ways to break up D) * multiplier
    # e.g. 1st arg, N = 1000
    #      2nd arg, D = 10
    #      and so n yields input size...
    # e.g. n = 100, 200, 300, .. , 900, 1000

    # "setup" program used by timeit.Timer
    # This is ran once at the beginning of timeit.Timer creation
    # Has to be inside for loop to avoid scope issues...
    # Newlines below avoids indentation error in timeit
    # ^ Indent error only occurs when adding a variable into docstring
    setup = '''
    \nfrom sorts import * # function names are same vals in 'sorts' dict 
    '''
    setup += '\nN = '+str(n)+'\n'
    setup += '\nD = '+str(D)+'\n'
    setup += '\n'+input_str+'\n'
    
    # Beginning of timing... for each input size, n...
    print('n = {}'.format(n))
    data[0,d-1] = n # Build x-axis 
    data[rows-3] = [x/norm for x in n_graph]
    data[rows-2] = [x/norm for x in n2_graph]
    data[rows-1] = [x/norm for x in log_graph]

    # Time
    row = 1
    for k,v in sorts.items():
      time = 0
      try:
        time = min(timeit.Timer('a=s[:];'+v,setup=setup).repeat(t,i))
      except RuntimeError:
        print('Possible max recursion depth reached.')
      print(k+': {} s'.format(time))
      data[row,d-1] = time
      row += 1


  # Plot each sort one at a time (each row in 2d-array at a time)
  row = 1
  for k,v in sorts.items():
    plt.plot(data[0,:], data[row,:], label=k)
    row += 1

  # Plot n, n^2, nlogn based on max time value from 2d array
  # and scale to max time value
  data_max = np.max(data[1:rows-3])
  data[3:,:] = data[3:,:] * data_max

  # Plot functions to compare against
  for r in range(1,len(fcts)+1):
    print(r)
    plt.plot(data[0,:], data[rows-r,:], '.', label=fcts[r-1])

  # Set up graph
  plt.xlabel('Input Size (n)')
  plt.ylabel('Time (seconds)')
  plt.title(input_type)
  plt.legend(loc='upper left')
  plt.savefig('./out/sort_'+input_type+'_'+str(N)+'.png')
  plt.clf()

  # Also save as CSV just because...
  #np.savetxt('./out/sort_'+input_type+'_'+str(N)+'.csv', data, delimiter=',')
