#simple code to plot and show plotted points on a graph
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 2*(np.pi),0.1)
y = np.cos(x)
plt.plot(x,y)
plt.show()
