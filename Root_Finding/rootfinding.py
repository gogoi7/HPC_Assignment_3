#make a class of root finding methods
#with the following methods:
#1. Newton's method
#2. Halley's method
#3. Method of Successive Approximations

import numpy as np
import matplotlib.pyplot as plt

class RootFinding:
    def __init__(self, f, df, d2f):
        self.f = f
        self.df = df
        self.d2f = d2f

    def newton(self, x0, xmin, xmax, tol, max_iter=50):
        x = x0
        for i in range(max_iter):
            x = x - self.f(x)/self.df(x)
            if np.abs(self.f(x)) < tol:
                break
            if x > xmax:
                x = 2*xmax - x
            elif x < xmin:
                x = 2*xmin - x
        return x
    
    def halley(self, x0, xmin, xmax, tol, max_iter):
        x = x0
        for i in range(max_iter):
            a = self.f(x)/self.df(x)
            b = self.d2f(x)/self.df(x)
            x = x - a/(1 - 0.5*a*b)
            if np.abs(self.f(x)) < tol:
                break
            if x > xmax:
                x = 2*xmax - x
            elif x < xmin:
                x = 2*xmin - x
        return x
    
    def successive_approximations(self, x0, xmin, xmax, tol, max_iter):
        x = x0
        for i in range(max_iter):
            x = self.f(x) + x
            if np.abs(self.f(x)) < tol:
                break
            if x > xmax:
                x = 2*xmax - x
            elif x < xmin:
                x = 2*xmin - x
        return x

if __name__ == '__main__':
    # Define the function and its derivatives
    f = lambda x: np.tan(x) - x
    df = lambda x: 1/np.cos(x)**2 - 1
    d2f = lambda x: 2*np.sin(x)*np.cos(x)/np.cos(x)**4

    # Create an instance of the RootFinding class
    rf = RootFinding(f, df, d2f)

    # Find the roots using Newton's method
    tol = 1e-12
    x0 = np.pi*np.arange(1, 3)+0.1
    max_iter = 1000

    roots_newton = np.zeros(len(x0))
    for i in range(len(x0)):
        j = i + 1
        xmin, xmax = (j-0.5)*np.pi, (j+0.5)*np.pi
        roots_newton[i] = rf.newton(x0[i], xmin, xmax, tol, max_iter)

    # Find the roots using Halley's method
    roots_halley = np.zeros(len(x0))
    for i in range(len(x0)):
        j = i + 1
        xmin, xmax = (j-0.5)*np.pi, (j+0.5)*np.pi
        roots_halley[i] = rf.halley(x0[i], xmin, xmax, tol, max_iter)

    # Find the roots using the method of successive approximations
    roots_succ = np.zeros(len(x0))
    for i in range(len(x0)):
        j = i + 1
        xmin, xmax = (j-0.5)*np.pi, (j+0.5)*np.pi
        roots_succ[i] = rf.successive_approximations(x0[i], xmin, xmax, tol, max_iter)

    # Print the results
    print('Roots using Newtons method:', roots_newton)
    print('Roots using Halleys method:', roots_halley)
    print('Roots using the method of successive approximations:', roots_succ)