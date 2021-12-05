from math import tan, cos, sin


def f(x):
    return tan(x) - 1 + 0.6 * x


def f_first_derivative(x):
    return 1.0 / (cos(x)**2) + 0.6


def f_second_derivative(x):
    return (2.0 * sin(x)) / (cos(x)**3)


# min f'(x) = f'(a) для [a;b] c [0; 1] из-за монотонности f''(x)
f1_min = f_first_derivative(0.5)
# max f''(x) = f''(1) для [a;b] c [0; 1] из-за мнотонности f''(x)
f2_max = f_second_derivative(0.6)


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
