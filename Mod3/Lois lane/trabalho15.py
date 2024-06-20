import numpy as np

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

# Dados fornecidos
x = np.array([-1, 0, 1, 2])
y = np.array([17, 14, 10, 40])

# Valor a ser interpolado
x_value = 1.5

# Calculando a interpolação
y_value = lagrange_interpolation(x, y, x_value)

print(f'O valor de f({x_value}) é {y_value}')