import unittest
import numpy as np
import main


class MyTestCase(unittest.TestCase):
    def test_input1(self):
        matrix, right_side = main.read_matrix('input1.txt')
        np_solution = np.linalg.solve(matrix, right_side)
        jacobi = main.jacobi_method(matrix, right_side, 5)
        gauss = main.gauss_method(matrix, right_side, 5)
        self.assertTrue(np.allclose(np_solution, jacobi, gauss))

    def test_input2(self):
        matrix, right_side = main.read_matrix('input2.txt')
        np_solution = np.linalg.solve(matrix, right_side)
        jacobi = main.jacobi_method(matrix, right_side, 5)
        gauss = main.gauss_method(matrix, right_side, 5)
        self.assertFalse(np.allclose(np_solution, jacobi, gauss))

    def test_input3(self):
        matrix, right_side = main.read_matrix('input3.txt')
        np_solution = np.linalg.solve(matrix, right_side)
        jacobi = main.jacobi_method(matrix, right_side, 5)
        gauss = main.gauss_method(matrix, right_side, 5)
        self.assertTrue(np.allclose(np_solution, jacobi, gauss))

    def test_input4(self):
        matrix, right_side = main.read_matrix('input4.txt')
        np_solution = np.linalg.solve(matrix, right_side)
        jacobi = main.jacobi_method(matrix, right_side, 5)
        gauss = main.gauss_method(matrix, right_side, 5)
        self.assertTrue(np.allclose(np_solution, jacobi, gauss))

    def test_input5(self):
        matrix, right_side = main.read_matrix('input5.txt')
        np_solution = np.linalg.solve(matrix, right_side)
        jacobi = main.jacobi_method(matrix, right_side, 5)
        gauss = main.gauss_method(matrix, right_side, 5)
        self.assertTrue(np.allclose(np_solution, jacobi, gauss))


if __name__ == '__main__':
    unittest.main()
