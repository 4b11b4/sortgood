import timeit

setup = '''
import random
N = 1000
random.seed('slartibartfast')
s = [random.random() for i in range(N)]
'''

print(min(timeit.Timer('a=s[:]', setup=setup).repeat(7, 1000)))
