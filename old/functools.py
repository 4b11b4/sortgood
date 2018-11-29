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
