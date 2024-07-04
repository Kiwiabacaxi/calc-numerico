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

# Função que define a EDO
def dydt(t, y):
    return -k * np.sqrt(y)

# Implementação do método de Heun com iteração
def heun_method(dydt, t0, y0, h, t_end, tol=1e-6, max_iter=10):
    t_values = np.arange(t0, t_end + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0

    for i in range(1, min(len(t_values), iterations + 1)):
        k1 = dydt(t_values[i - 1], y_values[i - 1])
        y_predict = y_values[i - 1] + h * k1
        k2 = dydt(t_values[i], y_predict)
        y_corrected = y_values[i - 1] + (h / 2) * (k1 + k2)

        iter_count = 0
        while np.abs(y_corrected - y_predict) > tol and iter_count < max_iter:
            y_predict = y_corrected
            k2 = dydt(t_values[i], y_predict)
            y_corrected = y_values[i - 1] + (h / 2) * (k1 + k2)
            iter_count += 1

        y_values[i] = y_corrected

    return t_values[:iterations + 1], y_values[:iterations + 1]

# Valores fornecidos
mat = np.array([6, 2, 0])
k = mat[0] / 100
y0 = 3.0
t_end = 5 + mat[2]
iterations = 5

# Valores para h
h_values = [0.5, 0.25]

for h in h_values:
    print(f"Resultados para h = {h}:")
    t_values, y_values = heun_method(dydt, 0, y0, h, t_end)
    # Exibindo os últimos três valores
    for t, y in zip(t_values[-3:], y_values[-3:]):
        print(f"t = {t:.2f}, y = {y:.5f}")
    print("\n")

