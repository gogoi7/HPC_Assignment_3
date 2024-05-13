import numpy as np
from numba import jit

@jit(nopython=True, parallel=True)
def inverse_transform_sampling(n, gamma):
    """Generate samples from the Lorentzian distribution using inverse transform sampling."""
    u = np.random.rand(n)
    x = gamma * np.tan(np.pi * (u - 0.5))
    return x