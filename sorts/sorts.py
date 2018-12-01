import random

def swap(A, x, y):
  A[x],A[y]=A[y],A[x]

def ins(lst):
  """
  Insertion Sort:
    Maintain a sorted subarr of the arr from 0 to the current
    number. Copy the current number and shift all the numbers of
    the sorted subarr overwriting the copied number, once we get
    to a location where the key is in the right position stop
    shifting the numbers and insert the key.

  Run-time Worst Case: O(n^2)
    * 
  Run-time "Average" : O()
    * 
  """
  
  # Iterate L to R
    # Start: index=1 "position 1 in list"
      # * Why? 1st time thru while loop, we are at idx=1
      #   We then compare: lst[idx-1] < lst[idx] (i.e. lst[0] < list[1])
      #   (so we take care of idx=0 in the first step)
    # Stop: idx=len(lst)-1 "end of list"
      # range(1,n) returns [1, 2, 3, .. n-1]
  for idx in range(1, len(lst)):

    # Copy the current value as we are going L to R.
    # It will be written when we are done with the while loop below
    value_to_insert = lst[idx]
    
    # Save current idx as variable for iterating while loop from R to L
      #  for  loop goes L>>R
      # while loop goes L<<R
    pos = idx

    # Now go L<<<R and compare each value with the value to insert
    while lst[pos-1] > value_to_insert and pos > 0:
      
      # We already saved the value to insert.
      # Overwrite current value with value on the left (i.e. shift right).
      lst[pos] = lst[pos-1]

      # Keep going L in while loop until while loop condition fails
      # (cond: value "while" L<<R  >  value "for" L>>R)
      #                               (value to insert)
      pos = pos-1
   
    # If while loop stops going L<<R (by decrementing pos)...
      # value to insert > value to the left
      # (we are finally at the correct spot) 
    # Write the current value which we saved at this position.
    lst[pos] = value_to_insert

def mrg(lst): #mergesort
  """
  Merge Sort:

  Run-time Worst Case: O()
    * 
  Run-time Average   : O()
    * 
  """
  # If the size of the list is 1, don't make any more recursive calls
  if len(lst) > 1:
    mid = len(lst)/2

    # Requires extra arrs to pass to the recursive function call
    L = lst[:mid]
    R = lst[mid:]

    # Recursively call mergesort on the L and R halves.
    mrg(L)
    mrg(R)
    # After recursive calls, we know L and R half are sorted. Merge them.
    mer(L, R, lst)

def mer(L, R, lst): #merge helper function
  """
  Merge Function
  """
  i=j=k=0

  # Until we reach the end of one of the L or R
  while i < len(L) and j < len(R):
    # If (cur L val > cur R val)
      # Then add L val to list at position: k
    if L[i] < R[j]:
      lst[k]=L[i]
      i=i+1
    # Else (cur L val <= cur R val)
      # Add R val to list at position: k
    else:
      lst[k]=R[j]
      j=j+1
    k=k+1 # goto next position

  # If while loop exits, we are got to the end of L || R, but not L && R
  # Get any remaining values from L || R, whichever is not at the end yet 
  while i < len(L):
    lst[k]=L[i]
    i=i+1
    k=k+1
  while j < len(R):
    lst[k]=R[j]
    j=j+1
    k=k+1
 
def qck(arr, low, high): # Quicksort Simple Pivot
  """
  Quick Sort:

  Run-time Worst Case: O()
    * 
  Run-time Average   : O()
    * 
  """
  if low < high:
    # Find the place to split the array 
    pi = prt(arr, low, high)
    # Recursively sort elements before partition index and after index 
    qck(arr, low, pi-1)
    qck(arr, pi+1, high)

def qcr(arr, low, high): # Quicksort Random Pivot
  if low < high:
    pi = prt_r(arr, low, high)
    qcr(arr, low, pi-1)
    qcr(arr, pi+1, high)

def qcm(arr, low, high): # Quicksort Median-of-three Pivot
  if low < high:
    pi = prt_m(arr, low, high)
    qcm(arr, low, pi)
    qcm(arr, pi+1, high)

def prt(arr, low, high):
  pivot = arr[high]

  i = low-1

  for j in range(low, high):
    # If current element is smaller than or equal to pivot
    if arr[j] <= pivot:
      i = i+1
      swap(arr, i, j)

  swap(arr, i+1, high)
  return i+1
 
def prt_r(arr, low, high):
  pivot_idx = random.randint(low, high)
  pivot = arr[pivot_idx]

  i = low

  swap(arr, low, pivot_idx)

  for j in range(low , high+1):
    if arr[j] < pivot:
      i = i+1
      swap(arr, i, j)

  swap(arr, i, low)
  return i

def prt_m(arr, low, high):
  # Get index between low and high
  mid = ((high-1-low) / 2) + low

  # Check which is the median of: low, middle & high indices
  if (arr[mid] - arr[high-1]) * (arr[low] - arr[mid]) >= 0:
    swap(arr, low, mid)
  elif (arr[high-1] - arr[mid]) * (arr[low] - arr[high-1]) >= 0:
    swap(arr, low, high-1)

  # Use low index as pivot. If it was already the median, don't swap above.
  pivot = arr[low]

  i = low+1

  for j in range(low,high):
    if arr[j] < pivot:
      swap(arr, i, j)
      i = i+1

  swap(arr, i-1, low)
  return i-1
