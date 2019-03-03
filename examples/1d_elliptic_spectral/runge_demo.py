"""
Demonstration of Runge's phenomenon.
"""
USE_CHEB = True

import matplotlib.pyplot as plt
from scipy.interpolate import barycentric_interpolate
import numpy as np

def runge_fn(x):
    "Runge's function"
    return 1/(1 + 25*x**2)

# fine grid for plotting
x_fine = np.linspace(-1, 1, 1000)

# draw the true function
plt.plot(x_fine, runge_fn(x_fine), '--')

if USE_CHEB:
    ns = (10, 20, 30)
else:
    ns = (6, 10, 12, 16)

for n in ns:

    # interpolation points
    if USE_CHEB:
        zi = np.linspace(0, 1, n)
        xi = -1 + (1 + np.cos(np.pi*(1 - zi)))
    else:
        xi = np.linspace(-1, 1, n)
    yi = runge_fn(xi)

    # interpolate the function
    y_fine = barycentric_interpolate(xi, yi, x_fine)

    plt.plot(x_fine, y_fine, label='n = {}'.format(n))


plt.legend()
plt.show()