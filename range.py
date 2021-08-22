import numpy as np

# example1
x = np.arange(5)
print(x)

# example2
x = np.arange(5, dtype=float)
print(x)

# example3
x = np.arange(10, 20, 2)
print(x)

# example4
a = np.linspace(1, 10, 10)
print(a)

# example5
a = np.linspace(1, 1, 10)
print(a)

# example6
a = np.linspace(10, 20, 5)
print(a)
a = np.linspace(10, 20, 5, endpoint=False)
print(a)

# example7
a = np.linspace(1, 10, 10)
print(a)
a = np.linspace(1, 10, 10, retstep=True)
print(a)
b = np.linspace(1, 10, 10).reshape([10, 1])
print(b)

# example8
a = np.logspace(1.0, 2.0, num=10)
print(a)

# example9
a = np.logspace(start=0, stop=9, num=10, base=2)
print(a)
