import math


class Oscillation:
    # x(t) = a0 * e ** (-b * t) * sin(w * t + alpha)
    def __init__(self, a0: float, damping_fact: float, freq: float, angle: float = 0):
        self.a0 = a0  # initial amplitude
        self.damping_fact = damping_fact  # beta, rad/sec
        self.freq = freq  # w, rad/sec
        self.angle = angle

    def x(self, t: float) -> float:
        return self.a(t) * math.sin(self.freq * t + self.angle)

    def a(self, t: float) -> float:
        return self.a0 * math.exp(- self.damping_fact * t)

    @property
    def period(self) -> float:
        return 2 * math.pi / self.freq

    @property
    def relax_time(self) -> float:
        return 1 / self.damping_fact

    @property
    def damping_decr(self) -> float:
        return math.exp(self.damping_fact * self.period)

    @property
    def logarithm_decr(self) -> float:
        return self.damping_fact * self.period

    @property
    def quality(self) -> float:
        return math.pi / self.logarithm_decr

    def __str__(self):
        s1 = 'Initial params: A0: {0}, Damping factor: {1}, Period: {2}, Angle: {3}\n'.format(self.a0,
                                                                                              self.damping_fact,
                                                                                              self.period, self.angle)
        s2 = 'Calculated params: Frequency: {0}, Relaxation time: {1}, Damping decrement: {2}, Logarithm decrement: {3}, Quality: {4}'.format(
            self.freq, self.relax_time, self.damping_decr, self.logarithm_decr, self.quality)
        return s1 + s2


class MechanicOscillation(Oscillation):
    def __init__(self, x0: float, m: float, k: float, r: float = 1, angle: float = 0):
        super().__init__(x0, r / (2 * m), math.sqrt(k / m), angle)


class ElectricOscillation(Oscillation):
    def __init__(self, q0: float, capacitance: float, inductance: float, resistance: float = 1, angle: float = 0):
        super().__init__(q0, resistance / (2 * inductance), 1 / math.sqrt(capacitance * inductance), angle)
