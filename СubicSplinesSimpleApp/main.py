import matplotlib.pyplot as plt
from cubic_splines.cubic_spline_2d import *
from lagranges.lagrange_2d import *
from newtons.newton_2d import *


def calculate_2d_spline_interpolation(x, y, num=100):
    cubic_spline_2d = CubicSpline2D(x, y)
    params = np.linspace(cubic_spline_2d.params[0], cubic_spline_2d.params[-1], num + 1)[:-1]

    result_x, result_y = [], []
    for param in params:
        point_x, point_y = cubic_spline_2d.point(param)
        result_x.append(point_x)
        result_y.append(point_y)

    return result_x, result_y


def calculate_2d_lagrange_interpolation(x, y, num=100):
    lagrange_2d = Lagrange2D(x, y)
    params = np.linspace(lagrange_2d.params[0], lagrange_2d.params[-1], num + 1)[:-1]

    result_x, result_y = [], []
    for param in params:
        point_x, point_y = lagrange_2d.point(param)
        result_x.append(point_x)
        result_y.append(point_y)

    return result_x, result_y


def calculate_2d_newton_interpolation(x, y, num=100):
    newton_2d = Newton2D(x, y)
    params = np.linspace(newton_2d.params[0], newton_2d.params[-1], num + 1)[:-1]

    result_x, result_y = [], []
    for param in params:
        point_x, point_y = newton_2d.point(param)
        result_x.append(point_x)
        result_y.append(point_y)

    return result_x, result_y


if __name__ == '__main__':
    x_points = []
    y_points = []
    fig, ax = plt.subplots(figsize=(9, 9), num="Simple Interpolation App")

    curve_cubic_splines, = ax.plot(x_points, y_points, "-g", label="spline")
    curve_lagrange, = ax.plot(x_points, y_points, "-r", label="lagrange")
    curve_newton, = ax.plot(x_points, y_points, "-b", label="newton")
    points, = ax.plot(x_points, y_points, "x")

    def on_click(event):
        x_new_point, y_new_point = ax.transData.inverted().transform([event.x, event.y])
        x_points.append(x_new_point)
        y_points.append(y_new_point)

        if len(x_points) > 1 and len(x_points) == len(y_points):
            x_cubic_spline_points, y_cubic_spline_points = calculate_2d_spline_interpolation(x_points, y_points,
                                                                                             num=500)
            curve_cubic_splines.set_xdata(x_cubic_spline_points)
            curve_cubic_splines.set_ydata(y_cubic_spline_points)

            x_lagrange_points, y_lagrange_points = calculate_2d_lagrange_interpolation(x_points, y_points, num=500)
            curve_lagrange.set_xdata(x_lagrange_points)
            curve_lagrange.set_ydata(y_lagrange_points)

            x_newton_points, y_newton_points = calculate_2d_newton_interpolation(x_points, y_points, num=500)
            curve_newton.set_xdata([i + 0.005 for i in x_newton_points]) # todo: смещение для проверки
            curve_newton.set_ydata(y_newton_points)

        points.set_xdata(x_points)
        points.set_ydata(y_points)

        fig.canvas.draw()

    ax.legend()
    fig.canvas.mpl_connect('button_press_event', on_click)
    plt.show()
