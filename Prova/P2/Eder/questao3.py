"""
Se água for drenada de um tanque cilíndrico vertical abrindo-se uma válvula na base, ela escoará
rapidamente quando o tanque estiver cheio e mais lentamente conforme ele continuar a ser drenado.
Como pode ser mostrado, a taxa pela qual o nível de água abaixa é:

dy/dt = -k√y

em que k é uma constante depende da forma do orifício, da área da seção transversal do tanque e do
orifício de drenagem. A profundidade da água y é medida em metros e o tempo t, em minutos. Se k for
igual a 0.06, se o nível  inicial for de 3m, e se considerarmos um
tempo de escoamento equivalente a 7 minutos, determine os três ultimos valores do 
nível do tanque pelo método de Heun com 5 iterações para cada um dos valores de h abaixo:

h = 0.5
h = 0.25

"""

import numpy as np

def dy_dt(y, k=0.06):
    return -k * np.sqrt(y)

def heun_method(y0, t0, tf, h):
    y = y0
    t = t0
    ys = [y0]  # Lista para armazenar os valores de y

    while t < tf:
        y_pred = y + h * dy_dt(y)
        y_corr = y + (h / 2) * (dy_dt(y) + dy_dt(y_pred))
        y = y_corr
        t += h
        ys.append(y)
    
    return ys

# Parâmetros iniciais
y0 = 3
t0 = 0
# tf = 7
tf = 5

# Aplicar o método de Heun para h = 0.5 e h = 0.25
results_h_05 = heun_method(y0, t0, tf, 0.5)
results_h_025 = heun_method(y0, t0, tf, 0.25)

# Obter os três últimos valores para cada h
last_values_h_05 = results_h_05[-3:]
last_values_h_025 = results_h_025[-3:]

print(f"Para h = 0.5: {last_values_h_05}")
print(f"Para h = 0.25: {last_values_h_025}")