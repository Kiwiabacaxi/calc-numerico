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
xl = 0.8888888888888888
xu = 60.888888888888886

# Chamando a função do método da razão áurea com os valores iniciais e a função definida
golden_ratio_search(f, xl, xu, 5)
