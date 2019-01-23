import matplotlib.pyplot as plot
import math

xs = [0.01*x for x in range(1000)]
ys = [math.sin(x) for x in xs]
zs = [math.cos(x) for x in xs]

plot.axis('equal')
plot.xlabel('$x$')
plot.ylabel('$y$')
plot.title(r'The curves $\sin x$ and $\cos x$')
plot.plot(xs, ys, label=r'$\sin$', color='red')
plot.plot(xs, zs, ':', label=r'$\cos$')
plot.legend(loc='upper right')

plot.savefig("sincos.png")

