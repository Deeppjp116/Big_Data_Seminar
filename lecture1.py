from numpy import *
from matplotlib.pyplot import *
from math import *


p = [1, 2, 3, 5, 6]

b = [11, 13, 17]

c = p + b
# print(c)


L = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

t = [1.80, 2.10, 2.40, 2.70, 3.00, 3.30, 3.60]
s = "Dep"
print(len(L), len(s))


#  Doing for loop on list


tsq = []
for time in t:
    tsq.append(time * time)

plot(L, tsq)

show()