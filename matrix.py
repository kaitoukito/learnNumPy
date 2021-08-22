import numpy as np
import numpy.matlib

# example1
a = np.arange(12).reshape(3, 4)
print(a)
print(a.T)

# example2
print(np.empty((2, 2)))
print(type(np.empty((2, 2))))
print(np.matlib.empty((2, 2)))
print(type(np.matlib.empty((2, 2))))

# example3
print(np.zeros((2, 2)))
print(np.matlib.zeros((2, 2)))

# example4
print(np.ones((2, 2)))
print(np.matlib.ones((2, 2)))

# example5
print(np.eye(2, 2))
print(np.matlib.eye(2, 2))

# example6
print(np.identity(2))
print(np.matlib.identity(2))

# example7
print(np.random.rand(2, 2))
print(np.matlib.rand(2, 2))

# example4
i = np.matrix('1, 2; 3, 4')
print(i)
print(type(i))
j = np.array(i)
print(j)
print(type(j))
k = np.matrix(j)
print(k)
print(type(k))
