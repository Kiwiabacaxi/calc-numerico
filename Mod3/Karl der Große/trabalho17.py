"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Trabalho 17:
Crie um programa no Python para calcular a integral da função
f(x) = 6 + 3cos(x) usando a regra do trapézio. O programa deverá
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


def trapezoidal_rule(a, b, n):
    """
    Calcula a integral da função f(x) usando a regra do trapézio.

    Parâmetros:
    a (float): Limite inferior do intervalo de integração.
    b (float): Limite superior do intervalo de integração.
    n (int): Número de intervalos.

    Retorna:
    float: O valor aproximado da integral.
    """
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral


# Solicitando os dados ao usuário
a = float(input("Digite o limite inferior do intervalo de integração: "))
b = float(input("Digite o limite superior do intervalo de integração: "))
n = int(input("Digite o número de intervalos: "))

# Calculando a integral
integral_value = trapezoidal_rule(a, b, n)

print(
    f"O valor aproximado da integral de {a} a {b} com {n} intervalos é: {integral_value}"
)
