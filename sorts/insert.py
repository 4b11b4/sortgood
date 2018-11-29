import timeit

setup = '''
import random

N = 1000
random.seed('slartibartfast')
#random.seed() #If parameter omitted, system time is used
s = [random.randint(0,1000) for i in range(N)]

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

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

def ainsertion(alist):
  list_size = len(alist)
  
  # Iterate from LEFT to RIGHT starting with index 1
  for idx in range(1, list_size):

    # Copy the current value
    # It will be inserted when we are done greater items shifting right
    value_to_insert = alist[idx]
    
    # Save index of current value which we will now use to go RIGHT to LEFT
    pos = idx

    # If item to the LEFT is greater than the value to insert
    # current item with the one to the LEFT
    while alist[pos-1] > value_to_insert and pos > 0:
      
      # We already saved the current value before going RIGHT to LEFT.
      # Overwrite the current spot with the one to the LEFT 
      alist[pos] = alist[pos-1]

      # Keep going left in the while loop until we find the place to insert 
      pos = pos-1
   
    # If we didn't keep going in the while loop, it means our value to insert
    # is greater than the one to the left and we are at the correct spot.
    # Insert the current value
    alist[pos] = value_to_insert

def Insertion_Sort(l):
    """Given an input list, returns a sorted permutation of the list
    using insertion sort (run time upper bound : n^2)"""
    # English description:
    # Maintain a sorted subarray of the array from 0 to the current
    # number. Copy the current number and shift all the numbers of
    # the sorted subarray overwriting the copied number, once we get
    # to a location where the key is in the right position stop
    # shifting the numbers and insert the key.
    for i in range(1, len(l)):
        # Copy the key value so we can overwrite it when shifting
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            # Shift over all the entries greater than key
            l[j+1] = l[j]
            j = j - 1
        # Now copy the key into the appropriate spot left by
        # shifting all the greater values over
        l[j+1] = key
    return l

'''
print('Total time for insertion sort with 1000 numbers:')
t = 1
i = 10
print("{} sec".format(min(timeit.Timer('a=s[:]; insertion_sort(a);', setup=setup).repeat(t, i))))
#print(min(timeit.Timer('a=s[:]; insertionSort(a); print(a)', setup=setup).repeat(t, i)))
#print(min(timeit.Timer('a=s[:]; ainsertion(a); print(a)', setup=setup).repeat(t, i)))
#print(min(timeit.Timer('a=s[:]; Insertion_Sort(a); print(a)', setup=setup).repeat(t, i)))
