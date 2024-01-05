import numpy as np

m = 480
n = 320

x = np.linespace(-2, 1, num=m).reshape((1, m))
y = np.linespace(-2, 1, num=n).reshape((n, 1))
C = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))