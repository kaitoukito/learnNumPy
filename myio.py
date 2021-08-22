import numpy as np

# example1
a = np.array([1, 2, 3, 4, 5])
np.save('outfile.npy', a)
np.save('outfile2', a)

# example2
b = np.load('outfile.npy')
print(b)

# example3
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.arange(0, 1.0, 0.1)
c = np.sin(b)
print(a)
print(b)
print(c)
np.savez("runoob.npz", a, b, sin_array=c)
r = np.load("runoob.npz")
print(r.files)
print(r["arr_0"])
print(r["arr_1"])
print(r["sin_array"])

# example4
a = np.array([1, 2, 3, 4, 5])
np.savetxt('out.txt', a)
b = np.loadtxt('out.txt')
print(b)

# example5
a = np.arange(0, 10, 0.5).reshape(4, -1)
print(a)
np.savetxt("out.txt", a, fmt="%d", delimiter=",")
b = np.loadtxt("out.txt", delimiter=",")
print(b)
