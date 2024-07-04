"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Trabalho 25:
Um reator de batelada pode ser descrito pelas seguintes equações:
dC/dt = -e^(-10/(T+273)) * C
dT/dt = 1000 * e^(-10/(T+273)) * C - 10 * (T - 20)
onde C é a concentração do reagente e T é a temperatura do reator.
A princípio, o reator está a 16°C e tem uma concentração do reagente C de 1,0 gmol/L.
Encontre a concentração e a temperatura do reator no tempo t de 0 a 4 usando o método de Runge-Kutta de quarta ordem clássico para a resolução do sistema de EDOs. Use h = 0,25.
"""

import numpy as np


def dCdt(C, T):
    return -np.exp(-10 / (T + 273)) * C


def dTdt(C, T):
    return 1000 * np.exp(-10 / (T + 273)) * C - 10 * (T - 20)


def runge_kutta_4th_system(dCdt, dTdt, t0, C0, T0, h, t_end):
    t_values = np.arange(t0, t_end + h, h)
    C_values = np.zeros(len(t_values))
    T_values = np.zeros(len(t_values))
    C_values[0] = C0
    T_values[0] = T0

    for i in range(1, len(t_values)):
        t = t_values[i - 1]
        C = C_values[i - 1]
        T = T_values[i - 1]

        k1_C = h * dCdt(C, T)
        k1_T = h * dTdt(C, T)

        k2_C = h * dCdt(C + 0.5 * k1_C, T + 0.5 * k1_T)
        k2_T = h * dTdt(C + 0.5 * k1_C, T + 0.5 * k1_T)

        k3_C = h * dCdt(C + 0.5 * k2_C, T + 0.5 * k2_T)
        k3_T = h * dTdt(C + 0.5 * k2_C, T + 0.5 * k2_T)

        k4_C = h * dCdt(C + k3_C, T + k3_T)
        k4_T = h * dTdt(C + k3_C, T + k3_T)

        C_values[i] = C + (k1_C + 2 * k2_C + 2 * k3_C + k4_C) / 6
        T_values[i] = T + (k1_T + 2 * k2_T + 2 * k3_T + k4_T) / 6

    return t_values, C_values, T_values


# Valores padrão
t0 = 0
C0 = 1.0
T0 = 16
# h = 0.25
h = float(input("Digite o valor de h: "))
t_end = 4

# Resolvendo o sistema de EDOs usando o método de Runge-Kutta de quarta ordem
t_values, C_values, T_values = runge_kutta_4th_system(dCdt, dTdt, t0, C0, T0, h, t_end)

# Exibindo os resultados
for t, C, T in zip(t_values, C_values, T_values):
    print(f"t = {t:.2f}, C = {C:.5f} gmol/L, T = {T:.5f} °C")
