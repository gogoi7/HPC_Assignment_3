from Imp_ODE_cython import backeuler
import numpy as np

y0 = 1
ti, tf = 0, 16.00001
n = np.arange(0, 10)
dt_values = 16 / 2 ** n

# Lists to store data
error_data = []

for i, dt in enumerate(dt_values):
    t_values, y_values = backeuler(y0, ti, tf, n[i])
    y_analytic = [np.exp(-t) for t in t_values]
    t_values, y_values, y_analytic = np.array(t_values), np.array(y_values), np.array(y_analytic)
    error = np.abs(y_values - y_analytic) / y_analytic
    error_data.append((t_values[1:], error[1:], f"dt = 16/2^{n[i]}"))

# Save data to a file
with open("error_cython.txt", "w") as file:
    for t, error, label in error_data:
        for time, err in zip(t, error):
            file.write(f"{time},{err},{label}\n")
