# preciso conferir - sem o uso do erro parece ta mt errado

# use iteração de ponto fixo simples para localizar a raiz de f(x) = 2sen(sqrt(x)) - x
# use a aproximação inicial x0 = (mat(3) + 1) / 9

import numpy as np

tam = 5
mat = np.array([6, 5, 6])

x0 = (mat[2] + 1) / 9
print(x0)

# f(x) = 2sen(sqrt(x)) - x
x = np.inf

# 2*np.sin(np.sqrt(x)) - x

v1 = np.zeros(tam)

i = 0
# Função g1
while i < 5:
    if i == 0:
        x = x0
        # print(x)
        v1[i] = 2 * np.sin(np.sqrt(x)) - x
        # erro_aproximado = abs((v1[i] - x)/(v1[i]))
        i = i + 1

    if i > 0:
        x = v1[i - 1]
        # print(x)
        v1[i] = 2 * np.sin(np.sqrt(x)) - x
        # erro_aproximado = abs((v1[i] - x)/(v1[i]))
        i = i + 1
# else:
# print("Raíz g1 encontrada:", v1[i-1])

print("Primeira função:\n", v1)
# print("Segunda função:\n", v2)
# print("Terceira função:\n", v3)
