import numpy as np
from scipy import optimize

def lagrange_interpolation(x, y, x_value):
    n = len(x)
    p = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (x_value - x[j]) / (x[i] - x[j])
        p += y[i] * L
    return p


def objective(x):
    return lagrange_interpolation(x_values, y_values, x) - 15

x_values = np.array([-1, 0, 1, 2])
y_values = np.array([17, 14, 10, 40])

solution = optimize.root(objective, 0)  # 0 é o chute inicial
x = solution.x[0]

print(f'O valor de x para o qual f(x) = 15 é {x}')