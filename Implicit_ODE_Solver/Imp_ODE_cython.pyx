import numpy as np
cimport numpy as np

def backeuler(double y0, double ti, double tf, int n):
    cdef double dt = (tf - ti) / (2**n)
    cdef int N = int(2**n)
    t_values = [ti]
    y_values = [y0]
    cdef double t = ti
    cdef double y = y0
    cdef int i
    for i in range(1,N+1):
        y = y / (1 + dt)
        t = t + dt
        t_values.append(t)
        y_values.append(y)
    return t_values, y_values