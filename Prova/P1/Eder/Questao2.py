"""
Use a iteração de ponto fixo simples para localizar a raiz de f(x) = 2sen(sqrt(x))-x.
Use aproximação inicial x0 = 0,333333333.
Use 6 casas após a vírgula para mostrar os resultados (raiz estimada) das 5 primeiras iterações.
Considere que a primeira iteração é aquela que contém a aproximação inicial obtida para x0.
"""

import math

def f(x):
    return 2*math.sin(math.sqrt(x)) - x

def ponto_fixo(f, x0, iteracoes):
    print("{:.6f}".format(x0))
    for i in range(iteracoes):
        x0 = f(x0)
        print("{:.6f}".format(x0))

ponto_fixo(f, 0.333333333, 5)