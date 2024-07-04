"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Trabalho 22:
Crie um programa no Python para resolver o problema de valor inicial
dy/dt = yt^3 - 1.5y, y(0) = 1
usando o método de Heun com iteração. O algoritmo deverá convergir para um erro tolerado para cada estimativa. O programa deverá permitir a escolha de h. Verifique os resultados com h = 0,25 e o intervalo para t de 0 a 4.
"""

import numpy as np


def f(t, y):
    return y * t**3 - 1.5 * y


def heun_method(dydt, t0, y0, h, t_end, tol=1e-6, max_iter=10):
    t_values = np.arange(t0, t_end + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0

    for i in range(1, len(t_values)):
        k1 = dydt(t_values[i - 1], y_values[i - 1])
        y_predict = y_values[i - 1] + h * k1
        k2 = dydt(t_values[i], y_predict)
        y_corrected = y_values[i - 1] + (h / 2) * (k1 + k2)

        iter_count = 0
        while np.abs(y_corrected - y_predict) > tol and iter_count < max_iter:
            y_predict = y_corrected
            k2 = dydt(t_values[i], y_predict)
            y_corrected = y_values[i - 1] + (h / 2) * (k1 + k2)
            iter_count += 1

        y_values[i] = y_corrected

    return t_values, y_values


# Valores padrão
t0 = 0
y0 = 1
# h = 0.25
h = float(input("Digite o valor de h: "))
t_end = 4

# Resolvendo a EDO usando o método de Heun com iteração
t_values, y_values = heun_method(f, t0, y0, h, t_end)

# Exibindo os resultados
for t, y in zip(t_values, y_values):
    print(f"t = {t:.2f}, y = {y:.5f}")
