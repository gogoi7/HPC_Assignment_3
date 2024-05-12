#plot relative error of Bessel function of the first kind of order 0
#using Trapezoid and Simpson's rule compared to scipy.special.j0
#for N=10*2**n, n=0, 1, 2, ..., 8

import numpy as np
from Bessel import BesselCalculator

N = [10*2**n for n in range(9)]
x = 3.83171
bc = BesselCalculator(N[-1])
bessel_scipy = bc.bessel_scipy(x)
results = np.zeros((len(N), 3))
for i, n in enumerate(N):
    bc = BesselCalculator(n)
    bessel_trapezoid = bc.bessel_trapezoid(x)
    bessel_simpson = bc.bessel_simpson(x)
    results[i] = [n, np.abs(bessel_trapezoid - bessel_scipy)/np.abs(bessel_scipy), \
                   np.abs(bessel_simpson - bessel_scipy)/np.abs(bessel_scipy)]  

#save the errors into a file and make a new script file to plot the errors
np.savetxt('Bessel_err.txt', results, fmt='%.18e')