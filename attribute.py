import numpy as np

# example1
a = np.arange(24)
print(a)
print(a.ndim)
b = a.reshape(2, 4, 3)
print(b)
print(b.ndim)

# example2
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)

# example3
a = np.array([[1, 2, 3], [4, 5, 6]])
a.shape = (3, 2)
print(a)

# example4
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.reshape(3, 2)
print(b)

# example5
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(x.itemsize)
y = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print(y.itemsize)

# example6
x = np.array([1, 2, 3, 4, 5, 6])
print(x.flags)
y = x.reshape(2, 3)
print(y.flags)
