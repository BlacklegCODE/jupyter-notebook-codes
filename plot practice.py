from pylab import*
import numpy as np
x = np.linspace(-5,5)
y = np.exp(-x**2)
plt.plot(x,y,'-.^g')
plt.show()
