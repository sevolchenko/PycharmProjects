import numpy as np
import matplotlib.pyplot as plt
import sys


def read_matrix(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    matrix = []
    right_side = []
    for row in lines:
        new_row = [float(j) for j in row.split()]
        matrix.append(new_row[:(len(new_row) - 1)])
        right_side.append(new_row[len(new_row) - 1])
    return matrix, right_side


def jacobi_method(matrix, right_side, iterations_count):
    if not(check_diag_dominance(matrix)):
        sys.stderr.write("There is no diagonal dominance in matrix. Result may be not right.\n")
    b = [[-matrix[row][col] / matrix[row][row] if row != col else 0 for col in range(len(right_side))] for row in
         range(len(right_side))]
    d = [right_side[row] / matrix[row][row] for row in range(len(right_side))]
    curr_x = d.copy()
    for i in range(iterations_count):
        curr_x = [d[row] + sum(b[row][col] * curr_x[col] for col in range(len(d))) for row in range(len(right_side))]
    return curr_x


def gauss_method(matrix, right_side, iterations_count):
    if not(check_diag_dominance(matrix)):
        sys.stderr.write("There is no diagonal dominance in matrix. Result may be not right.\n")
    b = [[-matrix[row][col] / matrix[row][row] if row != col else 0 for col in range(len(right_side))] for row in
         range(len(right_side))]
    d = [right_side[row] / matrix[row][row] for row in range(len(right_side))]
    curr_x = d.copy()
    for i in range(iterations_count):
        for row in range(len(right_side)):
            curr_x[row] = d[row] + sum(b[row][col] * curr_x[col] for col in range(len(d)))
    return curr_x


def check_diag_dominance(matrix):
    return np.alltrue([matrix[row][row] > sum([abs(matrix[row][col]) for col in range(len(matrix)) if row != col]) for row in range(len(matrix))])


if __name__ == '__main__':
    matrix, right_side = read_matrix('input2.txt')
    np_solution = np.linalg.solve(matrix, right_side)
    jacobi = jacobi_method(matrix, right_side, 5)
    gauss = gauss_method(matrix, right_side, 5)
    print("numpy: " + str(np_solution))
    print("jacobi: " + str(jacobi))
    print("gauss: " + str(gauss))

    fig, ax = plt.subplots()
    n = 50
    r1 = [sum((jacobi_method(matrix, right_side, iter_count) - np_solution) ** 2) / len(np_solution) for iter_count in
          range(1, n)]
    ax.plot(range(1, n), np.abs(r1), 'b')
    r2 = [sum((gauss_method(matrix, right_side, iter_count) - np_solution) ** 2) / len(np_solution) for iter_count in
          range(1, n)]
    ax.plot(range(1, n), np.abs(r2), 'r')
    ax.set(xlabel='n', ylabel='eps', title='')
    ax.set_yscale('log')
    ax.grid()
    plt.show()



