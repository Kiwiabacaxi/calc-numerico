"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Assign:
Crie um programa que utiliza a interpolação
quadrática para maximizar a função
f(x) = -x^4 + 2x^3 - 2x^ + 6

considerando os pontos de busca iniciais - 7,
- 2 e 1. Estabeleça como critério de parada a
precisão de 10^-8 para o erro estimado.
"""

# import numpy as np


# Define a função dada no exercício
def f(x):
    return -(x**4) + 2 * x**3 - 2 * x**2 + 6


# Define o método da interpolação quadrática
def quadratic_interpolation(f, x0, x1, x2, tol=1e-8, max_iterations=100):
    for i in range(max_iterations):
        fx0 = f(x0)
        fx1 = f(x1)
        fx2 = f(x2)

        L0 = (x1 * x2) / ((x0 - x1) * (x0 - x2))
        L1 = (x0 * x2) / ((x1 - x0) * (x1 - x2))
        L2 = (x0 * x1) / ((x2 - x0) * (x2 - x1))

        x3 = L0 * fx0 + L1 * fx1 + L2 * fx2

        print(f"Iteration {i+1}: x0 = {x0}, x1 = {x1}, x2 = {x2}, x3 = {x3}")

        if x3 < x1:
            x0, x1, x2 = x0, x1, x3
        else:
            x0, x1, x2 = x1, x3, x2

        if abs(x3 - x1) < tol:
            return x3, i

    return x3, max_iterations


# Encontra o ponto de máximo da função
x_max, num_iterations = quadratic_interpolation(f, -7, -2, 1)

print(
    f"O ponto de máximo da função é {x_max} encontrado em {num_iterations} iterações."
)
