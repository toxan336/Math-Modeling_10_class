import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
x=np.arange(0, 10, 0.01)
def fun(z, x):
    e, omega=z
    de_dx= omega
    domega_dx= -np.sin(e) * +omega - 3 * e * x + 5
    return de_dx, domega_dx
e0 = 0.01
omega0 = 0.05
z0=e0, omega0
sol = odeint(fun, z0, x)
plt.plot(x, sol[:, 0], 'b')
plt.plot(x, sol[:, 1], 'g')
plt.plot(sol[:, 0], sol[:, 1], 'k')
plt.legend()
plt.show()