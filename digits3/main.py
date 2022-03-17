import numpy as np


def read_matrix(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    matrix = []
    right_side = []
    for row in lines:
        new_row = [int(j) for j in row.split()]
        matrix.append(new_row[:(len(new_row) - 1)])
        right_side.append(new_row[len(new_row) - 1])
    return matrix, right_side


def compress_matrix(matrix, right_side):
    n = len(matrix)
    res = [matrix[0][0], matrix[0][1], right_side[0]]
    for i in range(1, n - 1):
        res.append(matrix[i][i - 1])
        res.append(matrix[i][i])
        res.append(matrix[i][i + 1])
        res.append(right_side[i])
    res.append(matrix[n - 1][n - 2])
    res.append(matrix[n - 1][n - 1])
    res.append(right_side[n - 1])
    return res, n


def solution(data, length):
    y = [data[0]]
    alpha = [- data[1] / y[0]]
    beta = [data[2] / y[0]]
    for i in range(1, length - 1):
        y.append(data[4 * i] + data[4 * i - 1] * alpha[i - 1])
        alpha.append(- data[4 * i + 1] / y[i])
        beta.append((data[4 * i + 2] - data[4 * i - 1] * beta[i - 1]) / y[i])
    y.append(data[4 * (length - 1)] + data[4 * (length - 1) - 1] * alpha[length - 2])
    alpha.append(- data[4 * (length - 1) + 1] / y[(length - 1)])
    beta.append((data[4 * (length - 1) + 1] - data[4 * (length - 1) - 1] * beta[length - 2]) / y[length - 1])
    x = [beta[length - 1]]
    for i in range(length - 2, -1, -1):
        x.insert(0, alpha[i] * x[0] + beta[i])
    return x


if __name__ == '__main__':
    matrix, right_side = read_matrix('input.txt')
    np_solution = np.linalg.solve(matrix, right_side)
    data, length = compress_matrix(matrix, right_side)
    mine_solution = solution(data, length)
    print("numpy: " + str(np_solution))
    print("mine: " + str(mine_solution))
    print("Equals" if (np.allclose(np_solution, mine_solution)) else "Not Equals")

