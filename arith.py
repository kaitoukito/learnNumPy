import numpy as np

# example1
a = np.arange(9, dtype=np.float_).reshape(3, 3)
print(a)
b = np.array([10, 10, 10])
print(b)
print(np.add(a, b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.divide(a, b))

# example2
a = np.array([0.25,  1.33,  1,  100])
print(a)
print(np.reciprocal(a))

# example3
a = np.array([10, 100, 1000])
print(a)
print(np.power(a, 2))
b = np.array([1, 2, 3])
print(b)
print(np.power(a, b))

# example4
a = np.array([10, 20, 30])
b = np.array([3, 5, 7])
print(a)
print(b)
print(np.mod(a, b))
print(np.remainder(a, b))
