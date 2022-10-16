from scipy.optimize import linprog

# Example problem from slide 22 is presented below.

# Minimize:
#   1x1 + 1x2 + 1x3 + 1x4
c = [1, 1, 1, 1]

# Subject to:
#   1x1 + 2x2 - 1x3 - 1x4 == 1
#  -1x1 - 5x2 + 2x3 + 3x4 == 1
A = [[1, 2, -1, -1],
     [-1, -5, 2, 3]]
b = [1, 1]

# Bounded by:
#   x1, x2, x3, x4 >= 0
bound = [(0, None), (0, None), (0, None), (0, None)]

# Using scipy.optimize.linprog:
result = linprog(c, A_eq=A, b_eq=b, bounds=bound, method='highs')

print(result.fun)
print(result.x)
print(result.message)

# COMMAND PROMPT OUTPUT:
'''
3.0
[2. 0. 0. 1.]
Optimization terminated successfully.
'''
# This output is equivalent to the basic feasible solution on slide 30.
# Which, as determined on slide 32, is one of the optimal solutions.

# Note:
n = len(c) # the number of variables is the length of vector c
m = len(A) # the number of constraints is the number of rows in matrix A

print(f'n={n}, m={m}')

# COMMAND PROMPT OUTPUT:
'''
n=4, m=2
'''
