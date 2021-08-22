import numpy as np

# example1
dt = np.dtype(np.int32)
print(dt)

# example2
dt = np.dtype('i4')
print(dt)

# example3
dt = np.dtype('<i4')
print(dt)

# example4
dt = np.dtype([('age', np.int8)])
print(dt)

# example5
dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a)

# example6
dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a['age'])

# example7
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)

# example8
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
print(a)
