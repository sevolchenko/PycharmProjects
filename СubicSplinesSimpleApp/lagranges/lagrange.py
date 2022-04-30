class Lagrange:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def point(self, param):
        result = 0
        for i in range(len(self.y)):
            elem = 1
            for j in range(len(self.y)):
                if i != j:
                    elem *= (param - self.x[j]) / (self.x[i] - self.x[j])
            result += self.y[i] * elem
        return result
