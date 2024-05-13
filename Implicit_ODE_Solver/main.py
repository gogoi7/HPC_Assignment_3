import numpy as np

def backeuler(y0, ti, tf, dt):
    t = np.arange(ti, tf, dt)
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(1, len(t)):
        y[i] = y[i - 1] / (1 + dt)
    return t, y

y0 = 1
ti, tf = 0, 16.00001
n = np.arange(0, 10)
dt_values = 16 / 2 ** n

# Lists to store data
error_data = []

for i, dt in enumerate(dt_values):
    t, y = backeuler(y0, ti, tf, dt)
    y_exact = np.exp(-t)
    error = np.abs(y - y_exact) / y_exact
    error_data.append((t[1:], error[1:], f"dt = 16/2^{n[i]}"))

# Save data to a file
with open("error_python.txt", "w") as file:
    for t, error, label in error_data:
        for time, err in zip(t, error):
            file.write(f"{time},{err},{label}\n")

# Now, you can plot the data later using this saved data

# import numpy as np
# import matplotlib.pyplot as plt

# def backeuler(y0,ti,tf,dt):
#     t = np.arange(ti,tf,dt)
#     y = np.zeros(len(t))
#     y[0] = y0
#     for i in range(1,len(t)):
#         y[i] = y[i-1]/(1+dt)
#     return t,y

# y0 = 1
# ti,tf = 0,16.00001
# n = np.arange(0,10)
# dt = 16/2**n 

# for i,dt in enumerate(dt):
#     t,y = backeuler(y0,ti,tf,dt)
#     y_exact = np.exp(-t)
#     error = np.abs(y-y_exact)/y_exact
#     plt.plot(t[1:],error[1:],label=f"dt = 16/2$^{n[i]}$", marker="o")

# plt.xlabel("Time")
# plt.ylabel("Relative Error")
# plt.yscale("log")
# plt.legend()
# plt.grid()

# plt.show()




# #Use an initial condition y0 = 1 and solve the ODE over a time 
# #interval (e.g., t = 0 to t = 16) with a fixed time step ∆t

# from decay_ODE import DecayODE
# from ODEsolve import Euler, BackwardEuler
# import numpy as np
# import matplotlib.pyplot as plt

# # Define the parameters of the ODE
# y_0 = 1
# t_0 = 0
# t_f = 16
# n = np.arange(0,10)
# dt = 16/2**n
# alpha = 0.5
# for dt in dt:

#     # Create an instance of the DecayODE class
#     decay = DecayODE(y_0, t_0, t_f, dt, alpha)

#     # Create an instance of the Euler class
#     euler = Euler(decay.f, y_0, t_0, t_f, dt)

#     # Create an instance of the BackwardEuler class
#     backward_euler = BackwardEuler(decay.f, y_0, t_0, t_f, dt)

#     # Solve the ODE using the Euler method
#     y_euler = euler.solve()

#     # Solve the ODE using the backward Euler method
#     y_backward_euler = backward_euler.solve()

#     # Create an array of time values
#     t = np.arange(t_0, t_f, dt)

#     # Create an array of the exact solution
#     y_exact = decay.exact_solution(t)

#     # Plot the numerical and exact solutions
#     plt.plot(t, y_euler, label="Euler")
#     plt.plot(t, y_backward_euler, label="Backward Euler")
#     plt.plot(t, y_exact, label="Exact")
#     plt.xlabel("Time")
#     plt.ylabel("y")
#     plt.legend()
#     plt.title(f"dt = {dt}")
#     plt.show()

#     #plot the error
#     error_euler = np.abs(y_euler - y_exact)
#     error_backward_euler = np.abs(y_backward_euler - y_exact)
#     plt.plot(t, error_euler/y_exact, label="Euler")
#     plt.plot(t, error_backward_euler/y_exact, label="Backward Euler")
#     plt.xlabel("Time")
#     plt.ylabel("Relative Error")
#     plt.legend()

#     plt.title(f"Relative Error dt = {dt}")
#     plt.show()

    




