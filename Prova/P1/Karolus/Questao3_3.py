import numpy as np

# Definindo a função fornecida
def f(x, theta_0=0.8726646259971648, v_0=25, g=9.81, y_0=1):
    return (np.tan(theta_0))*x - ((g/(2*v_0**2*(np.cos(theta_0))**2))*x**2) + y_0

# Valores iniciais
xl = 0.8888888888888888
xu = 60.888888888888886

# Constante da razão áurea
phi = (1 + np.sqrt(5)) / 2

# Função de busca da razão áurea
def razao_aurea(f, xl, xu, erro, phi):
    d = (phi - 1) * (xu - xl)
    x1 = xl + d
    x2 = xu - d

    res1 = f(x1)
    res2 = f(x2)

    iterations = [(xl, xu, max(res1, res2))]

    for _ in range(4):  # Inclui o xl e xu como iteração 0 e executa mais 4 iterações
        if res1 > res2:
            xl = x1
            d = (phi - 1) * (xu - xl)
            x1 = xl + d
            res1 = f(x1)
        else:
            xu = x2
            d = (phi - 1) * (xu - xl)
            x2 = xu - d
            res2 = f(x2)
        iterations.append((xl, xu, max(res1, res2)))

    return iterations

# Realizando as iterações
iterations = razao_aurea(f, xl, xu, 1e-6, phi)

# Formatando a tabela de saída
table = "Iteração | xl        | xu        | Altura Máxima\n" + "-"*50 + "\n"
table += "\n".join(f"{i}         | {iterations[i][0]:.6f} | {iterations[i][1]:.6f} | {iterations[i][2]:.6f}" for i in range(5))

print(table)