import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return np.log10(x) + 3 * np.sin(x / 2)

def false_position_method(func, a, b, tolerance=1e-6, max_iterations=1000):
    if func(a) * func(b) >= 0:
        print("Não é possível garantir que haja uma raiz no intervalo fornecido.")
        return None

    for iteration in range(max_iterations):
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        if np.abs(func(c)) < tolerance:
            return c
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c

    print("O método da falsa posição atingiu o número máximo de iterações.")
    return None

# Intervalo dado [4, 11]
a = 4
b = 11
tolerance = 1e-4  # Erro tolerado

intervals_with_sign_change = []

# Realizando o método da falsa posição em subintervalos do intervalo [4, 11] para encontrar mudanças de sinal
x_values = np.linspace(a, b, 1000)
func_values = func(x_values)

for i in range(len(x_values) - 1):
    if func_values[i] * func_values[i + 1] < 0:
        root = false_position_method(func, x_values[i], x_values[i + 1], tolerance)
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