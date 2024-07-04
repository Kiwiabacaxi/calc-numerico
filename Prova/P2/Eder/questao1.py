"""
Considere que K = 8 seja a soma de todos os valores de mat. Os dados a seguir representam o crescimento bacteriológico em uma cultura líquida durante certo número de dias.

Dia:                  0   |    4   |    8   |    12   |   16    |    20
Quantidade x 10^6: 67 + k | 84 + k | 98 + k | 125 + k | 149 + k | 185 + k

Para a regressão pelo modelo exponencial, determine os seguintes coeficientes:
a) a0
b) B2
"""

import numpy as np
from scipy import stats

# Dados fornecidos
k = 8
dias = np.array([0, 4, 8, 12, 16, 20])
quantidades = np.array([(67 + k), (84 + k), (98 + k), (125 + k), (149 + k), (185 + k)])

# Transformar os dados para o modelo linearizado
y_ln = np.log(quantidades)  # Aplicando logaritmo natural

# Realizar regressão linear
slope, intercept, r_value, p_value, std_err = stats.linregress(dias, y_ln)

# Converter intercepto para a
a = np.exp(intercept)

# slope é diretamente o coeficiente b, que pode ser relacionado a B2 conforme necessário
b = slope

# Resultados
a0 = a
B2 = b  # A relação exata entre b e B2 depende da definição de B2 no contexto

print(f"a) a0 = {a0:.6f}")
print(f"b) B2 = {B2:.6f}")