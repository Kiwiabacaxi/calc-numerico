"""
@Carlos Alexandre Sousa Silva

Digits_cpf = 620
mat = [mat(1), mat(2), mat(3)]
mat = [6,2,0]

Assign:
Resolva essa questao em python usando no maximo numpy

Se agua for drenada de um tanque cilindrico vertical abrindo-se uma valvula na base, ela escoara rapidamente quando o tanque estiver cheio e mais lentamente conforme ele continuar a ser drenado.
Como pode ser mostrado, a taxa pela qual o nivel de agua abaixa é:

dy/dt = -k√y

em que k é uma constante dependente da forma do orificio, da area da seção transversal do tanque e do orificio de drenagem. 
A profundidade da agua y é medida em metros e o tempo t, em minutos. 
Se k for igual ao primeiro valor de mat divido por 100, se o nivel inicial for de 3m, 
e se considerarmos um tempo de escoamento equivalente ao terceiro valor de 5 + mat(3), 
determine os tres ultimos valores do nivel do tanque pelo metodo de Heun com 5 iteracoes para cada um dos valores de h abaixo:

a) h = 0.5
b) h = 0.25

"""

import numpy as np
from scipy.integrate import solve_ivp

# Valores fornecidos
mat = np.array([6, 2, 0])
k = mat[0] / 100
y0 = 3.0
t_end = 5 + mat[2]

# Função para dy/dt
def dydt(t, y):
    return -k * np.sqrt(y)

# Método de Heun usando solve_ivp
def heun_scipy(y0, t_end, h, k):
    t_span = (0, t_end)
    t_eval = np.arange(0, t_end + h, h)
    
    sol = solve_ivp(dydt, t_span, [y0], method='RK23', t_eval=t_eval)
    
    return sol.y[0][-3:]  # Últimos três valores

# Valores para h
h_values = [0.5, 0.25]

# Calcular para h = 0.5
result_h_0_5 = heun_scipy(y0, t_end, h_values[0], k)
print(f"Últimos três valores do nível do tanque para h = 0.5: {result_h_0_5}")

# Calcular para h = 0.25
result_h_0_25 = heun_scipy(y0, t_end, h_values[1], k)
print(f"Últimos três valores do nível do tanque para h = 0.25: {result_h_0_25}")
