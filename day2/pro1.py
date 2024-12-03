from numpy import *
from matplotlib.pyplot import *
from math import *


a = array([1, 2, 3, 4])
b = array([2, 3, 4, 5])
print(a + b)


x = linspace(0.0, 10.0, 200)
x *= 2 * pi / 10

y = sin(x)
y = cos(x)

x[0] = -1
print(x[0], x[-1])
