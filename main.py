from solvers import BinarySearchSolver, NewtonSolver, ModifiedNewtonSolver
from constants import f, f_first_derivative, f_second_derivative, f1_min, f2_max

binarySolver = BinarySearchSolver(f, 0, 1)
binarySolver.check()
binarySolver.solve()
print('=' * 64)
newtonSolver = NewtonSolver(f, f_first_derivative, f_second_derivative, 0.5, 0.6, 0.6, f1_min, f2_max)
newtonSolver.check()
newtonSolver.solve()
print('=' * 64)
modifiedSolver = ModifiedNewtonSolver(f, f_first_derivative, f_second_derivative, 0.5, 0.6, 0.6, f1_min, f2_max)
modifiedSolver.check()
modifiedSolver.solve()
