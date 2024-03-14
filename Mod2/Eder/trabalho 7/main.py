import numpy as np


def f(x):
    return (((-x)**4)+(2*x**3)-(2*x)+6)

def interpolacao_quadratica(f, x1, x2, x3, erro):
    res1 = f(x1)
    res2 = f(x2)
    res3 = f(x3)

    x4 = x2 - 1/2 * ((x2 - x1)**2 * (res2 - res3) - (x2 - x3)**2 * (res2 - res1)) / ((x2 - x1) * (res2 - res3) - (x2 - x3) * (res2 - res1))

    print("-> ", x4)

    xanterior = x4
    erro_absoluto = np.inf

    while erro_absoluto > erro:
        res4 = f(x4)
        if res4 > res2:
            if x4 > x2:
                x3 = x4
            else:
                x1 = x4
        else:
            if x4 > x2:
                x1 = x2
            else:
                x3 = x2

        x4 = x2 - 1/2 * ((x2 - x1)**2 * (res2 - res3) - (x2 - x3)**2 * (res2 - res1)) / ((x2 - x1) * (res2 - res3) - (x2 - x3) * (res2 - res1))
        erro_absoluto = np.abs((x4 - xanterior)/x4)
        print("-> ", x4)
        xanterior = x4

    return x4

print(interpolacao_quadratica(f, -6, 0, 6, 0.00000001))

        