import numpy as np

# example1
x = np.empty([3, 2], dtype=int)
print(x)

# example2
x = np.zeros(5)     # the default type is float
print(x)
y = np.zeros((5,), dtype=np.int)
print(y)
z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(z)

# example3
x = np.ones(5)      # the default type is float
print(x)
x = np.ones([2, 2], dtype=int)
print(x)
