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

phi = ((1 + np.sqrt(5)) / 2)

def f(x):
    return (((-x)**4)+(2*x**3)-(2*x)+6)

def razao_aurea(f, xl, xu, erro, phi):
    d = (phi - 1) * (xu - xl)
    x1 = xl + d
    x2 = xu - d
    
    res1 = f(x1)
    res2 = f(x2)

    if res1 > res2:
        xl = x1
        erro_absoluto = (2 - phi) * np.abs((xu - xl)/res1)

        print("-> ", xl)

        while erro_absoluto > erro:
            d = (phi - 1) * (xu - xl)
            x1 = xl + d
            res1 = f(x1)
            if res1 > res2:
                xl = x1
                erro_absoluto = (2 - phi) * np.abs((xu - xl)/res1)
                print("-> ", xl)
            else:
                xu = x2
                x2 = x1
                res2 = res1
                erro_absoluto = (2 - phi) * np.abs((xu - xl)/res1)
                print("-> ", xu)
    else:
        xu = x2
        erro_absoluto = (2 - phi) * np.abs((xu - xl)/res2)

        print("-> ", xu)

        while erro_absoluto > erro:
            d = (phi - 1) * (xu - xl)
            x2 = xu - d
            res2 = f(x2)
            if res2 > res1:
                xu = x2
                erro_absoluto = (2 - phi) * np.abs((xu - xl)/res2)
                print("-> ", xu)
            else:
                xl = x1
                x1 = x2
                res1 = res2
                erro_absoluto = (2 - phi) * np.abs((xu - xl)/res2)
                print("-> ", xl)

    return (xl + xu) / 2
        

print(razao_aurea(f, -6, 6, 0.00000001, phi))