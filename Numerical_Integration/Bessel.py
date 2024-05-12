import numpy as np
from NumInt import TrapezoidRule, SimpsonsRule
from scipy.special import j0

class BesselCalculator:
    def __init__(self, N):
        self.N = N

    def bessel_trapezoid(self, x):
        tr = TrapezoidRule(lambda theta: np.cos(x*np.sin(theta)), 0, np.pi, self.N)
        result = tr.integrate()/np.pi
        return result

    def bessel_simpson(self, x):
        sr = SimpsonsRule(lambda theta: np.cos(x*np.sin(theta)), 0, np.pi, self.N)
        result = sr.integrate()/np.pi
        return result
    
    def bessel_scipy(self, x):
        result = j0(x)
        return result

if __name__ == '__main__':
    x = np.linspace(0, 10, 50)
    N = 1000
    results = np.zeros((len(x), 4))
    for i, val in enumerate(x):
        bc = BesselCalculator(N)
        bessel_trapezoid = bc.bessel_trapezoid(val)
        bessel_simpson = bc.bessel_simpson(val)
        bessel_scipy = bc.bessel_scipy(val)
        results[i] = [val, bessel_trapezoid, bessel_simpson, bessel_scipy]

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

