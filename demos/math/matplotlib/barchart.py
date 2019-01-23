
import pylab as p
import numpy as np

x = np.array([10, 20, 30, 40, 50])
y = np.array([100, 110, 80, 60, 105])

p.bar(x, y)
p.show()

# p.savefig('barchart.png', format='png')
