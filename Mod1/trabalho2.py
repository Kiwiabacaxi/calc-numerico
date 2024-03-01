"""
@Antonio
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Assign:
Crie uma função no Python para estimar raízes pelo
método da bisseção. O erro tolerado para conclusão do
treinamento e de 0,0001. Use essa função para identificar os
subintervalos nos quais ocorre mudança de sinal
dentro do intervalo [4,11] para a função abaixo. Envie
o trabalho para o e-mail josericardo@iftm.edu.br.

Trabalho 2 = 0,0001 # erro maximo tolerado

f(x) = log(x) + 3sin(x/2)
"""

# Imports
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Definição da função dada no exercicio
def f(x):
    return np.log10(x) + 3 * np.sin(x / 2)


# Método da bisseção para estimar as raízes de uma função
def bisection_method_np(f, a, b, tol=0.0001):
    # checar se a e b são raízes
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("Os valores de a e b não são raízes")

    # Pegar o valor do meio do intervalo/ achar o ponto médio
    m = (a + b) / 2

    # Fazer as verificações
    if np.abs(f(m)) < tol:
        # Se a diferença entre a e b for menor que a tolerância, retornar m (raiz)
        return m

    elif np.sign(f(a)) == np.sign(f(m)):
        # Se o sinal de f(a) for igual ao sinal de f(m), chamar a função recursivamente
        return bisection_method_np(f, m, b, tol)

    elif np.sign(f(b)) == np.sign(f(m)):
        # Se o sinal de f(b) for igual ao sinal de f(m), chamar a função recursivamente
        return bisection_method_np(f, a, m, tol)


# Rodando a função no intervalo [4, 11] e com tolerância de 0.0001
raiz = bisection_method_np(f, 4, 11, 0.000_1)
print(f"A raiz da função no intervalo [4, 11] é aproximadamente {raiz:.10f}")


# Plotando o gráfico com o seaborn
x = np.linspace(4, 11, 100)
y = f(x)

# Configuração do gráfico com seaborn
sns.set_theme()
plt.figure(figsize=(10, 6))
sns.lineplot(x=x, y=y, label="f(x) = log(x) + 3sin(x/2)")
plt.scatter(
    raiz,
    f(np.array(raiz)),
    color="red",
    label="Raízes aproximadas",
)
plt.title("Gráfico de f(x) e Raízes Aproximadas")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.axhline(0, color="blue")  # Adiciona linha horizontal em y=0
plt.show()
