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
import matplotlib.pyplot as plt

# Dados fornecidos
dias = np.array([0, 4, 8, 12, 16, 20])
mat = np.array([6, 2, 0])
k = np.sum(mat)

quantidade = np.array([67 + k, 84 + k, 98 + k, 125 + k, 149 + k, 185 + k]) * 1e6

# Ajuste exponencial
log_quantidade = np.log(quantidade)

# Regressão linear nos logaritmos para encontrar os coeficientes da exponencial
coefficients = np.polyfit(dias, log_quantidade, 1)
beta = coefficients[0]
log_alpha = coefficients[1]
alpha = np.exp(log_alpha)

print(f"alpha_0: {alpha:.5f}")
print(f"beta_2: {beta:.5f}")



# Plote
plt.scatter(dias, quantidade, label="Dados")
plt.plot(dias, alpha * np.exp(beta * dias), color="red", label="Regressão exponencial")
plt.xlabel("Dias")
plt.ylabel("Quantidade (x 10^6)")
plt.legend()
plt.show()
