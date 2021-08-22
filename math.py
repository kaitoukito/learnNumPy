import numpy as np

# example1
a = np.array([0, 30, 45, 60, 90])
print(np.sin(a*np.pi/180))
print(np.cos(a*np.pi/180))
print(np.tan(a*np.pi/180))
print('\n')

# example2
a = np.array([0, 30, 45, 60, 90])
sin = np.sin(a*np.pi/180)
print(sin)
inv = np.arcsin(sin)
print(inv)
print(np.degrees(inv))
cos = np.cos(a*np.pi/180)
print(cos)
inv = np.arccos(cos)
print(inv)
print(np.degrees(inv))
tan = np.tan(a*np.pi/180)
print(tan)
inv = np.arctan(tan)
print(inv)
print(np.degrees(inv))

# example3
a = np.array([1.0, 5.55,  123,  0.567,  25.532])
print(a)
print(np.around(a))
print(np.around(a, decimals=1))
print(np.around(a, decimals=-1))

# example4
a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print(a)
print(np.floor(a))

# example5
a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print(a)
print(np.ceil(a))
