import numpy as np

# example1
a = np.arange(6).reshape(2, 3)
print(a)
for x in np.nditer(a):
    print(x, end=' ')
print('\n')

# example2
a = np.arange(6).reshape(2, 3)
print(a)
for x in np.nditer(a.T):    # a.T has same memory order as a
    print(x, end=' ')
print('\n')
for x in np.nditer(a.T.copy(order='C')):    # a.T.copy has different memory order from a
    print(x, end=' ')
print('\n')

# example3
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print(a)
for x in np.nditer(a):
    print(x, end=' ')
print('\n')
b = a.T
print(b)
for x in np.nditer(b):
    print(x, end=' ')
print('\n')
c = b.copy(order='C')
print(c)
for x in np.nditer(c):
    print(x, end=' ')
print('\n')
f = b.copy(order='F')
print(f)
for x in np.nditer(f):
    print(x, end=' ')
print('\n')

# example4
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print(a)
for x in np.nditer(a, order='C'):
    print(x, end=' ')
print('\n')
for x in np.nditer(a, order='F'):
    print(x, end=' ')
print('\n')

# example5
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print(a)
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2 * x
print(a)

# example6
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print(a)
for x in np.nditer(a, flags=['external_loop'], order='F'):
    print(x, end=' ')
print('\n')

# example7
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print(a)
b = np.array([1, 2, 3, 4], dtype=int)
print(b)
for x, y in np.nditer([a, b]):
    print("%d:%d" % (x, y), end=' ')
print('\n')
