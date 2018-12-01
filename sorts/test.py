import random
from sorts import * # functions are named insert1, insert2, etc.

def is_inc(lst):
  for x in range(len(lst)-1):
    if lst[x] > lst[x+1]:
      return False
  return True

def swap(lst, i1, i2):
  temp = i1
  lst[i1] = lst[i2]
  lst[i2] = temp

def main():
  # Set up basic input
  N = 100 
  random.seed('cs350final') #If parameter omitted, system time is used
  s = [random.randint(0,N) for i in range(N)]

  # Insertion Sort
  a = s[:]
  exec('ins(a)') # run the function 
  #swap(a, 0, 10)
  print('ins: {}'.format(is_inc(a)))

  # Merge Sort 
  a = s[:]
  mrg(a)
  #swap(a, 0, 10)
  print('mrg: {}'.format(is_inc(a)))

  # quicksort 
  a = s[:]
  qck(a, 0, len(a)-1)
  #print(a)
  #swap(a, 0, 10)
  print('qck: {}'.format(is_inc(a)))

  # quicksort 
  a = s[:]
  qck_r(a, 0, len(a)-1)
  #print(a)
  #swap(a, 0, 10)
  print('qck_r1: {}'.format(is_inc(a)))

  # quicksort 
  a = s[:]
  qck_m(a, 0, len(a))
  #print(a)
  #swap(a, 0, 10)
  print('quick_m1: {}'.format(is_inc(a)))

if __name__ == '__main__':
  main()
