"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Assign:
Crie um programa no PYTHON para encontrar raízes
pelo método da secante em relação a função

f(x) = sin (x/2) * log10(-10x)

com aproximação inicial – 8 e fator de perturbação
igual a 10– 6.

erro aceito de 0,0001

"""

import numpy as np

# Define a função dada no exercício
def f(x):
    return np.sin(x / 2) * np.log10(-10 * x)

# Define o método da secante
def secant_method(f, x0, x1, tol=1e-4, max_iterations=100):
    for i in range(max_iterations):
        fx0 = f(x0)
        fx1 = f(x1)
        if fx1 - fx0 == 0:
            return None, i  # Pode ocorrer uma divisão por zero se fx1 == fx0
        
        # Calcula a próxima aproximação
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        
        # Verifica a condição de parada
        if abs(x2 - x1) < tol:
            return x2, i
        
        x0, x1 = x1, x2  # Prepara para a próxima iteração

    return None, max_iterations  # Não encontrou a raiz dentro do número máximo de iterações

def secant_method_with_error(f, x0, x1, error_tol=1e-4):

    x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))

    while abs(f(x2)) > error_tol:

        x0, x1 = x1, x2

        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))

    return x2



# Aproximação inicial e fator de perturbação
x0 = -8
x1 = x0 * (1 + 1e-6)

# Encontrar a raiz usando o método da secante
root, iterations = secant_method(f, x0, x1)

root, iterations
print(f"Raiz encontrada: {root}")

# Aplicando o método da secante com o critério de parada baseado no erro máximo.

root_with_error = secant_method_with_error(f, x0, x1)
root_with_error

print(f"Raiz encontrada com erro máximo: {root_with_error}")