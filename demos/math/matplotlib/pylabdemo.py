import pylab as p

x = p.arange(0, 10, 0.1)
y = p.sin(x)
p.plot(x, y)
p.show()

# p.savefig('pylabdemo.png', format='png')
