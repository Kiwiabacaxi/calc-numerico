"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Assign:
Crie um programa no Python para ajustar um polinômio de
segundo grau aos dados da Tabela abaixo. Exiba os
coeficientes da equação e o coeficiente de rˆ2.

x_i = 0, 1, 2, 3, 4, 5
y_i = 3.1 , 6.9, 13.6, 28.2, 42.9, 61.1

"""

import numpy as np

# Dataset
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([3.1, 6.9, 13.6, 28.2, 42.9, 61.1])

# Ajuste de um polinômio de segundo grau
Coeficientes = np.polyfit(x, y, 2)

# Coeficientes do polinômio de segundo grau
a, b, c = Coeficientes
print("Coeficientes do polinômio de segundo grau:")
print("a =", a)
print("b =", b)
print("c =", c)

# Coeficiente de determinação (R²)
y_pred = a * x**2 + b * x + c
ss_res = np.sum((y - y_pred) ** 2)
ss_tot = np.sum((y - np.mean(y)) ** 2)
r_squared = 1 - (ss_res / ss_tot)
print("\nCoeficiente de determinação (R²):", r_squared)
