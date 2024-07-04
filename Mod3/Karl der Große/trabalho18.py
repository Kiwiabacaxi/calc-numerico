"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Trabalho 18:
Crie um programa no Python para calcular a integral da função
f(x) = 6 + 3cos(x) usando a regra 1/3 de Simpson. O programa deverá
permitir que o usuário escolha o intervalo de integração, a quantidade
de intervalos e apresentar o resultado da integral.
"""

import numpy as np


def f(x):
    """
    Função a ser integrada.

    Parâmetros:
    x (float): O ponto em que a função será avaliada.

    Retorna:
    float: O valor da função em x.
    """
    return 6 + 3 * np.cos(x)


def simpsons_rule(a, b, n):
    """
    Calcula a integral da função f(x) usando a regra 1/3 de Simpson.

    Parâmetros:
    a (float): Limite inferior do intervalo de integração.
    b (float): Limite superior do intervalo de integração.
    n (int): Número de intervalos (deve ser par).

    Retorna:
    float: O valor aproximado da integral.
    """
    if n % 2 == 1:
        raise ValueError("O número de intervalos deve ser par.")

    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n, 2):
        integral += 4 * f(a + i * h)
    for i in range(2, n - 1, 2):
        integral += 2 * f(a + i * h)

    integral *= h / 3
    return integral


# Valores padrão
a = 0
b = np.pi
n = 100  # Deve ser par

# Calculando a integral
integral_value = simpsons_rule(a, b, n)

print(
    f"O valor aproximado da integral de {a} a {b} com {n} intervalos é: {integral_value}"
)
