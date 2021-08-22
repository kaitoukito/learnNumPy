import numpy as np

# example1
a, b = 13, 17
print(bin(a), bin(b))
print(bin(np.bitwise_and(13, 17)))

# example2
a, b = 13, 17
print(bin(a), bin(b))
print(bin(np.bitwise_or(13, 17)))

# example3
print(np.invert(np.array([13], dtype=np.uint8)))
print(np.binary_repr(13, width=8))  # binary representation
print(np.binary_repr(242, width=8))

# example4
print(np.left_shift(10, 2))
print(np.binary_repr(10, width=8))
print(np.binary_repr(40, width=8))

# example5
print(np.right_shift(40, 2))
print(np.binary_repr(40, width=8))
print(np.binary_repr(10, width=8))

print(np.right_shift(-40, 2))   # arithmetic right shift
print(np.binary_repr(-40, width=8))
print(np.binary_repr(-10, width=8))
