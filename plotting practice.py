import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-7,7)
f = x**2
g = x**3

plt.plot(x,g)
plt.plot(x,f)

plt.show()
