import numpy as np

# example1
x = np.array([[1,  2],  [3,  4],  [5,  6]])
print(x)
y = x[[0, 1, 2], [0, 1, 0]]
print(y)

# example2
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
rows = np.array([[0, 1], [2, 3]])
cols = np.array([[0, 1], [1, 2]])
y = x[rows]
print(y)
z = x[rows, cols]
print(z)

# example3
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
b = a[1:3, 1:3]
c = a[1:3, [1, 2]]
d = a[..., 1:]
print(b)
print(c)
print(d)

# example4
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
print(x[x > 5])

# example5
a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print(a)
print(a[~np.isnan(a)])

# example6
a = np.array([1, 2+6j, 5, 3.5+5j])
print(a)
print(a[np.iscomplex(a)])

# example7
x = np.arange(32).reshape((8, 4))
print(x)
print(x[[4, 2, 1, 7]])

# example8
x = np.arange(32).reshape((8, 4))
print(x)
print(x[[-4, -2, -1, -7]])

# example9
x = np.arange(32).reshape((8, 4))
print(x)
print(x[[1, 5, 7, 2]])
print(x[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])
