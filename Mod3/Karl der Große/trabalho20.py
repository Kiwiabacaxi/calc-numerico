"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Trabalho 20:
Crie um programa no Python para resolver o problema de valor inicial
dy/dt = yt^3 - 1.5y, y(0) = 1
usando o método de Euler. O programa deverá permitir a escolha de h. Verifique os resultados com h = 0,25 e o intervalo para t de 0 a 4.
"""

import numpy as np


def dydt(t, y):
    """
    Define a derivada dy/dt.

    Parâmetros:
    t (float): O valor de t.
    y (float): O valor de y.

    Retorna:
    float: O valor da derivada dy/dt.
    """
    return y * t**3 - 1.5 * y


def euler_method(dydt, t0, y0, h, t_end):
    """
    Resolve a EDO usando o método de Euler.

    Parâmetros:
    dydt (function): A função que define a derivada dy/dt.
    t0 (float): O valor inicial de t.
    y0 (float): O valor inicial de y.
    h (float): O tamanho do passo.
    t_end (float): O valor final de t.

    Retorna:
    tuple: Dois arrays, um com os valores de t e outro com os valores de y.
    """
    t_values = np.arange(t0, t_end + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0

    for i in range(1, len(t_values)):
        y_values[i] = y_values[i - 1] + h * dydt(t_values[i - 1], y_values[i - 1])

    return t_values, y_values


# Valores padrão
t0 = 0
y0 = 1
# h = 0.25
h = float(input("Digite o valor de h: "))
t_end = 4

# Resolvendo a EDO
t_values, y_values = euler_method(dydt, t0, y0, h, t_end)

# Exibindo os resultados
for t, y in zip(t_values, y_values):
    print(f"t = {t:.2f}, y = {y:.5f}")
