import numpy as np
import matplotlib.pyplot as plt


def function(x, y):
    return np.log(np.sqrt(x) / y) ** 2 + np.arctan(5 * y ** 3)


def analytical_derivative_x(x, y):
    return np.log(np.sqrt(x) / y) / x


def analytical_derivative_y(x, y):
    return 15 * y ** 2 / (25 * y ** 6 + 1) - 2 * np.log(np.sqrt(x) / y) / y


def numerical_derivative(x, y, step_x, step_y):
    return (function(x + step_x, y + step_y) - function(x - step_x, y - step_y)) / (2 * (step_x + step_y))


def draw_function():

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    i_x = np.arange(1.0, 4.0, 0.01)
    i_y = np.arange(1, 9.0, 0.01)
    x, y = np.meshgrid(i_x, i_y)
    f = function(x, y)

    ax.plot_surface(x, y, f)
    ax.set(xlabel='x', ylabel='y', zlabel='f', title='f = log(sqrt(x)/y)^2+atan(5*y^3)')
    ax.grid()
    plt.show()


def print_gradient(x, y, step):

    print("function value at x = {0}, y = {1} is {2}".format(x, y, function(x, y)))
    print("analytical gradient value at x = {0}, y = {1} is ({2}, {3})".format(
        x, y, analytical_derivative_x(x, y), analytical_derivative_y(x, y)))
    print("numerical gradient value at x = {0}, y = {1} with step = {2} is ({3}, {4})".format(
        x, y, step, numerical_derivative(x, y, step, 0), numerical_derivative(x, y, 0, step)))


if __name__ == '__main__':
    print_gradient(2, 2, 1e-5)
    draw_function()



