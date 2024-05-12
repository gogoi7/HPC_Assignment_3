import numpy as np
from seriesconv_cython import HarmonicSeries

# Create an instance of HarmonicSeries
harmonic_series = HarmonicSeries()

# Define the range of N values
N_range = [2 ** n for n in range(9)]  # N = {1, 2, 4, 8, ..., 256}

# Create empty lists to store values
ascending_sums = []
descending_sums = []

for N in N_range:
    ascending_sums.append(harmonic_series.ascending_sum(N))
    descending_sums.append(harmonic_series.descending_sum(N))
asc_err = np.abs(ascending_sums - np.log(2))
des_err = np.abs(descending_sums - np.log(2))

#save the errors to a single file for comparison
np.savetxt("errors_cython.txt", np.column_stack((N_range, asc_err, des_err)), fmt='%d %.16f %.16f', header='N Ascending_Errors Descending_Errors')
