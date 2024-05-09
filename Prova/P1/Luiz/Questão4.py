""" 
o seguinte sistema de equações é projetado para 
determinar as concentrações em uma serie de reatores
acoplados como função da quantidade de entrada de massa em cada reator.

{
    15c1-3c2-c3 = 3818
    -3c1+18c2-6c3 = 1200
    -4c1-c2+12c3 = 2350
}

considere a aproximação inicial (0,0,0) e obtenha as 3 primeiras 
iterações da resolução desse problema pelo metodo da iteração 
de gauss-jacobi. A primeira iteração é aquela que considera a 
aproximação inicial.

"""

import numpy as np

# Sistema de equações
A = np.array([[15, -3, -1], [-3, 18, -6], [-4, -1, 12]])
b = np.array([3818, 1200, 2350])

# Aproximação inicial
x0 = np.array([0, 0, 0])

# Método de Gauss-Jacobi
def gauss_jacobi(A, b, x0, n_iter):
    n = len(A)
    x = x0.copy()
    for k in range(n_iter):
        print(f"Iteração {k}: {x}")
        x_new = np.zeros_like(x)
        for i in range(n):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        x = x_new
    return x

# Executar o método para as primeiras 3 iterações
gauss_jacobi(A, b, x0, 3)