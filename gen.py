import random
import time
import timeit
import functools

def basic_sort(n):
  n.sort()

if __name__ == '__main__':
  NUM = 50
  n = [random.randint(-50, 100) for c in range(NUM)]
  print(n)

  """
  beg = time.perf_counter()
  n.sort()
  end = time.perf_counter()
  print('dif: {} sec'.format(end-beg))
  print(n)
  """

  t = timeit.Timer(functools.partial(basic_sort, n))
  print(t.timeit(5))
  
  '''
  print(timeit.timeit(stmt="basic_sort(n)", globals=globals(), \
                      number=10000))

  print(timeit.timeit(stmt="basic_sort(n)", globals=globals(), \
                      setup="", number=10000))
  '''

  print(n)
