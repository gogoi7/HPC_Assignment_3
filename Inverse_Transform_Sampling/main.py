import sys
import numpy as np
from Invtrans import inverse_transform_sampling

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python main.py <n> <output_file>")
    sys.exit(1)
    
# Parameters
n = int(sys.argv[1])
output_file = sys.argv[2]
gamma = 1.0

# Generate samples 
samples = inverse_transform_sampling(n, gamma)

# Create a histogram of the sampled values and save the counts to a file
bin_edges = np.linspace(-10.1, 10.1, 102)
hist, _ = np.histogram(samples, bins=bin_edges, density=True)

# Save the histogram to the specified output file
np.savetxt(output_file, np.column_stack((bin_edges[:-1], hist)), header='bin_edges, counts', fmt='%f')
