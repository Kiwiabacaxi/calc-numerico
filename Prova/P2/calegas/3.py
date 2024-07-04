"""
Se a água for drenada de um tanque cilíndrico vertical abrindo-se uma válvula na base, ela escoará
rapidamente quando o tanque estiver cheio e mais lentamente conforme ele continuar a ser drenado.
Como pode ser mostrado, a taxa pela qual o nível de água abaixa é:
dy/dt = -k * sqrt(y)
em que k é uma constante dependente da forma de orifício, da área da seção transversal do tanque e do
orifício de drenagem. A profundidade da água y é medida em metros e o tempo t, em minutos.
Se k for igual ao primeiro valor de "mat" dividido por 100, se o nível inicial for de 3m, e se
considerarmos um tempo de escoamento equivalente ao terceiro valor de 5 + mat(3), determine os três últimos
valores do nível do tanque pelo método de Heun com 5 iterações para cada um dos valores de h abaixo

a) h = 0,5
b) h = 0,25

mat = [6, 3, 0]
"""

import numpy as np

# Definindo os parâmetros
k = 6 / 100
y0 = 3
T = 5
f = lambda t, y: -k * np.sqrt(y)


# Método de Heun
def heun_method(y0, h, steps):
    t = 0
    y = y0
    results = [(t, y)]

    for _ in range(steps):
        t1 = t + h
        y1_predict = y + h * f(t, y)
        y1_correct = y + (h / 2) * (f(t, y) + f(t1, y1_predict))

        t = t1
        y = y1_correct
        results.append((t, y))

    return results


# Aplicando o método de Heun
results_h05 = heun_method(y0, 0.5, 4)
results_h025 = heun_method(y0, 0.25, 4)

# Exibindo os resultados
print("a) h = 0.5")
for t, y in results_h05:
    print(f"t = {t:.2f} | y = {y:.5f}")

print("\nb) h = 0.25")
for t, y in results_h025:
    print(f"t = {t:.2f} | y = {y:.5f}")
