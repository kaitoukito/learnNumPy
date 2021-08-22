import numpy as np

# example1
a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
print(a)
print(np.amin(a))
print(np.amin(a, axis=0))
print(np.amin(a, axis=1))
print(np.amax(a))
print(np.amax(a, axis=0))
print(np.amax(a, axis=1))
print('\n')

# example2
a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
print(a)
print(np.ptp(a))
print(np.ptp(a, axis=0))
print(np.ptp(a, axis=1))
print('\n')

# example3
a = np.array([[10, 7, 4], [3, 2, 1]])
print(a)
print(np.percentile(a, 50))
print(np.percentile(a, 50, axis=0))
print(np.percentile(a, 50, axis=1))
print(np.percentile(a, 50, axis=1, keepdims=True))
print('\n')

# example4
a = np.array([[30, 65, 70], [80, 95, 10], [50, 90, 60]])
print(a)
print(np.median(a))
print(np.median(a, axis=0))
print(np.median(a, axis=1))

# example5
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a)
print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))

# example6
a = np.array([1, 2, 3, 4])
print(a)
print(np.average(a))
wts = np.array([4, 3, 2, 1])
print(np.average(a, weights=wts))
print(np.average([1, 2, 3, 4], weights=[4, 3, 2, 1], returned=True))    # return sum of wights

# example7
a = np.arange(6).reshape(3, 2)
print(a)
wt = np.array([3, 5])
print(np.average(a, axis=1, weights=wt))
print(np.average(a, axis=1, weights=wt, returned=True))

# example8
print(np.std([1, 2, 3, 4]))

# example9
print(np.var([1, 2, 3, 4]))
