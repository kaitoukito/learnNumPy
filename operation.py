import numpy as np

# example1
a = np.arange(8)
print(a)
b = a.reshape(4, 2)
print(b)

# example2
a = np.arange(9).reshape(3, 3)
for row in a:
    print(row)
for element in a.flat:  # a.flat is an iterator
    print(element)

# example3
a = np.arange(8).reshape(2, 4)
print(a)
b1 = a.flatten()
print(b1)   # copy of a
# print(a.flatten(order='F'))
b1[0] = 99
print(a)

# example4
a = np.arange(8).reshape(2, 4)
print(a)
c1 = a.ravel()
print(c1)   # view of a
# print(a.ravel(order='F'))
c1[0] = 99
print(a)

# example5
a = np.arange(12).reshape(3, 4)
print(a)
print(np.transpose(a))

# example6
a = np.arange(12).reshape(3, 4)
print(a)
print(a.T)
print('\n')

# example7
a = np.arange(27).reshape(3, 3, 3)  # axis: (x0, x1, x2)
print(a)
# print(np.where(a == 6))
print(a[0, 1, 2])
print('\n')

b = np.rollaxis(a, 2, 0)            # axis: (x2, x0, x1), put x2 before x0
print(b)
# print(np.where(b == 6))
print(b[2, 0, 1])
print('\n')

c = np.rollaxis(a, 2, 1)            # axis: (x0, x2, x1), put x2 before x1
print(c)
# print(np.where(c == 6))
print(c[0, 2, 1])
print('\n')

# example7
a = np.arange(27).reshape(3, 3, 3)
print(a)
d = np.swapaxes(a, 2, 0)            # axis: (x2, x1, x0)
print(d)
print(d[2, 1, 0])
print('\n')

# example8
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])
print(x)
print(y)
b = np.broadcast(x, y)  # b is an iterator
for r, c in b:
    print(r, c)
print(b.shape)
b = np.broadcast(x, y)
c = np.empty(b.shape)
c.flat = [u + v for u, v in b]
print(c)
print(x + y)

# example9
a = np.arange(4).reshape(1, 4)
print(a)
print(np.broadcast_to(a, (4, 4)))

# example10
x = np.array(([1, 2], [3, 4]))  # 2 x 2
print(x)

y = np.expand_dims(x, axis=0)   # 1 x 2 x 2
print(y)
print(x.ndim, y.ndim)
print(x.shape, y.shape)

y = np.expand_dims(x, axis=1)   # 2 x 1 x 2
print(y)
print(x.ndim, y.ndim)
print(x.shape, y.shape)

# example11
x = np.arange(9).reshape(1, 3, 3)
print(x)
y = np.squeeze(x)
print(y)
print(x.shape, y.shape)
print('\n')

# example12
a = np.array([[1, 2], [3, 4]])
print(a)
b = np.array([[5, 6], [7, 8]])
print(b)
print(np.concatenate((a, b)))
print(np.concatenate((a, b), axis=1))
print('\n')

# example13
a = np.array([[1, 2], [3, 4]])
print(a)
b = np.array([[5, 6], [7, 8]])
print(b)
print(np.stack((a, b), 0))
print(np.stack((a, b), 1))
print(np.stack((a, b), 2))
print('\n')

# example14
a = np.array([[1, 2], [3, 4]])
print(a)
b = np.array([[5, 6], [7, 8]])
print(b)
c = np.hstack((a, b))
print(c)
print('\n')

# example15
a = np.array([[1, 2], [3, 4]])
print(a)
b = np.array([[5, 6], [7, 8]])
print(b)
c = np.vstack((a, b))
print(c)
print('\n')

# example16
a = np.arange(9)
print(a)
b = np.split(a, 3)
print(b)
b = np.split(a, [4, 7])
print(b)
print('\n')

# example17
a = np.arange(16).reshape(4, 4)
print(a)
b = np.split(a, 2)
print(b)
c = np.split(a, 2, axis=1)
print(c)
d = np.hsplit(a, 2)
print(d)

# example18
harr = np.floor(10 * np.random.random((2, 6)))
print(harr)
print(np.hsplit(harr, 3))

# example19
a = np.arange(16).reshape(4, 4)
print(a)
b = np.vsplit(a, 2)
print(b)

# example20
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a.shape)
b = np.resize(a, (3, 2))
print(b)
print(b.shape)
b = np.resize(a, (3, 3))
print(b)

# example21
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(np.append(a, [7, 8, 9]))
print(np.append(a, [[7, 8, 9]], axis=0))
print(np.append(a, [[5, 5, 5], [7, 8, 9]], axis=1))
print('\n')

# example22
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)
print(np.insert(a, 3, [11, 12]))
print(np.insert(a, 1, [11], axis=0))
print(np.insert(a, 1, 11, axis=1))

# example23
a = np.arange(12).reshape(3, 4)
print(a)
print(np.delete(a, 5))
print(np.delete(a, 1, axis=1))
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(a)
print(np.delete(a, np.s_[::2]))
print('\n')

# example24
a = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])
print(a)
u = np.unique(a)
print(u)
print('\n')

u, indices = np.unique(a, return_index=True)    # return indices of u in a
print(a)
print(u)
print(indices)
print('\n')

u, indices = np.unique(a, return_inverse=True)  # return indices of a in u
print(a)
print(u)
print(indices)
print(u[indices])   # u[indices of a in u] = a
print('\n')

u, counts = np.unique(a, return_counts=True)
print(a)
print(u)
print(counts)
print('\n')
