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
from scipy.optimize import curve_fit

# Dados
x = np.array([6, 7, 11, 15, 17, 21, 23, 29, 29, 37, 39])
y = np.array([29, 21, 29, 14, 21, 15, 7, 7, 13, 1, 3])

def linear_regression(x, y):
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    return m, c

# Regressão linear direta
m, c = linear_regression(x, y)
print(f"Coeficientes do modelo linear: m = {m}, c = {c}")

# Plot do modelo linear
plt.figure(figsize=(10, 5))
plt.scatter(x, y, color='blue', label='Dados originais')
plt.plot(x, m * x + c, color='red', label='Modelo linear')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regressão Linear')
plt.legend()
plt.show()


# Transformação Exponencial
y_exp = np.log(y)

m_exp, c_exp = linear_regression(x, y_exp)
print(f"Coeficientes do modelo exponencial: m = {m_exp}, c = {c_exp}")

# Plot do modelo exponencial
plt.figure(figsize=(10, 5))
plt.scatter(x, y, color='blue', label='Dados originais')
plt.plot(x, np.exp(m_exp * x + c_exp), color='red', label='Modelo exponencial')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regressão Linear com Transformação Exponencial')
plt.legend()
plt.show()

# Gráfico na escala logarítmica
plt.figure(figsize=(10, 5))
plt.scatter(x, y_exp, color='blue', label='Dados transformados (log(y))')
plt.plot(x, m_exp * x + c_exp, color='red', label='Modelo exponencial (log(y))')
plt.xlabel('x')
plt.ylabel('log(y)')
plt.title('Regressão Linear com Transformação Exponencial (Escala Logarítmica)')
plt.legend()
plt.show()

# Transformação Potência
x_pow = np.log(x)
y_pow = np.log(y)

m_pow, c_pow = linear_regression(x_pow, y_pow)
print(f"Coeficientes do modelo potência: m = {m_pow}, c = {c_pow}")

# Plot do modelo potência
plt.figure(figsize=(10, 5))
plt.scatter(x, y, color='blue', label='Dados originais')
plt.plot(x, np.exp(c_pow) * x ** m_pow, color='red', label='Modelo potência')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regressão Linear com Transformação Potência')
plt.legend()
plt.show()

# Gráfico na escala logarítmica
plt.figure(figsize=(10, 5))
plt.scatter(x_pow, y_pow, color='blue', label='Dados transformados (log(x), log(y))')
plt.plot(x_pow, m_pow * x_pow + c_pow, color='red', label='Modelo potência (log-log)')
plt.xlabel('log(x)')
plt.ylabel('log(y)')
plt.title('Regressão Linear com Transformação Potência (Escala Logarítmica)')
plt.legend()
plt.show()

def saturation_model(x, a, b):
    return a * x / (b + x)

popt_sat, _ = curve_fit(saturation_model, x, y)
a_sat, b_sat = popt_sat
print(f"Coeficientes do modelo de saturação: a = {a_sat}, b = {b_sat}")

# Plot do modelo de saturação
plt.figure(figsize=(10, 5))
plt.scatter(x, y, color='blue', label='Dados originais')
plt.plot(x, saturation_model(x, a_sat, b_sat), color='red', label='Modelo de saturação')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regressão Linear com Transformação de Saturação')
plt.legend()
plt.show()
