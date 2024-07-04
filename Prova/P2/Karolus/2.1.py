"""
@Carlos Alexandre Sousa Silva

Digits_cpf = 620
mat = [mat(1), mat(2), mat(3)]
mat = [6,2,0]

Assign:
Resolva essa questao em python usando no maximo numpy

Considere os dados
x           1.6     2.0     2.5     3.2     4.0     4.5
f(x)        mat(1)  mat(2)  mat(3)  15      8       2

a) Determine f(2.8) pela interpolaçao de Lagrange
b) Determine f(2) pela interpolaçao de Lagrange

"""

import numpy as np
from scipy.interpolate import lagrange

# Dados fornecidos
x = np.array([1.6, 2.0, 2.5, 3.2, 4.0, 4.5])
mat = np.array([6, 2, 0])
f_x = np.array([mat[0], mat[1], mat[2], 15, 8, 2])

# Função de interpolação de Lagrange usando scipy
poly = lagrange(x, f_x)

# Calcular f(2.8) e f(2)
f_2_8 = poly(2.8)
f_2 = poly(2.0)

print(f"f(2.8) pela interpolaçao de Lagrange: {f_2_8:.5f}")
print(f"f(2) pela interpolaçao de Lagrange: {f_2:.5f}")
