import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return np.log10(x) + 3 * np.sin(x / 2)

def incremental_search(func, a, b, num_subintervals):
    subinterval_width = (b - a) / num_subintervals

    x_values = np.linspace(a, b, num_subintervals + 1)
    func_values = func(x_values)

    intervals = []

    for i in range(num_subintervals):
        if func_values[i] * func_values[i + 1] < 0:
            intervals.append((x_values[i], x_values[i + 1]))

    return intervals

# Intervalo dado [4, 11]
a = 4
b = 11
num_subintervals = 100  # Número de subintervalos

intervals_with_sign_change = incremental_search(func, a, b, num_subintervals)
print("Subintervalos com mudança de sinal:")
for interval in intervals_with_sign_change:
    print(interval)
    
# Plot
x = np.linspace(a, b, 100)
y = func(x)

plt.plot(x, y, label='f(x)')
plt.grid(True)
plt.show()

