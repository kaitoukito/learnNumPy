import numpy as np

# example1: [[1*11+2*13, 1*12+2*14],[3*11+4*13, 3*12+4*14]]
a = np.array([[1, 2], [3, 4]])
b = np.array([[11, 12], [13, 14]])
print(a)
print(b)
print(np.dot(a, b))
print('\n')

# example2: 1*11 + 2*12 + 3*13 + 4*14
a = np.array([[1, 2], [3, 4]])
b = np.array([[11, 12], [13, 14]])
print(a)
print(b)
print(np.vdot(a, b))
print('\n')

# example3: 1*0+2*1+3*0
a = np.array([1, 2, 3])
b = np.array([0, 1, 0])
print(np.inner(a, b))
print('\n')

# example4
# 1*11+2*12, 1*13+2*14
# 3*11+4*12, 3*13+4*14
a = np.array([[1, 2], [3, 4]])
b = np.array([[11, 12], [13, 14]])
print(a)
print(b)
print(np.inner(a, b))
print('\n')

# example5
a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]
print(a)
print(b)
print(np.matmul(a, b))
print('\n')

# example6: add 1s for b
a = [[1, 0], [0, 1]]
b = [1, 2]
print(a)
print(b)
print(np.matmul(a, b))
print(np.matmul(b, a))
print('\n')

# example7: broadcast b
a = np.arange(8).reshape(2, 2, 2)
b = np.arange(4).reshape(2, 2)
print(a)
print(b)
print(np.matmul(a, b))
print('\n')

# example8
a = np.array([[1, 2], [3, 4]])
print(np.linalg.det(a))

# example9
b = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
print(b)
print(np.linalg.det(b))
print(6*(-2*7 - 5*8) - 1*(4*7 - 5*2) + 1*(4*8 - -2*2))

# example10
x = np.array([[1, 2], [3, 4]])
y = np.linalg.inv(x)
print(x)
print(y)
print(np.dot(x, y))

# example11
a = np.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]])
print(a)
ainv = np.linalg.inv(a)
print(ainv)
b = np.array([[6], [-4], [27]])
print(b)
x = np.linalg.solve(a, b)
print(x)
x = np.dot(ainv, b)
print(x)
