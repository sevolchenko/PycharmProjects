from unittest import TestCase
import numpy as np

import main


class TestFunction(TestCase):
    def test_function(self):
        self.assertTrue(np.abs(main.function(2, 2) - 1.666) < 1e-3)

    def test_derivative(self):
        self.assertTrue(np.abs(main.analytical_derivative_x(2, 2) - main.numerical_derivative(2, 2, 1e-3, 0) < 1e-3))
