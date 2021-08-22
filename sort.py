import numpy as np

# example1
a = np.array([[3, 7], [9, 1]])
print(a)
print(np.sort(a))
print(np.sort(a, axis=0))

dt = np.dtype([('name', 'S10'), ('age', int)])
a = np.array([("raju", 21), ("anil", 25), ("ravi", 17), ("amar", 27)], dtype=dt)
print(a)
print(np.sort(a, order='name'))
print(np.sort(a, order='age'))

# example2
x = np.array([3, 1, 2])
print(x)
y = np.argsort(x)
print(y)
print(x[y])
for i in y:
    print(x[i], end=" ")
print('\n')

# example3
high_priority = (100, 100, 90, 80)
low_priority = (80, 90, 100, 100)
ind = np.lexsort((low_priority, high_priority))
print(ind)
print([(high_priority[i], low_priority[i]) for i in ind])

# example4
a = np.array([[30, 40, 70], [80, 20, 10], [50, 90, 60]])
print(a)
print(np.argmax(a))
print(a.flatten())
maxindex = np.argmax(a, axis=0)
print(maxindex)
maxindex = np.argmax(a, axis=1)
print(maxindex)
minindex = np.argmin(a)
print(minindex)
print(a.flatten()[minindex])
minindex = np.argmin(a, axis=0)
print(minindex)
minindex = np.argmin(a, axis=1)
print(minindex)

# example5
a = np.array([[30, 40, 0], [0, 20, 10], [50, 0, 60]])
print(a)
print(np.nonzero(a))

# example6
x = np.arange(9.).reshape(3, 3)
print(x)
y = np.where(x > 3)
print(y)
print(x[y])

# example7
x = np.arange(9.).reshape(3, 3)
print(x)
condition = np.mod(x, 2) == 0
print(condition)
print(np.extract(condition, x))

# example8
a = np.array([3, 4, 2, 1])
print(a)
print(np.partition(a, 3))
print(np.partition(a, (1, 3)))

arr = np.array([46, 57, 23, 39, 1, 10, 0, 120])
print(arr)
print(arr[np.argpartition(arr, 2)[2]])
print(arr[np.argpartition(arr, -2)[-2]])
print(arr[np.argpartition(arr, [2, 3])[2]])
print(arr[np.argpartition(arr, [2, 3])[3]])
