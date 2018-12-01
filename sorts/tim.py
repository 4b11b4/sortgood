import timeit

setup = '''
import random

N = 10000
random.seed('slartibartfast')
s = [random.random() for i in range(N)]
timsort = list.sort
'''

print(min(timeit.Timer('a=s[:]; timsort(a)', setup=setup).repeat(7, 1000)))
