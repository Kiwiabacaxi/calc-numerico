import numpy as np
import matplotlib.pyplot as plt

# Definindo a função e a regra 1/3 de Simpson
def f(x):
    return 6 + 3 * np.cos(x)

def simpson_one_third_rule(a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)

    for i in range(1, n):
        if i % 2 == 0:
            s += 2 * f(a + i * h)
        else:
            s += 4 * f(a + i * h)

    return h / 3 * s

# Solicitando os dados do usuário
a = float(input("Digite o limite inferior do intervalo de integração: "))
b = float(input("Digite o limite superior do intervalo de integração: "))
n = int(input("Digite a quantidade de intervalos: "))

# Calculando a integral
integral = simpson_one_third_rule(a, b, n)

# Criando o gráfico
x = np.linspace(a, b, 1000)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = 6 + 3cos(x)')
plt.fill_between(x, y, color='gray', alpha=0.5, label=f'Integral = {integral:.2f}')
plt.legend()
plt.grid(True)
plt.title('Gráfico da função e sua integral')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()