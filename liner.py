import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1.3, 4.4, 0.1)
y = 1.35 * (x - 3.8) * (x - 1.2) * (x + 0.8)
z = 1.0996 * x + 0.3456 + (1.35 * (x - 3.8) * (x - 1.2) * (x + 0.8)) / 1000

plt.figure()
#plt.plot(x, y)
plt.plot(x, z)
plt.show()
