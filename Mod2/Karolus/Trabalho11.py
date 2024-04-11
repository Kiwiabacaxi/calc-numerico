"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Assign:
Use a regressão por mínimos quadrados para ajustar uma
reta aos dados da tabela abaixo.

x = np.array([6, 7, 11, 15, 17, 21, 23, 29, 29, 37, 39])
y = np.array([29, 21, 29, 14, 21, 15, 7, 7, 13, 1, 3])

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
import seaborn as sns

# Dataset
x = np.array([6, 7, 11, 15, 17, 21, 23, 29, 29, 37, 39])
y = np.array([29, 21, 29, 14, 21, 15, 7, 7, 13, 1, 3])

# Coeficientes da regressão linear
a1, a0 = np.polyfit(x, y, 1)

# Função linear reg
def linear_regression(x: np.ndarray, a0: float, a1: float) -> np.ndarray:
    return a0 + a1 * x

# Funções de transformação
def exponencial(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.polyfit(x, np.log(y), 1)

def potencia(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.polyfit(np.log(x), np.log(y), 1)

def saturacao(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.polyfit(x, 1 / y, 1)

# Plotar gráficos
plt.figure(figsize=(14, 8))

# Gráfico de regressão linear
plt.subplot(2, 2, 1)
plt.scatter(x, y, color='blue')
plt.plot(x, linear_regression(x, a0, a1), color='red')
plt.title('Regressão Linear')

# Gráfico de transformação exponencial
plt.subplot(2, 2, 2)
a1_exp, a0_exp = exponencial(x, y)
plt.scatter(x, y, color='blue')
plt.plot(x, np.exp(a0_exp) * np.exp(a1_exp * x), color='red')
plt.title('Transformação Exponencial')

# Gráfico de transformação de potência
plt.subplot(2, 2, 3)
a1_pow, a0_pow = potencia(x, y)
plt.scatter(x, y, color='blue')
plt.plot(x, np.exp(a0_pow) * x ** a1_pow, color='red')
plt.title('Transformação de Potência')

# Gráfico de transformação de saturação
plt.subplot(2, 2, 4)
a1_sat, a0_sat = saturacao(x, y)
plt.scatter(x, y, color='blue')
plt.plot(x, 1 / (a0_sat + a1_sat * x), color='red')
plt.title('Transformação de Saturação')

plt.tight_layout()
plt.show()


