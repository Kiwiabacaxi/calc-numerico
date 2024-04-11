"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Assign:
Crie um programa que utiliza o método de Gauss-
Seidel para resolver o sistema:
 6x + 2y + 1z - 1w = 2
-2x + 7y - 1z + 1w = 1/2
-1x + 1y + 8z + 1w = 2
 2x + 2y + 1z + 9w = 1

Utilize como aproximação inicial a quádrupla
ordenada (0,0,0,0) e como tolerância ε = 0,02.

"""

import numpy as np

def gauss_seidel(a, b, x, n, e):
    # Iterando até a condição de parada
    for j in range(n):
        temp = np.copy(x)
        for i in range(a.shape[0]):
            # Somatório dos elementos da linha i exceto o elemento da diagonal
            sum = np.dot(a[i, :i], x[:i]) + np.dot(a[i, i + 1:], x[i + 1:])
            # Atualização do valor de x[i]
            x[i] = (b[i] - sum) / a[i, i]
        # Verificando a condição de parada
        if np.allclose(x, temp, rtol=e):
            return x
    return x

# Matriz de coeficientes
a = np.array([[6.0, 2.0, 1.0, -1.0],
              [-2.0, 7.0, -1.0, 1.0],
              [-1.0, 1.0, 8.0, 1.0],
              [2.0, 2.0, 1.0, 9.0]])

# Vetor de termos independentes
b = np.array([2.0, 0.5, 2.0, 1.0])

# Vetor de aproximação inicial
x = np.array([0.0, 0.0, 0.0, 0.0])

# Número de iterações
n = 100

# Tolerância
e = 0.02

# Chamando a função gauss_seidel
solution = gauss_seidel(a, b, x, n, e)

print('A solução é:', solution)