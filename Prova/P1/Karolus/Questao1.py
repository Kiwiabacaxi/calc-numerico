"""
@Carlos Alexandre Sousa Silva

Digits_cpf = 620
mat = [mat(1), mat(2), mat(3)]
mat = [6,2,0]

Assign:
Agua esta escoando em um canal trapezoidal a uma vazao de q = 20 mˆ3/s.
A profundidade critica y para tal canal deve satisfazer a equação

0 = 1 - (Qˆ2/gA_cˆ3) * B
Onde g = 9,81 m/sˆ2 é a aceleração da gravidade, A_c é a área da seção transversal do canal,(mˆ2) e B é a largura do canal na superficie (m).
Para esse caso, a largura e a area transversal podem ser relacionadas a profundidade x por

B = 3 + x
e
A_c = 3x + (xˆ2/2)

Encontre a profundidade critica usando o metodo da bisseção, Use como aproximaçãoes iniciais x1 = 0.5 e x_u = 3.2962962962962963
Exiba na tabela abaixo os resultados das primeiras 5 iteraçoes, considerando que na primeira deverao ser consideradas os primeiros valores obtidos pelas formulas apresentadas para x1 e x_u.
Apresente ate as 6 primeiras casas apos a virgula.

me de apenas x1, x_u e a Raiz estimada

x_u = 3.2962962962962963
"""

# import numpy as np
import pprint
# import pandas as pd


def calcular_B(x):
    return 3 + x

def calcular_Ac(x):
    return 3*x + (x**2 / 2)

def calcular_f(x, Q=20, g=9.81):
    B = calcular_B(x)
    Ac = calcular_Ac(x)
    return 1 - (Q**2 / g / Ac**3) * B

# Método da bisseção
# def metodo_bissecao(f, x1, xu, iteracoes):
#     resultados = []
#     for i in range(iteracoes):
#         xr = (x1 + xu) / 2
#         f_xr = f(xr)
#         f_x1 = f(x1)
        
#         resultados.append((x1, xu, xr))
        
#         if f_x1 * f_xr < 0:
#             xu = xr
#         else:
#             x1 = xr
            
#     return resultados

def metodo_bissecao(f, x1, xu, iteracoes):
    resultados = []
    for i in range(iteracoes):
        xr = (x1 + xu) / 2
        f_xr = f(xr)
        f_x1 = f(x1)
        
        resultados.append((round(x1, 6), round(xu, 6), round(xr, 6)))
        
        if f_x1 * f_xr < 0:
            xu = xr
        else:
            x1 = xr
            
    return resultados

# Parâmetros iniciais
x1 = 0.5
xu = 3.2962962962962963

# Executa 5 iterações do método da bisseção
resultados_bissecao = metodo_bissecao(calcular_f, x1, xu, 5)
pprint.pprint(resultados_bissecao)