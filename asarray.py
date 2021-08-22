import numpy as np

# example1
x = [1, 2, 3]
a = np.asarray(x)
print(a)
print(a.itemsize)
x = [(1, 2), (3, 4), (5, 6)]
a = np.asarray(x)
print(a)
print(a.itemsize)

# example2
x = (1, 2, 3)
a = np.asarray(x)
print(a)

# example3
x = [(1, 2, 3), (4, 5)]
a = np.asarray(x)
print(a)
print(a.itemsize)

# example4
x = [1, 2, 3]
a = np.asarray(x, dtype=float)
print(a)

# example5
s = b'Hello World'
a = np.frombuffer(s, dtype='S1')
print(a)

# example6
lst = range(5)
it = iter(lst)
x = np.fromiter(it, dtype=float)
print(x)
