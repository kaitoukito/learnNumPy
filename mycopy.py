import numpy as np

# example1: no copy
a = np.arange(6)
print(a)
print(id(a))
b = a
print(b)
print(b is a)
print(id(b))
b.shape = 3, 2
print(b)
print(a)
print('\n')

# example2: shallow copy
a = np.arange(6).reshape(3, 2)
print(a)
b = a.view()
print(b)
print(b is a)
print(id(a))
print(id(b))
b.shape = 2, 3
print(b)
print(a)
print('\n')

# example3: slice is shallow copy
arr = np.arange(12)
print(arr)
a = arr[3:]
b = arr[3:]
a[1] = 123
b[2] = 234
print(arr)
print(b is a)
print(id(a), id(b), id(arr[3:]))
print('\n')

# example4: deep copy
a = np.array([[10, 10], [2, 3], [4, 5]])
print(a)
b = a.copy()
print(b)
print(b is a)
b[0, 0] = 100
print(b)
print(a)
