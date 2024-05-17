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

# Dados fornecidos
x = np.array([6, 7, 11, 15, 17, 21, 23, 29, 29, 37, 39])
y = np.array([29, 21, 29, 14, 21, 15, 7, 7, 13, 1, 3])


# Função para calcular a regressão linear usando mínimos quadrados
def linear_regression(x, y):
    """
    Realiza uma regressão linear nos dados fornecidos.

    Args:
        x (numpy.ndarray): O array de valores x.
        y (numpy.ndarray): O array de valores y correspondentes.

    Returns:
        tuple: Retorna um par de coeficientes (m, c) da linha de regressão y = mx + c.
    """
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    return m, c


# Regressão linear simples
m, c = linear_regression(x, y)
y_pred = m * x + c

# Transformação Exponencial
m_exp, c_exp = linear_regression(x, np.log(y))
y_pred_exp = np.exp(m_exp * x + c_exp)

# Transformação de Potência
m_pow, c_pow = linear_regression(np.log(x), np.log(y))
y_pred_pow = np.exp(m_pow * np.log(x) + c_pow)

# Transformação de Saturação (inversa)
m_inv, c_inv = linear_regression(x, 1 / y)
y_pred_inv = 1 / (m_inv * x + c_inv)

# a) Printar Coeficientes dos modelos
print(f"Coeficientes da Regressão Linear: m = {m:.5f}, c = {c:.5f}")
print(f"Coeficientes da Transformação Exponencial: m = {m_exp:.5f}, c = {c_exp:.5f}")
print(f"Coeficientes da Transformação de Potência: m = {m_pow:.5f}, c = {c_pow:.5f}")
print(f"Coeficientes da Transformação de Saturação: m = {m_inv:.5f}, c = {c_inv:.5f}")

# Plotando os gráficos
# fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig, axs = plt.subplots(3, 2, figsize=(12, 8))

# b) Gráfico na escala original. (Linear, Exponencial, Potência, Saturação)
# Grafico Linear
axs[0, 0].scatter(x, y, label="Dados Originais")
axs[0, 0].plot(x, y_pred, color="red", label="Regressão Linear")
axs[0, 0].set_title("Regressão Linear")

# Grafico Exponencial
axs[0, 1].scatter(x, y, label="Dados Originais")
axs[0, 1].plot(x, y_pred_exp, color="red", label="Transformação Exponencial")
axs[0, 1].set_title("Transformação Exponencial")

# Grafico Potência
axs[1, 0].scatter(x, y, label="Dados Originais")
axs[1, 0].plot(x, y_pred_pow, color="red", label="Transformação de Potência")
axs[1, 0].set_title("Transformação de Potência")

# Grafico Saturação
axs[1, 1].scatter(x, y, label="Dados Originais")
axs[1, 1].plot(x, y_pred_inv, color="red", label="Transformação de Saturação")
axs[1, 1].set_title("Transformação de Saturação")

# c) Gráfico na escala logarítmica para as transformações exponencial e potência.

# Grafico Exponencial
axs[2, 0].scatter(x, np.log(y), label="Dados Originais")
axs[2, 0].plot(x, m_exp * x + c_exp, color="red", label="Transformação Exponencial")
axs[2, 0].set_title("Transformação Exponencial (Log)")
axs[2, 0].set_yscale("log")
axs[2, 0].set_xscale("log")

# Grafico Potência
axs[2, 1].scatter(np.log(x), np.log(y), label="Dados Originais")
axs[2, 1].plot(
    np.log(x), m_pow * np.log(x) + c_pow, color="red", label="Transformação de Potência"
)
axs[2, 1].set_title("Transformação de Potência (Log)")
axs[2, 1].set_xscale("log")
axs[2, 1].set_yscale("log")


plt.tight_layout()
plt.show()
