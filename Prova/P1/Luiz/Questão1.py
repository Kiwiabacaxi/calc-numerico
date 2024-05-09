""" 
@Luiz Antonio Folador

mat = [6,0,0]


Assign:
Agua esta escoando em um canal trapezoidal a uma vazao de q = 20 mˆ3/s.
A profundidade critica y para tal canal deve satisfazer a equação

0 = 1 - (Qˆ2/gA_cˆ3) * B
Onde g = 9,81 m/sˆ2 é a aceleração da gravidade, A_c é a área da seção transversal do canal,(mˆ2) e B é a largura do canal na superficie (m).
Para esse caso, a largura e a area transversal podem ser relacionadas a profundidade x por

B = 3 + x
e
A_c = 3x + (xˆ2/2)

Encontre a profundidade critica usando o metodo da bisseção, Use como aproximaçãoes iniciais x1 = 0.5 e x_u = ((mat(1) + mat(2) + mat(3))/27) + 3
Exiba na tabela abaixo os resultados das primeiras 5 iteraçoes, considerando que na primeira deverao ser consideradas os primeiros valores obtidos pelas formulas apresentadas para x1 e x_u.
Apresente ate as 6 primeiras casas apos a virgula.
"""

import numpy as np

# Constantes
g = 9.81  # aceleração da gravidade
Q = 20  # vazão

# Funções para calcular B e A_c
B = lambda x: 3 + x
A_c = lambda x: 3*x + (x**2)/2

# Função para a equação que deve ser igual a zero
f = lambda x: 1 - (Q**2 / g / A_c(x)**3) * B(x)

# Método da bisseção
def bissecao(f, x1, xu, n_iter):
    for i in range(n_iter):
        xr = (x1 + xu) / 2
        if f(x1) * f(xr) < 0:
            xu = xr
        else:
            x1 = xr
        print(f"Iteração {i+1}: x1 = {x1:.6f}, xu = {xu:.6f}, xr = {xr:.6f}")
    return xr

# Valores iniciais
x1 = 0.5
xu = ((6 + 0+ 0) / 27) + 3

# Executar o método da bisseção para as primeiras 5 iterações
bissecao(f, x1, xu, 5)