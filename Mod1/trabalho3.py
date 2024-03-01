"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Assign:
Crie uma função no Python para determinação de
raízes pelo método da falsa posição e em seguida
resolva o mesmo problema abordado no trabalho 2.
Envie o trabalho para o e-mail
josericardo@iftm.edu.br.

Trabalho 3 = 0,0001 # erro maximo tolerado

f(x) = log(x) + 3sin(x/2)
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Definição da função dada no exercicio
def f(x):
    return np.log10(x) + 3 * np.sin(x / 2)


def false_position_np(f, a, b, tol):
    if np.sign(f(a)) == np.sign(f(b)):
        # Se o sinal de f(a) for igual ao sinal de f(b), lançar uma exceção
        raise Exception("Os valores de a e b não são raízes")

    # Inicializa as variáveis
    fa = f(a)
    fb = f(b)
    c = a
    iteracao = 0

    while True:
        iteracao += 1

        # Calcula o ponto médio (ou a falsa posição)
        c_anterior = c  # Guarda o valor anterior de c para comparação
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)

        if fc == 0 or (b - a) / 2 < tol:
            break

        print(f"Iteração {iteracao}: x = {c}")

        if np.sign(fc) == np.sign(fa):
            a = c
            fa = fc
        else:
            b = c
            fb = fc

        # Adiciona uma condição de parada para evitar loop infinito
        if np.isclose(c, c_anterior, atol=tol):
            break

    return c


# Valores iniciais

# Chamando a função
a = 4
b = 15
tol = 0.000_1
# raiz = false_position_np(f, 4, 11, 0.000_1)
# lista de raizes
raizes = []
for i in range(a, b):
    try:
        raiz = false_position_np(f, i, i + 1, tol)
        raizes.append(raiz)
    except Exception:
        pass


# printar a lista de raizes
print(f"O intervalo entre [{a},{b}] tem as seguintes raizes: {raizes}")

# Plotando o gráfico com o seaborn
x = np.linspace(a, b, 1_000)
y = f(x)


# Configuração do gráfico com seaborn
sns.set_theme()
plt.figure(figsize=(10, 6))
sns.lineplot(x=x, y=y, label="f(x) = log(x) + 3sin(x/2)")
plt.scatter(
    raizes,  # Certifique-se de que 'raizes' é uma lista de raízes
    f(np.array(raizes)),  # Aplica a função a todas as raízes
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
