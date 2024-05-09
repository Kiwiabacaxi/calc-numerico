"""
@Carlos Alexandre Sousa Silva

Digits_cpf = 620
mat = [mat(1), mat(2), mat(3)]
mat = [6,2,0]

Assign:
O seguinte sistema de esquações é projetado para determinar as concentrações (os c's em g/m³) em uma série de 
reatores acoplados como função da quantidade de entrada da massa em cada reator (o lado direito está em g/dia),

15c1 - 3c2 - c3 = 3818
-3c1 + 18c2 - 6c3 = 1206
-4c1 - c2 + 12c3 = 2350

Considere a aproximação inicial (0,0,0) e obtenha as 3 primeiras iterações da resolução desse problema pelo método
da itereação de Gauss-Jacobi. A primeira iteração é aquela que considera a aproximação inicial.
Mostre os valores de c1, c2 e c3 para cada iteração.

me de uma tabela bonitinha que tenha as iteraçoes de 1 a 3, o c1, c2 e c3 de cada iteração

"""

import numpy as np
import pandas as pd

# Coeficientes da matriz A do sistema Ax = b
A = np.array([
    [15, -3, -1],
    [-3, 18, -6],
    [-4, -1, 12]
])

# Vetor b do lado direito das equações
b = np.array([3818, 1206, 2350])

# Número de iterações
n_iterations = 3

# Vetor de aproximações iniciais (x_0)
x = np.zeros(3)

# Estrutura para armazenar as iterações
results = []

# Método de Gauss-Jacobi
for _ in range(n_iterations):
    new_x = np.zeros_like(x)
    for i in range(A.shape[0]):
        sum_ = np.dot(A[i], x) - A[i, i] * x[i]
        new_x[i] = (b[i] - sum_) / A[i, i]
    results.append(new_x.copy())
    x = new_x

# Criando um DataFrame para apresentar os resultados
df_results = pd.DataFrame(results, columns=['c1', 'c2', 'c3'])
df_results.index = np.arange(1, n_iterations + 1)  # ajustando a indexação para começar de 1
df_results.index.name = 'Iteração'
print(df_results)