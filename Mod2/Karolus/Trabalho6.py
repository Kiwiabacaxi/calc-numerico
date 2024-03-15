"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Assign:
Crie um programa que utiliza a razão áurea
para maximizar a função
f(x) = -x^4 + 2x^3 - 2x^ + 6

Considerando o intervalo de busca inicial de
[- 6, 6]. Estabeleça como critério de parada a
precisão de 10^-8 para o erro estimado.
"""

import numpy as np


# Define a função dada no exercício
def f(x):
    return -(x**4) + 2 * x**3 - 2 * x**2 + 6


def golden_ratio_method(f, a, b, tol=1e-8, max_iterations=100):
    c = (3 - np.sqrt(5)) / 2 * (b - a) + a
    d = (np.sqrt(5) - 1) / 2 * (b - a) + a
    fc = f(c)
    fd = f(d)

    for i in range(max_iterations):
        if fc < fd:
            b = d
            d = c
            c = (3 - np.sqrt(5)) / 2 * (b - a) + a
            fd = fc
            fc = f(c)
        else:
            a = c
            c = d
            d = (np.sqrt(5) - 1) / 2 * (b - a) + a
            fc = fd
            fd = f(d)

        print(
            f"Iteration {i+1}: a = {a}, b = {b}, c = {c}, d = {d}, fc = {fc}, fd = {fd}"
        )

        if abs(b - a) < tol:
            return (a + b) / 2, i

    return (a + b) / 2, max_iterations


# Encontra o ponto de máximo da função
x_max, num_iterations = golden_ratio_method(f, -6, 6)

print(
    f"O ponto de máximo da função é {x_max} encontrado em {num_iterations} iterações."
)
