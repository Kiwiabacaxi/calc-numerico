"""
@Carlos Alexandre Sousa Silva

Digits_cpf = 620
mat = [mat(1), mat(2), mat(3)]
mat = [6,2,0]

Assign:
A trajetoria de uma bola pode ser calculada como
y = (tan(theta_0))*x - ((g/2(v_0)^2(cos(theta_0))^2)*x^2) + y_0
onde y é a altura da bola(m), theta_0 é o angulo inicial (em radianos), v_0 é a velocidade inicial (m/s), g = 9.81 (m/s^2) é a constante gravitacional
e y_0 é a altura inicial da bola (m).

Use a busca da razão aurea para determinar a altura maxima, dados y_0 = 1, v_0 = 25 e theta_0 = 0.8726646259971648.

Considere x_1 = 0.8888888888888888
e
x_u = 60.888888888888886

e apresente os resultados das 5 iterações.
Considere que a primeira iteração é aquela que contém os valores iniciais de x_1 e x_u.
Use até 6 casas decimais após a vírgula.

me de um tabela bonitinho que tenha as iterações e os valores de x_1, x_u e a altura máxima estimada.

"""
import numpy as np
import pandas as pd


# Constants
g = 9.81  # gravitational constant in m/s^2
y_0 = 1  # initial height in meters
v_0 = 25  # initial velocity in m/s
theta_0 = 0.8726646259971648  # initial angle in radians

# Function to calculate the height y of the ball at a given x
def calculate_y(x):
    return np.tan(theta_0) * x - (g / (2 * (v_0 ** 2) * (np.cos(theta_0) ** 2))) * x**2 + y_0

# Golden ratio search parameters
x_l = 0.8888888888888888
x_u = 60.888888888888886
phi = (1 + np.sqrt(5)) / 2  # golden ratio

# Variables to hold the search points and heights
iterations = []
x_1 = x_l
x_2 = x_u
h_max_1 = calculate_y(x_1)
h_max_2 = calculate_y(x_2)

# Append initial iteration
iterations.append((x_1, x_2, max(h_max_1, h_max_2)))

# Perform the golden section search for the maximum height
for i in range(1, 5):
    d = (x_2 - x_1) / phi
    x_int_1 = x_2 - d
    x_int_2 = x_1 + d
    h_int_1 = calculate_y(x_int_1)
    h_int_2 = calculate_y(x_int_2)

    if h_int_1 > h_int_2:
        x_2 = x_int_2
        h_max_2 = h_int_2
    else:
        x_1 = x_int_1
        h_max_1 = h_int_1

    # Append each iteration
    iterations.append((x_1, x_2, max(h_max_1, h_max_2)))

# Create a nicely formatted table of the results

# Dataframe for the iterations
df = pd.DataFrame(iterations, columns=['x_1', 'x_u', 'Altura máxima estimada'])
df.index.name = 'Iteração'
df.index += 1  # Start index at 1 for iteration count
df.round(6)  # Round to 6 decimal places

print(df)
