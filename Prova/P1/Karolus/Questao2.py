"""
@Carlos Alexandre Sousa Silva

Digits_cpf = 620
mat = [mat(1), mat(2), mat(3)]
mat = [6,2,0]

Assign:
Use a iteraçao de ponto fixo simples para localizar a raiz de f(x) = 2*sin(sqrt(x)) - x
Use  a aproximaçao inicial x0 = 0.1111111111111111
Use 6 casas decimais apos a virgula para mostrar os resultados na tabela abaixo das 5 primeiras iteraçoes.
Considere que a primeira iteraçao é aquela que contém a aproximaçao inicial obtida para x0.

me de uma tabela formatadinha que tenha as iteraçoes e a raiz estimada
lembrando que a primeira iteraçao é 0.1111111111111111 e a raiz é 1.9723810010822, entao so tem que descobrir a iteraçao 2, 3 e 4
"""

import numpy as np
import pprint

# Definindo a função f(x)
def f(x):
    return 2 * np.sin(np.sqrt(x)) - x

# Definindo g(x) a partir de f(x) = 0 -> g(x) = x = 2*sin(sqrt(x))
def g(x):
    return 2 * np.sin(np.sqrt(x))

# Aproximação inicial
x0 = 0.1111111111111111
results = [(0, x0)]  # Lista para armazenar os resultados de cada iteração

# Realizar as iterações
for i in range(1, 6):  # 5 iterações desejadas
    x0 = g(x0)  # Nova aproximação
    results.append((i, x0))

pprint.pprint(results)  # Exibir resultados
