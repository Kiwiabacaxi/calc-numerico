import numpy as np

aprox_inicial = -8
fp = 0.0000001 - 8
erro_maximo = 0.0001


def f(x):
    return np.sin((x / 2)) * np.log10(-10 * x)


def metodSecante(f, x0, fp, erro_maximo):
    x2 = fp - (f(fp) * (fp - x0)) / (f(fp) - f(x0))

    while np.abs(f(x2)) > erro_maximo:
        x0, fp = fp, x2
        x2 = fp - (f(fp) * (fp - x0)) / (f(fp) - f(x0))
        print(x2)
    return x2


print("Printando a função")
# print(f(aprox_inicial))
print(metodSecante(f, aprox_inicial, fp, erro_maximo))
