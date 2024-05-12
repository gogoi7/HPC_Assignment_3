class NumericalIntegration:
    def __init__(self, function, a, b, n):
        self.function = function
        self.a = a
        self.b = b
        self.n = n

    def integrate(self):
        pass

class TrapezoidRule(NumericalIntegration):
    def integrate(self):
        h = (self.b - self.a) / self.n
        result = 0.5 * (self.function(self.a) + self.function(self.b))
        for i in range(1, self.n):
            x = self.a + i * h
            result += self.function(x)
        return h * result

class SimpsonsRule(NumericalIntegration):
    def integrate(self):
        h = (self.b - self.a) / self.n
        result = self.function(self.a) + self.function(self.b)
        for i in range(1, self.n):
            x = self.a + i * h
            if i % 2 == 0:
                result += 2 * self.function(x)
            else:
                result += 4 * self.function(x)
        return h / 3 * result