"""
use a iteração de ponto fixo simples para localizar a 
raiz de f(x) = 2sen(sqrt(x)) - x. use aproximação 
inicial x0 = 1/9. use 6 casas após a vígula para 
mostrar os resultados na tabela abaixo das 5 primeiras 
iterações. Considere que a primeira iteração é aquela 
que contem a aproximação inicial obtida para x0.
"""


import numpy as np

# Função dada
f = lambda x: 2*np.sin(np.sqrt(x)) - x

# Método de iteração de ponto fixo
def iteracao_ponto_fixo(f, x0, n_iter):
    print(f"Iteração 0: x0 = {x0:.6f}")
    for i in range(n_iter):
        x0 = f(x0)
        print(f"Iteração {i+1}: x0 = {x0:.6f}")
    return x0

# Valor inicial
x0 = 1/9

# Executar o método para as primeiras 5 iterações
iteracao_ponto_fixo(f, x0, 5)