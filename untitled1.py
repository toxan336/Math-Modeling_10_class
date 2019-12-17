import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t=np.arange(0, 100, 0.01)
def diff_fuction(z, t):
    y,q=z
    dy_dt=q
    dq_dt=-np.sin(y)-k/m*q
    return dy_dt, dq_dt
y_0 = 30
q_0 = 0.05
z0=y_0, q_0

k=0.2
m=5

sol = odeint(diff_fuction, z0,t)
plt.plot(t, sol[:, 0])
plt.legend()
plt.show()