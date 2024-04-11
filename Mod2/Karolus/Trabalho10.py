"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Assign:
Use a regressão por mínimos quadrados para ajustar uma
reta aos dados da tabela abaixo.

x 6 7 11 15 17 21 23 29 29 37 39
y 29 21 29 14 21 15 7 7 13 1 3

Construa um programa no Python que determine:
a) O gráfico dos pontos amostrados, juntamente com a reta
obtida na regressão.

b) Os coeficientes a0 e a1 da regressão linear.

c) O coeficiente r2 para o modelo.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset
x = np.array([6, 7, 11, 15, 17, 21, 23, 29, 29, 37, 39])
y = np.array([29, 21, 29, 14, 21, 15, 7, 7, 13, 1, 3])

# Coeficientes da regressão linear
a1, a0 = np.polyfit(x, y, 1)

# Coeficiente de determinação
r2 = np.corrcoef(x, y)[0, 1] ** 2


# Funçao para regressão linear
def linear_regression(x: np.ndarray, a0: float, a1: float) -> np.ndarray:
    return a0 + a1 * x


# Plot - Gráfico de dispersão A)
sns.set_theme("notebook")
plt.figure(figsize=(15, 7))
plt.tight_layout()
plt.scatter(x, y, color="blue")
plt.plot(x, linear_regression(x, a0, a1), color="red")
plt.title("Regressão Linear")

# Adiciona linhas do ponto até a reta
for xi, yi in zip(x, y):
    plt.plot([xi, xi], [yi, a0 + a1 * xi], color="green")

plt.title("Regressão por mínimos quadrados")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# Resultados B) e C)
print(f"Coeficiente a0: {a0}")
print(f"Coeficiente a1: {a1}")
print(f"Coeficiente r2: {r2}")
