"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Trabalho 15:
Crie um programa no Python para determinar os coeficientes
do polinômio interpolador de Lagrange, para uma ordem
qualquer especificada pelo usuário. Use o programa para
determinar:
a) O valor de f(1,5) considerando os dados abaixo:
   x = [-1, 0, 1, 2]
   f(x) = [17, 14, 10, 40]
"""


def lagrange_interpolation(x, y, value):
    """
    Calcula o polinômio interpolador de Lagrange e estima o valor da função no ponto especificado.

    Parâmetros:
    x (list): Lista de valores de x.
    y (list): Lista de valores de y correspondentes aos valores de x.
    value (float): O ponto no qual a função deve ser avaliada.

    Retorna:
    result (float): O valor estimado da função no ponto especificado.
    """
    n = len(x)
    result = 0.0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (value - x[j]) / (x[i] - x[j])
        result += term
    return result


# Dados fornecidos
x = [-1, 0, 1, 2]
y = [17, 14, 10, 40]

# Estimando f(1,5)
value = 1.5
estimated_value = lagrange_interpolation(x, y, value)

print(f"Estimativa de f({value}):", estimated_value)
