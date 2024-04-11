"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Assign:
Crie um programa que utiliza o método de Gauss-
Jacobi para resolver o sistema:
 6x + 2y + 1z - 1w = 2
-2x + 7y - 1z + 1w = 1/2
-1x + 1y + 8z + 1w = 2
 2x + 2y + 1z + 9w = 1

Utilize como aproximação inicial a quádrupla
ordenada (0,0,0,0) e como tolerância ε = 0,02.

"""

import numpy as np

# Define o sistema de equações
A = np.array([[6, 2, 1, -1], [-2, 7, -1, 1], [-1, 1, 8, 1], [2, 2, 1, 9]])
y = np.array([2, 1 / 2, 2, 1])


def gauss_jacobi(
    A: np.ndarray, b: np.ndarray, x0: np.ndarray, tolerancia: float
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
        if np.allclose(x0, x, rtol=tolerancia):
            return x, iteracoes
        x0 = x
        iteracoes += 1


# Encontra a solução do sistema
x, num_iterations = gauss_jacobi(A, y, np.array([0, 0, 0, 0]), 0.02)

print(f"A solução do sistema é {x} encontrada em {num_iterations} iterações.")
