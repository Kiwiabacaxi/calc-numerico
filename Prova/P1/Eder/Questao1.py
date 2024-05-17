"""
Agua esta escoando em um canal trapezoidal a uma vazao de Q = 20 m³/s. A profundidade critica y para tal canal deve satisfa\er a equação

0 = 1 - (Q²/(gA³c))B

onde g = 9.81 m/s², Ac é a area da seção transversal (m²), e B é a largura do canal na superfície (m).
Para esse caso, a largura e a área transversal podem ser relacionadas à profundidade x por

B = 3 + x e Ac = 3x + x²/2

Encontre a profundidade crítica usando o método da bisseção. Use como aproximações iniciais xl = 0.5 e xu = 3.296296296. 
Exiba os resultados das primeiras 5 iterações, sendo xl, xu e raiz estimada para cada iteração.
Apresente até as 6 primeiras casas após a vírgula.

"""

import math

# Constantes do problema
Q = 20
g = 9.81

# Funções para calcular B e Ac
B = lambda x: 3 + x
Ac = lambda x: 3*x + x**2/2

# Função para calcular a equação dada
f = lambda x: 1 - (Q**2 / (g * Ac(x)**3)) * B(x)

# Método da bisseção
def bisection(xl, xu, iterations):
    for i in range(iterations):
        xr = (xl + xu) / 2
        if f(xl) * f(xr) < 0:
            xu = xr
        else:
            xl = xr
        print(f"Iteração {i+1}: xl = {xl:.6f}, xu = {xu:.6f}, raiz estimada = {xr:.6f}")

# Executar o método da bisseção para as primeiras 5 iterações
bisection(0.5, 3.296296296, 5)