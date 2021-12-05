from math import log2, ceil
from constants import COLORS


class BinarySearchSolver:
    def __init__(self, function, a, b):
        print(f'Инициализация {COLORS.OK_GREEN}{__class__.__name__}{COLORS.END_C}')
        self.f = function
        self.a = a
        self.b = b
        self.e = 0.5 * (10 ** -5)
        print('=' * 64)

    def check(self):
        print('Проверка критерия: f(a) * f(b) < 0')
        result = self.f(self.a) * self.f(self.b)
        print(f'f(a) * f(b) = {result}')
        print('=' * 64)
        if result >= 0:
            raise ValueError('Не выполнен критерий f(a)*f(b) < 0')

    def solve(self):
        right = self.b
        left = self.a
        iter_amount = ceil(log2((self.b - self.a) / self.e))
        print(f'Вычисление x с точностью {self.e} займет {iter_amount} итераций')
        for _ in range(iter_amount):
            mid = (right + left) / 2.0
            mid_value = self.f(mid)
            right_value = self.f(right)
            left_value = self.f(left)
            if left_value * mid_value < 0:
                right = mid
            elif right_value * mid_value < 0:
                left = mid
            elif mid_value == 0:
                print(f'f({mid}) = 0')
                return
            elif right_value == 0:
                print(f'f({right}) = 0')
                return
            elif left_value == 0:
                print(f'f({left}) = 0')
                return
        mid = (right + left) / 2.0
        print(f'Ответ: x = {COLORS.OK_CYAN}{mid}{COLORS.END_C}')


class NewtonSolver:
    def __init__(self, function, derivative, second_derivative, a, b, x_start):
        print(f'Инициализация {COLORS.OK_GREEN}{__class__.__name__}{COLORS.END_C}')
        self.f = function
        self.f1 = derivative
        self.f2 = second_derivative
        self.x0 = x_start
        self.a = a
        self.b = b
        self.e = 0.5 * (10 ** -5)
        print('=' * 64)

    def check(self):
        print('Проверка критерия: f(a) * f(b) < 0')
        result = self.f(self.a) * self.f(self.b)
        print(f'f(a) * f(b) = {result}')
        if result >= 0:
            raise ValueError('Не выполнен критерий f(a)*f(b) < 0')
        print('Проверка критерия: f(x0) * f''(x0) > 0')
        result = self.f(self.x0) * self.f2(self.x0)
        print(f'f(x0) * f'f'(x0) = {result}')
        if result <= 0:
            raise ValueError('Не выполнен критерий f(x0) * f''(x0) > 0')
        print('=' * 64)

    def solve(self):
        x = self.x0
        iter_amount = 0
        while True:
            iter_amount += 1
            new_x = x - (self.f(x) / float(self.f1(x)))
            if abs(x - new_x) <= self.e:
                print(f'Разница между x_{iter_amount} и x_{iter_amount - 1} < e = {self.e}. Остановка.')
                print(f'Ответ: x = {COLORS.OK_CYAN}{new_x}{COLORS.END_C}')
                print(f'Количество итераций для вычисления: {iter_amount}')
                return
            x = new_x


