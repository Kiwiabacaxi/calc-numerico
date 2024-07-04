"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Trabalho 16:
Considerando o trabalho 15, determine o x para o qual f(x) = 15.
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


def derivative_lagrange(x, y, value, h=1e-5):
    """
    Calcula a derivada do polinômio interpolador de Lagrange no ponto especificado usando diferenças finitas.

    Parâmetros:
    x (list): Lista de valores de x.
    y (list): Lista de valores de y correspondentes aos valores de x.
    value (float): O ponto no qual a derivada deve ser avaliada.
    h (float): Um pequeno incremento para calcular a derivada (opcional, padrão é 1e-5).

    Retorna:
    deriv (float): O valor da derivada no ponto especificado.
    """
    return (
        lagrange_interpolation(x, y, value + h)
        - lagrange_interpolation(x, y, value - h)
    ) / (2 * h)


def newton_raphson(x, y, target, initial_guess=0.0, tol=1e-8, max_iter=100):
    """
    Encontra a raiz do polinômio interpolador de Lagrange usando o método de Newton-Raphson.

    Parâmetros:
    x (list): Lista de valores de x.
    y (list): Lista de valores de y correspondentes aos valores de x.
    target (float): O valor alvo para o qual desejamos encontrar a raiz f(x) = target.
    initial_guess (float): O valor inicial para o método de Newton-Raphson (opcional, padrão é 0.0).
    tol (float): A tolerância para o critério de parada (opcional, padrão é 1e-8).
    max_iter (int): O número máximo de iterações (opcional, padrão é 100).

    Retorna:
    root (float): O valor de x para o qual f(x) = target.
    """
    x0 = initial_guess
    for _ in range(max_iter):
        f_value = lagrange_interpolation(x, y, x0) - target
        f_derivative = derivative_lagrange(x, y, x0)
        if abs(f_value) < tol:
            return x0
        if f_derivative == 0:
            raise ValueError("Derivada zero. O método de Newton-Raphson falhou.")
        x0 = x0 - f_value / f_derivative
    raise ValueError(
        "Número máximo de iterações alcançado. O método de Newton-Raphson falhou."
    )


# Dados fornecidos
x = [-1, 0, 1, 2]
y = [17, 14, 10, 40]

# Valor alvo
target_value = 15

# Encontrando o x para o qual f(x) = 15
try:
    root = newton_raphson(x, y, target_value, initial_guess=0.5)
    print(f"O valor de x para o qual f(x) = {target_value} é aproximadamente: {root}")
except ValueError as e:
    print(e)
