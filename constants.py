from math import tan, cos, sin


def f(x):
    return tan(x) - 1 + 0.6 * x


def f_first_derivative(x):
    return 1.0 / (cos(x)**2) + 0.6


def f_second_derivative(x):
    return (2.0 * sin(x)) / (cos(x)**3)


class COLORS:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_CYAN = '\033[96m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END_C = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
