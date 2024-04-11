"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Assign:
Sejam os dados da tabela abaixo:

x 6 7 11 15 17 21 23 29 29 37 39
y 29 21 29 14 21 15 7 7 13 1 3

Construa um programa no Python que aplique sobre a regressão
linear as três transformações de dados: exponencial, potência e
saturação. Para cada transformação exiba os seguintes resultados:

a) Coeficientes do modelo.

b) Gráfico na escala original.

c) Gráfico na escala logarítmica para as transformações
exponencial e potência.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit

# Dados
x = np.array([6, 7, 11, 15, 17, 21, 23, 29, 29, 37, 39]).reshape((-1, 1))
y = np.array([29, 21, 29, 14, 21, 15, 7, 7, 13, 1, 3])

# Funções para as transformações
def exp_func(x, a, b):
    return a * np.exp(b * x)

def power_func(x, a, b):
    return a * np.power(x, b)

def saturation_func(x, a, b):
    return a * x / (b + x)

# Ajuste dos modelos
popt_exp, _ = curve_fit(exp_func, x.flatten(), y)
popt_power, _ = curve_fit(power_func, x.flatten(), y)
popt_saturation, _ = curve_fit(saturation_func, x.flatten(), y)

# Previsão dos valores de y
y_pred_exp = exp_func(x, *popt_exp)
y_pred_power = power_func(x, *popt_power)
y_pred_saturation = saturation_func(x, *popt_saturation)

# Gráficos
fig, axs = plt.subplots(3, 2, figsize=(10, 15))

# Exponencial
axs[0, 0].scatter(x, y, color='blue')
axs[0, 0].plot(x, y_pred_exp, color='red')
axs[0, 0].set_title('Exponencial - Escala Original')

axs[0, 1].scatter(x, np.log(y), color='blue')
axs[0, 1].plot(x, np.log(y_pred_exp), color='red')
axs[0, 1].set_title('Exponencial - Escala Logarítmica')

# Potência
axs[1, 0].scatter(x, y, color='blue')
axs[1, 0].plot(x, y_pred_power, color='red')
axs[1, 0].set_title('Potência - Escala Original')

axs[1, 1].scatter(x, np.log(y), color='blue')
axs[1, 1].plot(x, np.log(y_pred_power), color='red')
axs[1, 1].set_title('Potência - Escala Logarítmica')

# Saturação
axs[2, 0].scatter(x, y, color='blue')
axs[2, 0].plot(x, y_pred_saturation, color='red')
axs[2, 0].set_title('Saturação - Escala Original')

plt.tight_layout()
plt.show()

print('Coeficientes Exponencial:', popt_exp)
print('Coeficientes Potência:', popt_power)
print('Coeficientes Saturação:', popt_saturation)