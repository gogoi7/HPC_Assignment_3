import numpy as np

class LogisticMap:
    def __init__(self, r):
        self.r = r
        
    def iterate(self, x):
        return self.r*x*(1-x)
    

rs = np.linspace(1, 4, 1000)
n = 1000
x0 = 0.5
xn = np.zeros((n, len(rs)))

for i, r in enumerate(rs):
    lmap = LogisticMap(r)
    x = x0
    for j in range(n):
        x = lmap.iterate(x)
        xn[j, i] = x

xn = xn[500:, :]

#save r and x values
np.save('r.npy', rs)
np.save('x.npy', xn)            