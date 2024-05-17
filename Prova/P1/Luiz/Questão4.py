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



def gauss_jacobi(
    A: np.ndarray, b: np.ndarray, x0: np.ndarray
) -> tuple:
    """
    Resolve um sistema de equações lineares usando o método de Gauss-Jacobi.

    Args:
        A: Matriz de coeficientes do sistema.
        b: Vetor de termos independentes.
        x0: Vetor de aproximação inicial.
        tolerancia: Tolerância para o critério de parada.

    Returns:
        Uma tupla contendo:
            x: Solução aproximada do sistema.
            iteracoes: Número de iterações realizadas.
    """
    # Cria um vetor com os elementos da diagonal de A e subtrai-os de A
    D = np.diag(A)
    R = A - np.diagflat(D)

    # Inicializa o contador de iterações
    iteracoes = 0

    while True:
        print(f"Iteração {iteracoes}: x = {x0}")
        x = (b - np.dot(R, x0)) / D
        if np.allclose(x0, x):
            return x, iteracoes
        x0 = x
        iteracoes += 1


# Encontra a solução do sistema
x, num_iterations = gauss_jacobi(A, b, x0)

print(f"A solução do sistema é {x} encontrada em {num_iterations} iterações.")
