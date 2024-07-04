"""
Considere os dados:

x:   1.6 | 2 | 2.5 | 3.2 | 4 | 4.5
f(x): 6  | 0 |  2  |  15 | 8 |  2

a) Determine f(2.8) pela interpolação de Lagrange.
b) Determine f(2) pela interpolação de Lagrange.
"""

import numpy as np

# Dados fornecidos
x = np.array([1.6, 2, 2.5, 3.2, 4, 4.5])
y = np.array([6, 0, 2, 15, 8, 2])

# Função para calcular a interpolação de Lagrange
def lagrange_interpolation(x, y, x_point):
    total = 0
    n = len(x)
    for i in range(n):
        xi, yi = x[i], y[i]
        li = 1
        for j in range(n):
            if j != i:
                li *= (x_point - x[j]) / (xi - x[j])
        total += yi * li
    return total

# a) f(2.8)
f_2_8 = lagrange_interpolation(x, y, 2.8)

# b) f(2) - Note que f(2) deve ser exatamente igual ao valor de y para x=2, mas vamos calcular para demonstrar o método.
f_2 = lagrange_interpolation(x, y, 2)

print(f"a) f(2.8) = {f_2_8:.6f}")
print(f"b) f(2) = {f_2:.6f}")