import numpy as np
import matplotlib.pyplot as plt

def dydt(t, y):
    return y * t**3 - 1.5 * y

def midpoint_method(dydt, t0, y0, h, n):
    t_values = [t0]
    y_values = [y0]
    t = t0
    y = y0
    for _ in range(n):
        k1 = h * dydt(t, y)
        k2 = h * dydt(t + 0.5*h, y + 0.5*k1)
        y += k2
        t += h
        t_values.append(t)
        y_values.append(y)
    return t_values, y_values

# Solicitando o valor de h ao usuário
h = float(input("Digite o valor de h: "))
n = int(4 / h)

# Calculando y para o intervalo de t de 0 a 4
t_values, y_values = midpoint_method(dydt, 0, 1, h, n)

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(t_values, y_values, '-o', label='Método do Ponto Médio')
plt.title('Solução do Problema de Valor Inicial')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)
plt.show()