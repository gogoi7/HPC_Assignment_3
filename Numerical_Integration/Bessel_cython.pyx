# cython_integration.pyx
cimport cython

import numpy as np
cimport numpy as np
from scipy import special

cpdef double f(x, theta):
    return x * np.cos(theta)

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double trapezoid_integration(double x, double a, double b, int N):
    cdef double h = (b - a) / N
    cdef double integral = 0.5 * (np.cos(f(x, a)) + np.cos(f(x, b)))
    cdef int i
    for i in range(1, N):
        integral += np.cos(f(x, a + i * h))
    integral *= h
    return integral/np.pi

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double simpsons_integration(double x, double a, double b, int N):
    cdef double h = (b - a) / N
    cdef double integral = np.cos(f(x, a)) + np.cos(f(x, b))
    cdef int i
    for i in range(1, N, 2):
        integral += 4 * np.cos(f(x, a + i * h))
    for i in range(2, N-1, 2):
        integral += 2 * np.cos(f(x, a + i * h))
    integral *= h / 3
    return integral/np.pi

def J0(x):
    return special.jn(0, x)

cpdef tuple cos_integral(double x, int N):
    cdef double integral_trap = trapezoid_integration(x, 0, np.pi, N)
    cdef double integral_simpson = simpsons_integration(x, 0, np.pi, N)
    cdef double true_value = J0(x)
    return (integral_trap, integral_simpson, true_value)