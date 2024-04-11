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

# Definindo o sistema de equações na forma de matriz
A = np.array([[6, 2, 1, -1], [-2, 7, -1, 1], [-1, 1, 8, 1], [2, 2, 1, 9]], dtype=float)
y = np.array([2, 1 / 2, 2, 1], dtype=float)

# gauss seidel


def gauss_seidel(
    A: np.ndarray, y: np.ndarray, x0: np.ndarray, tolerancia: float, max_iterations=1000
) -> tuple:
    """
    Resolve um sistema de equações lineares usando o método de Gauss-Seidel.

    Args:
        A: Matriz de coeficientes do sistema.
        y: Vetor de termos independentes.
        x0: Vetor de aproximação inicial.
        tolerancia: Tolerância para o critério de parada.
        max_iterations: Número máximo de iterações.

    Returns:
        Uma tupla contendo:
            x: Solução aproximada do sistema.
            iteracoes: Número de iterações realizadas.
    """

    n = len(y)
    x = np.copy(x0)
    iteracoes = 0

    for _ in range(max_iterations):
        print(f"Iteração {iteracoes}: x = {x}")
        x_old = np.copy(x)
        for i in range(n):
            x[i] = (
                y[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1 :], x_old[i + 1 :])
            ) / A[i, i]
        if np.linalg.norm(x - x_old) < tolerancia:
            break
        iteracoes += 1
    return x, iteracoes


# Aproximação inicial e tolerância
x0 = np.array([0, 0, 0, 0], dtype=float)
epsilon = 0.02

# Resolvendo o sistema com o método de Gauss-Seidel
x, num_iterations = gauss_seidel(A, y, x0, epsilon)
print(f"A solução do sistema é {x} encontrada em {num_iterations} iterações.")

# usando linalg
# x = np.linalg.solve(A, y)
# print(f"A solução do sistema é {x}.")