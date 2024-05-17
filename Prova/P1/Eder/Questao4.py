"""
O seguinte sistema de esquações é projetado para determinar as concentrações (os c's em g/m³) em uma série de 
reatores acoplados como função da quantidade de entrada da massa em cada reator (o lado direito está em g/dia),

15c1 - 3c2 - c3 = 3818
-3c1 + 18c2 - 6c3 = 1200
-4c1 - c2 + 12c3 = 2356

Considere a aproximação inicial (0,0,0) e obtenha as 3 primeiras iterações da resolução desse problema pelo método
da itereação de Gauss-Jacobi. A primeira iteração é aquela que considera a aproximação inicial.
Mostre os valores de c1, c2 e c3 para cada iteração.

"""

import numpy as np

# Definindo as equações
A = np.array([[15, -3, -1], [-3, 18, -6], [-4, -1, 12]])
b = np.array([3818, 1200, 2356])

# Definindo a aproximação inicial
x = np.zeros_like(b)

# Definindo a função para o método de Gauss-Jacobi
def gauss_jacobi(A, b, x, num_iter):
    D = np.diag(np.diag(A))
    LU = A - D
    x = np.dot(np.linalg.inv(D), b - np.dot(LU, x))
    for i in range(num_iter):
        x = np.dot(np.linalg.inv(D), b - np.dot(LU, x))
        print(f'Iteração {i+1}: {x}')
    return x

# Chamando a função para as 3 primeiras iterações
gauss_jacobi(A, b, x, 3)