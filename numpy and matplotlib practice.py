import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-white')

def f(x, y):
    return np.sin(x) ** 10 + np.cos(5 + y * x) * np.sin(x)

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)
X, Y = np.meshgrid(x, y)

# Make sure the inputs are broadcasted correctly and have the right shape
print("Shape of X:", X.shape)
print("Shape of Y:", Y.shape)

Z = f(X, Y)

# Check shape of Z as well
print("Shape of Z:", Z.shape)

plt.contourf(X, Y, Z, 20, cmap='RdBu')
plt.colorbar()
plt.show()
