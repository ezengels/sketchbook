import numpy as np
from imageio import imwrite

m = 480
n = 320

Z = np.zeros((n, m), dtype=complex)
M =np.full((n,m), True, dtype=bool)

x = np.linspace(-2, 1, num=m).reshape((1, m))
y = np.linspace(-2, 1, num=n).reshape((n, 1))
C = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))

for i in range(100):
    Z[M] = Z[M] * Z[M] + C[M]
    M[np.abs(Z) > 2] = False

imwrite('mandelbrot.png', np.uint8(np.flipud(1 - M) * 255))