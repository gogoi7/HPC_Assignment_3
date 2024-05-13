import Bessel_cython
import numpy as np

x = np.linspace(0, 10, 50)
N = 1000
results = np.zeros((len(x), 4))

for i, val in enumerate(x):
    tr, sr, ex = Bessel_cython.cos_integral(val, N)
    results[i] = [val, tr, sr, ex]

print('x\t\tTrapezoid\tSimpson\t\tScipy')
for result in results:
    i, bessel_trapezoid, bessel_simpson, bessel_scipy = result
    print('{:.6f}\t{:.6f}\t{:.6f}\t{:.6f}'.format(i, bessel_trapezoid, bessel_simpson, bessel_scipy))

if np.allclose(results[:, 1], results[:, 2]) and np.allclose(results[:, 1], results[:, 3]):
    print('All values are close.')
elif np.allclose(results[:, 1], results[:, 3]):
    print('Trapezoid and Scipy values are close.')
elif np.allclose(results[:, 2], results[:, 3]):
    print('Simpson and Scipy values are close.')
else:
    print('None of the values are close.')