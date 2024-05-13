from Invtrans_cython import its_hist
from time import time

start = time() # Start timer
logn = 8 # Number of samples
n = 10**logn # Number of samples
its_hist(n) # Generate samples and create histogram
end = time() # End timer
print(f"Histogram written to file hitogram_cython.txt\nTime: {end - start:.3f} s")