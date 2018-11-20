
import timeit

setup = '''
import random

N = 100
random.seed('slartibartfast')
s = [random.random() for i in range(N)]

def insertion_sort(m):
  """
  Public: Sorts a list using the insertion sort algorithm.
  m - The unsorted list.
  Examples
    insertion_sort([4,7,8,3,2,9,1])
    # => [1,2,3,4,7,8,9]
  Worst Case: O(n^2)
  Returns the sorted list.
  """

  for j in range(1, len(m)):
    key = m[j]
    i = j - 1

    # shift everything greater than 'key' to it's right
    while i >= 0 and m[i] > key:
      m[i + 1] = m[i]
      i = i - 1

    m[i + 1] = key

  return m
'''

print(min(timeit.Timer('a=s[:]; insertion_sort(a)', setup=setup).repeat(7, 1000)))
