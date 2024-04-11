"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Assign:
Crie um programa no Python para obter um modelo de
regressão linear múltipla para os dados da Tabela abaixo.
Exiba os coeficientes do modelo.

x_1,i = 0, 2, 2.5, 1, 4, 7
x_2,i = 0, 1, 2, 3, 6, 2
Y     = 6, 11, 9, 1, 3, 27

"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Dataset
x_1 = np.array([0, 2, 2.5, 1, 4, 7])
x_2 = np.array([0, 1, 2, 3, 6, 2])
Y = np.array([6, 11, 9, 1, 3, 27])

# Coeficientes da regressão linear
X = np.array([np.ones(len(x_1)), x_1, x_2]).T
Coeficientes = np.linalg.inv(X.T @ X) @ X.T @ Y

# Coeficientes do modelo
a0, a1, a2 = Coeficientes
print("Coeficientes do modelo:")
print("a0 =", a0)
print("a1 =", a1)
print("a2 =", a2)

# Criação do gráfico 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

# Pontos de dados
ax.scatter(x_1, x_2, Y, color="blue")

# Superfície de regressão
x1_range = np.linspace(min(x_1), max(x_1), num=100)
x2_range = np.linspace(min(x_2), max(x_2), num=100)
x1_range, x2_range = np.meshgrid(x1_range, x2_range)
Z = a0 + a1 * x1_range + a2 * x2_range
ax.plot_surface(x1_range, x2_range, Z, color="red", alpha=0.5)

ax.set_xlabel("x_1")
ax.set_ylabel("x_2")
ax.set_zlabel("Y")

plt.show()
