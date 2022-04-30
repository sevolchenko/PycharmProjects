class Newton:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def point(self, param):
        result = 0
        elem = 1
        for i in range(len(self.y)):
            result += elem * Newton.__divided_diff(self.x[:(i + 1)], self.y[:(i + 1)])
            elem *= (param - self.x[i])
        return result

    @staticmethod
    def __divided_diff(x, y):
        result = 0
        for j in range(len(y)):
            elem = 1
            for i in range(len(y)):
                if i != j:
                    elem *= x[j] - x[i]  # можно улучшить, но с потерей точности: перемножить все и на нужное делить
            result += (y[j] / elem)
        return result