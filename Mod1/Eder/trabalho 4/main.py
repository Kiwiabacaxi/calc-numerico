import numpy as np


def f(x):
    return (2 * x**3) - (11.7 * x**2) + (17.7 * x) - 5


def g1(x):
    return (5 + (11.7 * x**2) - (2 * x**3)) / 17.7


def g2(x):
    return np.sqrt((((2 * x**3) + (17.7 * x) - 5) / 11.7))


def g3(x):
    return np.cbrt((((11.7 * x**2) - (17.7 * x) + 5) / 2))


x0 = 2
erro_maximo = 0.0001


def pontoFixo(g, x0, erro_maximo):
    x = g(x0)

    erro = abs((x - x0) / x)

    while erro > erro_maximo:
        x0 = x
        x = g(x0)
        erro = abs((x - x0) / x)
        print(x)


print("Primeira função")
print(pontoFixo(g1, x0, erro_maximo))
print("Segunda função")
print(pontoFixo(g2, x0, erro_maximo))
print("Terceira função")
print(pontoFixo(g3, x0, erro_maximo))
