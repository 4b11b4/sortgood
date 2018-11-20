import time

n = [random.randint(-50, 100) for c in range(100)]
print(n)
beg = time.perf_counter()
n.sort()
print('dif: {} sec'.format(time.perf_counter()-beg))
