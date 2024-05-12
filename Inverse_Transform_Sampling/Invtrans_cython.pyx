import numpy as np
cimport numpy as np

def inverse_transform_sampling(int n, double gamma):
    """Generate samples from the Lorentzian distribution using inverse transform sampling."""
    cdef np.ndarray[np.double_t, ndim=1] u = np.random.rand(n)
    cdef np.ndarray[np.double_t, ndim=1] x = gamma * np.tan(np.pi * (u - 0.5))
    return x

def its_hist(int n):
    cdef double gamma = 1.0

    # Generate samples 
    cdef np.ndarray[np.double_t, ndim=1] samples = inverse_transform_sampling(n, gamma)

    # Create a histogram of the sampled values and save the counts to a file
    cdef np.ndarray[np.double_t, ndim=1] bin_edges = np.linspace(-10.1, 10.1, 102)
    cdef np.ndarray[np.double_t, ndim=1] hist = np.histogram(samples, bins=bin_edges, density=True)[0]

    # Save the histogram to the specified output file
    np.savetxt("histogram_cython.txt", np.column_stack((bin_edges[:-1], hist)), header='bin_edges, counts', fmt='%f')
