"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Assign:
Crie um programa no Python para determinar os coeficientes
do polinômio interpolador de Newton, para uma ordem
qualquer especificada pelo usuário. Use o programa para
determinar:
a) Os coeficientes do polinômio interpolador de Newton de 3ª
ordem dos seguintes dados:
   x = [8, 9, 10, 11, 12, 13]
   f(x) = [400, 900, 1500, 2250, 3200, 4400]
b) Estime f(11,8).
"""


def divided_differences(x, y):
    n = len(y)
    coef = [y[0]]
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            y[i] = float(y[i] - y[i - 1]) / float(x[i] - x[i - j])
        coef.append(y[j])
    return coef


def newton_polynomial(x, coef, value):
    n = len(coef) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (value - x[n - k]) * p
    return p


# Dados fornecidos
x = [8, 9, 10, 11, 12, 13]
y = [400, 900, 1500, 2250, 3200, 4400]

# Calculando os coeficientes do polinômio de Newton
coef = divided_differences(x, y)

# Estimando f(11.8)
value = 11.8
estimated_value = newton_polynomial(x, coef, value)

print("Coeficientes do polinômio interpolador de Newton:", coef)
print(f"Estimativa de f({value}):", estimated_value)
