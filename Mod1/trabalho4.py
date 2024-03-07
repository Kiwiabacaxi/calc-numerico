"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Assign:
Crie um programa no PYTHON para encontrar raízes
pelo método de iteração de ponto fixo simples da
função

com aproximação inicial 2.
erro maximo = 0,0001

f(x) = 2x^3 - 11.7x^2 + 17.7x - 5
"""

import numpy as np


# def f(x):
#     return 2 * np.power(x, 3) - 11.7 * np.power(x, 2) + 17.7 * x - 5


# def g(x):
#     return (2 * np.power(x, 3) - 11.7 * np.power(x, 2) + 5) / 17.7


def f(x):
    return 2 * np.power(x, 3) - 11.7 * np.power(x, 2) + 17.7 * x - 5


def g1(x):
    return (5 + 11.7 * np.power(x, 2) - 2 * np.power(x, 3)) / 17.7


def g2(x):
    return np.sqrt((((2 * x**3) + (17.7 * x) - 5) / 11.7))


def g3(x):
    return np.cbrt((((11.7 * x**2) - (17.7 * x) + 5) / 2))


# def fixed_point_iteration(f, g, x0, tol):
#     iteracao = 0
#     while True:
#         iteracao += 1
#         x = g(x0)
#         print(f"Iteração {iteracao}: x = {x}")
#         if abs(x - x0) < tol:
#             break
#         x0 = x
#     return x
def fixed_point_iteration(f, g, x0, tol, N=100):
    print("\n\n*** FIXED POINT ITERATION ***")
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        print("Iteration-%d, x1 = %0.6f and f(x1) = %0.6f" % (step, x1, f(x1)))
        x0 = x1

        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > tol

    if flag == 1:
        print("\nRequired root is: %0.8f" % x1)
        return x1
    else:
        print("\nNot Convergent.")
        return None


if __name__ == "__main__":
    x0 = 2
    tol = 0.0001
    raiz1 = fixed_point_iteration(f, g1, x0, tol)
    print(f"Raiz encontrada com g1: {raiz1}")
    print(f"Valor de f na raiz: {f(raiz1)}")

    raiz2 = fixed_point_iteration(f, g2, x0, tol)
    print(f"Raiz encontrada com g2: {raiz2}")
    print(f"Valor de f na raiz: {f(raiz2)}")

    raiz3 = fixed_point_iteration(f, g3, x0, tol)
    print(f"Raiz encontrada com g3: {raiz3}")
    print(f"Valor de f na raiz: {f(raiz3)}")
