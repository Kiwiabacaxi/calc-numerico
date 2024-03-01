import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return np.log10(x) + 3 * np.sin(x / 2)

def bisection_method(func, a, b, tolerance=1e-6):
    if func(a) * func(b) >= 0:
        print("Não é possível garantir que haja uma raiz no intervalo fornecido.")
        return None

    while (b - a) / 2 > tolerance:
        midpoint = (a + b) / 2
        if func(midpoint) == 0:
            return midpoint
        elif func(a) * func(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint

    return (a + b) / 2

# Intervalo dado [4, 11]
a = 4
b = 11
tolerance = 1e-4  # Erro tolerado

intervals_with_sign_change = []

# Realizando a bisseção em subintervalos do intervalo [4, 11] para encontrar mudanças de sinal
x_values = np.linspace(a, b, 100)
func_values = func(x_values)

for i in range(len(x_values) - 1):
    if func_values[i] * func_values[i + 1] < 0:
        root = bisection_method(func, x_values[i], x_values[i + 1], tolerance)
        if root:
            intervals_with_sign_change.append((x_values[i], x_values[i + 1]))
            print(f"Raiz encontrada no subintervalo [{x_values[i]}, {x_values[i + 1]}]: {root}")

print("\nSubintervalos com mudança de sinal:")
for interval in intervals_with_sign_change:
    print(interval)

x = np.linspace(a, b, 100)
y = func(x)

plt.plot(x, y, label='f(x)')
plt.grid(True)
plt.show()