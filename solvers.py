from math import log2, ceil


class BinarySearchSolver:
    def __init__(self, function, a, b):
        print(f'Инициализация {__class__.__name__}')
        self.f = function
        self.a = a
        self.b = b
        self.e = 0.5 * (10 ** -5)
        print('=' * 64)

    def check(self):
        print('Проверка критерия: f(a)*f(b) < 0')
        result = self.f(self.a) * self.f(self.b)
        print(f'f(a)*f(b) = {result}')
        print('=' * 64)
        if result >= 0:
            raise ValueError('Не выполнен критерий f(a)*f(b) < 0')

    def solve(self):
        right = self.b
        left = self.a
        iter_amount = ceil(log2((self.b - self.a) / self.e))
        print(f'Вычисление с точностью {self.e} займет {iter_amount} итераций')
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
        print('Проверка')
        print(f'x = {mid}')
        print(f'f({mid}) = {"{:.7f}".format(self.f(mid))}')
        print(f'|f({mid}) - f(x)| = |f({mid})| = {"{:.7f}".format(abs(self.f(mid)))} < e = {self.e}')


class NewtonSolver:
    pass
