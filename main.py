from solvers import BinarySearchSolver, NewtonSolver, ModifiedNewtonSolver
from constants import f, f_first_derivative, f_second_derivative

binarySolver = BinarySearchSolver(f, 0, 1)
binarySolver.check()
binarySolver.solve()
print('=' * 64)
newtonSolver = NewtonSolver(f, f_first_derivative, f_second_derivative, 0, 1, 1)
newtonSolver.check()
newtonSolver.solve()
print('=' * 64)
modifiedSolver = ModifiedNewtonSolver(f, f_first_derivative, f_second_derivative, 0, 1, 1)
modifiedSolver.check()
modifiedSolver.solve()
