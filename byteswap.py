import numpy as np

# example1
a = np.array([1, 256, 8755], dtype=np.int16)
print(a)
print(map(hex, a))
print(a.byteswap(True))
print(map(hex, a))
