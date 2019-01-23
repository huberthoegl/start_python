
# last update: 2016-04-12 (removed numerix)

import pylab as p
from matplotlib.mlab import normpdf

x = p.arange(-4, 4, 0.01)
y = normpdf(x, 0, 1) # unit normal
p.plot(x, y, color='red', lw=2)
p.show()

