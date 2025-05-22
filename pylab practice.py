from pylab import*
import numpy as np
def f(x,y):
 return np.sin(x**2+y**2)
x=np.linspace(0,10)
y=np.linspace(0,10)
X,Y=np.meshgrid(x,y)
Z=f(X,Y)
ax=axes(projection='3d')
ax.plot_surface(X,Y,Z)
xlabel('x-axis')
ylabel("y-axis")