import numpy as np
from matplotlib import pyplot as plt

# example1
x = np.arange(1, 11)
y = 2 * x + 5
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.figure(1)
plt.plot(x, y)

# example2
x = np.arange(1, 11)
y = 2 * x + 5
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.figure(2)
plt.plot(x, y, "ob")

# example3
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
plt.title("sine wave form")
plt.figure(3)
plt.plot(x, y)

# example4
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.figure(4)
plt.subplot(2,  1,  1)
plt.plot(x, y_sin)
plt.title('Sine')
plt.subplot(2,  1,  2)
plt.plot(x, y_cos)
plt.title('Cosine')

# example5
x = [5, 8, 10]
y = [12, 16, 6]
x2 = [6, 9, 11]
y2 = [6, 15, 7]
plt.title('Bar graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.figure(5)
plt.bar(x, y, align='center')
plt.bar(x2, y2, color='g', align='center')

# example6
a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
hist, bins = np.histogram(a, bins=[0, 20, 40, 60, 80, 100])
print(hist)
print(bins)

# example7
a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
plt.figure(6)
plt.hist(a, bins=[0, 20, 40, 60, 80, 100])
plt.title("histogram")

plt.show()
