from numpy import *
from matplotlib.pyplot import *
from math import *

# a = array([[1, 2, 3, 4], [11, 12, 13, 14]])

# print(a.shape)

# a = array([[1, 2, 3, 4], [4, 5, 6, 0], [11, 12, 13, 14]])
# print(a[0, 1:3])

# a= loadtxt(./circulate/lena.png)

# a = array([1, 2, 3], dtype=float)

# ones_like(a)
# array(a)


# a = loadtxt("pendulum.txt")

# a.shape()

# L, t = loadtxt("pendulum.txt")
# plot(L, t * t, ".")

c = [
    1,
    2,
    3,
    3,
    44,
]

print(c)

# c[:, 1]


a = imread("/media/deep/D18/anadonda/conda_practice/circulate/lena.png")

# imshow(a)
# a.shape

b = a[:256, :256]

b = a[200:400, 200:400]


print(b.shape)
imshow(b)
show()
