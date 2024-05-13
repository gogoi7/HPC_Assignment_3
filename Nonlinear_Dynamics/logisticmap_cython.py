import numpy as np
from logisticmapcy import logistic_map_cython

#print(logistic_map_cython(1000))
rs, xn = logistic_map_cython(1000)
#print(rs.shape)
#print(xn.shape)
xn = xn[500:, :]
np.save('r_cython.npy', rs)
np.save('x_cython.npy', xn)