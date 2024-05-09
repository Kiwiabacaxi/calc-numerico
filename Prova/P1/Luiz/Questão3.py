"""
A trajetória de uma bola pode ser calculada como
y = (tg(θ))x - (g/(2v²cos²(θ)))x² + y0
onde y é a altura (m), θ é o ângulo inicial (em radianos)
v é a velocidade inicial (m/s), g = 9.81 m/s² é a constante gravitacional
e y0 é a altura inicial (m). Use a busca da razão áurea para determinar a altura máxima
dados y0 = 1m, v = 25 m/s e θ = 50° rad.
Considere xl = 0,888888889m e xu = 60,888888889m
e apresente os resultados das 5 iterações, sendo xl, xu e máximo estimado para cada iteração.
Use até 6 casas decimais após a vírgula.
"""

import math

# Definindo a função dada
def f(x):
    g = 9.81
    v = 25
    theta = math.radians(50)
    y0 = 1
    return (math.tan(theta)*x) - ((g/(2*v**2*math.cos(theta)**2))*x**2) + y0

# Definindo a função para o método da razão áurea
def golden_ratio_search(f, xl, xu, iterations):
    phi = (1 + math.sqrt(5)) / 2
    for i in range(iterations):
        d = (phi - 1) * (xu - xl)
        x1 = xl + d
        x2 = xu - d
        if f(x1) > f(x2):
            xl = x2
        else:
            xu = x1
        print(f"Iteração {i+1}: xl = {xl:.6f}, xu = {xu:.6f}, máximo estimado = {f(xl):.6f}")

# Inicializando os valores dados
xl = 0.666666667
xu = 60.666666667

# Chamando a função do método da razão áurea com os valores iniciais e a função definida
golden_ratio_search(f, xl, xu, 5)