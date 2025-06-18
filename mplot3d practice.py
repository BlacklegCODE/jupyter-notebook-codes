import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
def f(x,y):
    return np.exp(-x**2 - y**2)
x = np.linspace(-2,2,100)
y = np.linspace(-2,2,100)
X,Y = np.meshgrid(x,y)
Z = f(X,Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(X,Y,Z,color='blue')
ax.set_title('woreframe plot')
plt.show()
