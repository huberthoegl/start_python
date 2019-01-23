# numpy_1.py
# http://www.scipy.org/NumPy_for_Matlab_Users

import numpy as np

# http://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html
a = np.array((1, 2, 3))

# http://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html
b = np.linspace(0, 2, 3)

print("a = n.array((1, 2, 3))")

print(a)

print("b = n.linspace(0, 2, 3)")
 
print(b)

print("a + b")

print(a + b)

# http://docs.scipy.org/doc/numpy/reference/generated/numpy.inner.html 
print("np.inner(a, b)")
print(np.inner(a, b))

# http://docs.scipy.org/doc/numpy/reference/generated/numpy.outer.html
print("c =  np.outer(a, b)")
c =  np.outer(a, b)
print(c)

print("2-dim array d, dtype=\"float\")")

d = np.array([[2.1, 3, 4], [3, 4, 5], [7, 8, 9]], dtype="float")
print(d)

# http://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html
print("np.dot(c, d) -> Matrix Multiplikation bei array")
print(np.dot(c, d))

print("c * d (array -> elemement-weise Multiplikation)")
print(c * d)

print("a = a.astype(\"float\")")
a = a.astype("float")
print(a)

print("a[1] = n.pi")
a[1] = np.pi
print(a)

print("c")
print(c)

print("c.repeat(2, 0)")
c = c.repeat(2, 0)
print(c)

# http://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html
print("np.arange(0.2, 0.9, 0.1)")
r = np.arange(0.2, 0.9, 0.1)
print(r)


