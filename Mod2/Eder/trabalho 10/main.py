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
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Dados
x = np.array([6, 7, 11, 15, 17, 21, 23, 29, 29, 37, 39]).reshape((-1, 1))
y = np.array([29, 21, 29, 14, 21, 15, 7, 7, 13, 1, 3])

# Criação do modelo de regressão linear
model = LinearRegression()

# Ajuste do modelo aos dados
model.fit(x, y)

# Coeficientes a0 e a1
a0 = model.intercept_
a1 = model.coef_

# Previsão dos valores de y
y_pred = model.predict(x)

# Coeficiente r2
r2 = r2_score(y, y_pred)

# Gráfico
plt.scatter(x, y, color='blue')
plt.plot(x, y_pred, color='red')
plt.title('Regressão por mínimos quadrados')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

print('a0:', a0)
print('a1:', a1)
print('r2:', r2)