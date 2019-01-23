# simple_numpy.py
# H. Hoegl, November 2012, 2017

from __future__ import print_function
from __future__ import division

'''
Einfache Array und Matrizen Operationen

Literatur 

   Die wichtigsten Array und Matrix Operationen:
   https://docs.scipy.org/doc/numpy-dev/user/quickstart.html

      Dieser Text verweist auf 
      https://docs.scipy.org/doc/numpy/reference/routines.html

   Vergleich mit Matlab:
   https://docs.scipy.org/doc/numpy-dev/user/numpy-for-matlab-users.html

   Vergleich mit IDL:
   http://mathesaurus.sourceforge.net/idl-numpy.html
'''

import numpy as np
import matplotlib.pyplot as plt

print("% --- Arrays ---")

# array is an alias for ndarray
a = np.array([[1, 2], [3, 4]])
print("% a\n", a)
print()

b = np.array([[4, 1], [2, 5]])
print("% b =\n", b)
print()

print("% a*b\n", a*b)   # elementweise Multiplikation
print()

print("% dot(a,b)", np.dot(a,b))  # Arrays muss man mit dot() multiplizieren
print()
                                  # Matrizen kann man mit * multiplizieren

b = np.ones(10)
print("% ones(10)\n", b)
print()

# += and *= work in place 
print("id(b)", id(b))
b += 1
print("b += 1")
print(b)
print("id(b)", id(b))
print()

print("b = b + 1")
b = b + 1
print(b)
print("id(b)", id(b))
print()

print("% outer(b,b)\n", np.outer(b,b))
print()

# arange returns an array object
c = np.arange(60)
print("% np.arange(60)\n", c)
print()

c.resize(3, 4, 5)
print("% c.resize(3, 4, 5)\n", c)
print()

print("c.shape\n", c.shape)
print()

print("c[2][0][4] =", c[2][0][4])
# bei c[2][0][5]: IndexError: index out of bounds

c.resize(2, 10, 3)
print("% c.resize(2, 10, 3)\n", c)
print()

c.resize(2, 2, 20)
print("% c.resize(2, 2, 20)\n", c)
print(c)
print()


print("% --- Matrizen ---")

A = np.matrix([[1, 2], [3, 4]])
print("% A\n", A)
print()

B = np.array([[4, 1], [2, 5]])
print("% B\n", B)
print()

print("% B.shape = ", B.shape)
print()

P = A*B
print("% P = A*B\n", P)
print()

print("% P transponiert\n", P.T)
print()

print("% P invers\n", P.I)
print()


K = np.matrix([[0.5, -1], [-0.25, -1]])
B = np.matrix([-1, -5])

# http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.solve.html
print("np.linalg.solve()")
P = np.linalg.solve(K, B.T)
# check
print("P = \n")
print(P)
print("check")
print((np.dot(K, P) == B.T).all())

x = np.linspace(-2, 12, 1000)
y1 = 0.5 * x + 1
y2 = -0.25 * x + 5
plt.grid()
plt.plot(x, y1, 'r')
plt.plot(x, y2, 'g')
plt.plot(P[0], P[1], 'bo')
plt.show()
