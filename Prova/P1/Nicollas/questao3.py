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
xl = 1.888888
xu = 61.888888

# Chamando a função do método da razão áurea com os valores iniciais e a função definida
golden_ratio_search(f, xl, xu, 5)
