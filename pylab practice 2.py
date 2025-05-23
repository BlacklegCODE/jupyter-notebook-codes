from pylab import*
import numpy as np
from math import*
x=np.linspace(0,5)
y1=np.sin(x)
y2=np.cos(x)
y3=np.exp(x)
y4=x**2
subplot(2,2,1)
plot(x,y1,label="$ sin x $")
legend()
subplot(2,2,2)
plot(x,y2,label="$ cos x $")
legend()
subplot(2,2,3)
plot(x,y3,label="$ e^x $")
legend()
subplot(2,2,4)
plot(x,y4,label="$ x^2 $")
legend()
show()