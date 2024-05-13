import numpy as np
cimport numpy as np

cdef class LogisticMap:
    cdef double r

    def __init__(self, double r):
        self.r = r
        
    def iterate(self, double x):
        return self.r * x * (1 - x)
    

def logistic_map_cython(int n):
    cdef np.ndarray[np.float64_t, ndim=2] xn
    cdef np.ndarray[np.float64_t] rs = np.linspace(1, 4, 1000)
    cdef int i, j
    cdef double x0 = 0.5

    xn = np.zeros((n, len(rs)), dtype=np.float64)

    for i in range(len(rs)):
        lmap = LogisticMap(rs[i])
        x = x0
        for j in range(n):
            x = lmap.iterate(x)
            xn[j, i] = x

    return rs, xn