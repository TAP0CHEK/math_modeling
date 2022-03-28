import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

t=np.arange(-1, 1, 0.01)




def diff_func(v, t):
  y, x = v
  dxdt = 3x - y + z
  dydt = x + y + z
  dzdt =
  return dydt , dxdt



x0 = -71
y0 = 1
z0 = -3


v0 = y0, x0


sol = odeint (diff_func, v0, t)

plt.plot(t, sol[:, 1], 'g')
plt.plot(t, sol[:, 0], 'g')
plt.legend()
plt.show()