import numpy as np

# example1
print(np.char.add(['hello'], [' xyz']))
print(np.char.add(['hello', 'hi'], [' abc', ' xyz']))

# example2
print(np.char.multiply('Runoob ', 3))

# example3
print(np.char.center('Runoob', 20, fillchar='*'))


# example4
print(np.char.capitalize('runoob'))

# example5
print(np.char.title('i like runoob'))

# example6
print(np.char.lower(['RUNOOB', 'GOOGLE']))
print(np.char.lower('RUNOOB'))

# example7
print(np.char.upper(['runoob', 'google']))
print(np.char.upper('runoob'))

# example8
print(np.char.split('i like runoob?'))
print(np.char.split('www.runoob.com', sep='.'))

# example9
print(np.char.splitlines('i\nlike runoob?'))
print(np.char.splitlines('i\rlike runoob?'))

# example10
print(np.char.strip('ashok arunooba', 'a'))
print(np.char.strip(['arunooba', 'admin', 'java'], 'a'))

# example11
print(np.char.join(':', 'runoob'))
print(np.char.join([':', '-'], ['runoob', 'google']))

# example12
print(np.char.replace('i like runoob', 'oo', 'cc'))

# example13
a = np.char.encode('runoob')    # utf-8
print(a)
a = np.char.encode('runoob', 'cp500')
print(a)

# example14
a = np.char.encode('runoob', 'cp500')
print(a)
print(np.char.decode(a, 'cp500'))
