"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador
"""

import numpy as np

# Definindo as funções para as derivadas
def dCdt(C, T):
    return -np.exp(-10/(T+273)) * C

def dTdt(C, T):
    return 1000 * np.exp(-10/(T+273)) * C - 10 * (T - 20)

# Método de Runge-Kutta de quarta ordem
def runge_kutta(C0, T0, t0, tf, h):
    n = int((tf - t0) / h)
    t = t0
    C = C0
    T = T0
    
    for _ in range(n):
        k1_C = h * dCdt(C, T)
        k1_T = h * dTdt(C, T)
        
        k2_C = h * dCdt(C + 0.5 * k1_C, T + 0.5 * k1_T)
        k2_T = h * dTdt(C + 0.5 * k1_C, T + 0.5 * k1_T)
        
        k3_C = h * dCdt(C + 0.5 * k2_C, T + 0.5 * k2_T)
        k3_T = h * dTdt(C + 0.5 * k2_C, T + 0.5 * k2_T)
        
        k4_C = h * dCdt(C + k3_C, T + k3_T)
        k4_T = h * dTdt(C + k3_C, T + k3_T)
        
        C += (k1_C + 2*k2_C + 2*k3_C + k4_C) / 6
        T += (k1_T + 2*k2_T + 2*k3_T + k4_T) / 6
        t += h
        
        print(f"t = {t:.2f}, C = {C:.4f}, T = {T:.4f}")

# Parâmetros iniciais
C0 = 1.0  # gmol/L
T0 = 16   # °C
t0 = 0    # Tempo inicial
tf = 4    # Tempo final
h = 0.25  # Passo

runge_kutta(C0, T0, t0, tf, h)