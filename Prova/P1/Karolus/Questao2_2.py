"""
@Carlos Alexandre Sousa Silva

Digits_cpf = 620
mat = [mat(1), mat(2), mat(3)]
mat = [6,2,0]

Assign:
Use a iteraçao de ponto fixo simples para localizar a raiz de f(x) = 2*sin(sqrt(x)) - x
Use  a aproximaçao inicial x0 = 0.1111111111111111
Use 6 casas decimais apos a virgula para mostrar os resultados na tabela abaixo das 5 primeiras iteraçoes.
Considere que a primeira iteraçao é aquela que contém a aproximaçao inicial obtida para x0.

me de uma tabela formatadinha que tenha as iteraçoes e a raiz estimada
lembrando que a primeira iteraçao é 0.1111111111111111 e a raiz é 1.9723810010822, entao so tem que descobrir a iteraçao 2, 3 e 4
"""
import numpy as np

# Definindo a função fornecida
def f(x):
    return 2 * np.sin(np.sqrt(x)) - x

# Definindo a função de iteração para o método de ponto fixo
# Usaremos a função g(x) = 2 * sin(sqrt(x))
def g(x):
    return 2 * np.sin(np.sqrt(x))

# Valor inicial
x0 = 0.1111111111111111

# Realizando as iterações
iterations = [x0]
for _ in range(4):  # Inclui o x0 como iteração 0 e executa mais 4 iterações
    next_x = g(iterations[-1])
    iterations.append(next_x)

# Formatando a tabela de saída
table = "Iteração | Raiz Estimada\n" + "-"*27 + "\n"
table += "\n".join(f"{i}         | {iterations[i]:.6f}" for i in range(5))

print(table)
