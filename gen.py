'''
def basic_sort(n):
  n.sort()

if __name__ == '__main__':
  n = [random.randint(-50, 100) for c in range(100)]
  t = timeit.Timer(functools.partial(basic_sort, n))

  print(t.timeit(1))
  
  print(timeit.timeit(stmt="basic_sort(n)", globals=globals(), \
                      number=10000))

  print(timeit.timeit(stmt="basic_sort(n)", globals=globals(), \
                      setup="", number=10000))
'''

import timeit

setup = '''
import random

random.seed('slartibartfast')
s = [random.random() for i in range(1000)]
timsort = list.sort
'''

print(min(timeit.Timer('a=s[:]; timsort(a)', setup=setup).repeat(7, 1000)))
