"""
@Carlos Alexandre Sousa Silva

Digits_cpf = 620
mat = [mat(1), mat(2), mat(3)]
mat = [6,2,0]

Assign:
Resolva essa questao em python usando no maximo numpy

Considere que k seja a soma de todos os valores de mat.
Os dados a seguir representam o crescimento bacteriologico em uma cultura liquida durante certo numero de dias
dia                     0       4       8       12      16      20
Quantidade * 10ˆ6       67+k    84+k    98+k    125+k   149+k   185+k

Para a regressao pelo modelo exponencial, determine os seguintes coeficientes:
A) alpha_0
B) beta_2

"""

import numpy as np

# Dados fornecidos
mat = [6, 2, 0]
k = sum(mat)

dias = np.array([0, 4, 8, 12, 16, 20])
quantidade = np.array([67, 84, 98, 125, 149, 185]) + k

# Aplicando logaritmo natural para linearizar o modelo exponencial
log_quantidade = np.log(quantidade)

# Calculando os parâmetros da regressão linear
n = len(dias)
sum_x = np.sum(dias)
sum_y = np.sum(log_quantidade)
sum_xx = np.sum(dias * dias)
sum_xy = np.sum(dias * log_quantidade)

beta_2 = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)
log_alpha_0 = (sum_y - beta_2 * sum_x) / n
alpha_0 = np.exp(log_alpha_0)

print(f"alpha_0: {alpha_0}")
print(f"beta_2: {beta_2}")
