import numpy as np

# example1
a = np.arange(10)
print(a)
s = slice(2, 7, 2)
print(s)
print(a[s])

# example2
a = np.arange(10)
b = a[2:7:2]    # start:stop:step
print(b)

# example3
a = np.arange(10)
b = a[5]
print(b)

# example4
a = np.arange(10)
print(a[2:])

# example5
a = np.arange(10)
print(a[2:5])

# example6
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
print(a[1:])

# example7
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a[..., 1])
print(a[:, 1])
print(a[1, ...])
print(a[1, :])
print(a[..., 1:])
print(a[:, 1:])
