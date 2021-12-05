from math import tan, cos, sin


def f(x):
    return tan(x) - 1 + 0.6 * x


def f_first_derivative(x):
    return 1.0 / (cos(x)**2) + 0.6


def f_second_derivative(x):
    return (2.0 * sin(x)) / (cos(x)**3)
