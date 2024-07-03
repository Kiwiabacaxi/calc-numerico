import numpy as np
import matplotlib.pyplot as plt

def dydt(t, y):
    return y * t**3 - 1.5 * y

def runge_kutta_4th(dydt, t0, y0, h, n):
    t_values = [t0]
    y_values = [y0]
    t = t0
    y = y0
    for _ in range(n):
        k1 = h * dydt(t, y)
        k2 = h * dydt(t + 0.5*h, y + 0.5*k1)
        k3 = h * dydt(t + 0.5*h, y + 0.5*k2)
        k4 = h * dydt(t + h, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        t += h
        t_values.append(t)
        y_values.append(y)
    return t_values, y_values

# Solicitando o valor de h ao usuário
h = float(input("Digite o valor de h: "))
n = int(4 / h)

# Calculando y para o intervalo de t de 0 a 4
t_values, y_values = runge_kutta_4th(dydt, 0, 1, h, n)

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(t_values, y_values, '-o', label='Método de Runge-Kutta de 4ª Ordem')
plt.title('Solução do Problema de Valor Inicial')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)
plt.show()