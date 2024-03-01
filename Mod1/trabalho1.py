"""
@Antonio Alves
@Carlos Alexandre Sousa Silva
@Eder Queiroz
@Luiz Antonio Folador

Assign:
Crie uma função no Python para estimar raízes pelo
método de busca incremental. O programa deverá
permitir a escolha dos limites inferior e superior do
intervalo de busca e o número de subintervalos. Use
essa função para identificar os subintervalos nos
quais ocorre mudança de sinal dentro do intervalo
[4,11] para a função abaixo. Envie o trabalho para o
e-mail josericardo@iftm.edu.br.

Trabalho 1 = 100 (subintervalos) # erro maximo tolerado
Trabalho 2 = 0,0001 # erro maximo tolerado
Trabalho 3 = 0,0001 # erro maximo tolerado

f(x) = log(x) + 3sin(x/2)
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Definição da função dada no exercicio
def f(x):
    return np.log10(x) + 3 * np.sin(x / 2)


# Função para o método de busca incremental
def busca_incremental(f, a, b, subintervalos=100):
    # Calcula o tamanho de cada subintervalo
    h = (b - a) / subintervalos

    # Inicializa a lista para armazenar os intervalos onde ocorre mudança de sinal
    intervalos_mudanca_sinal = []

    # # Realiza a busca incremental usando apenas o python
    # for i in range(subintervalos):
    #     x1 = a + i * h
    #     x2 = a + (i + 1) * h
    #     if f(x1) * f(x2) < 0:
    #         intervalos_mudanca_sinal.append((x1, x2))

    # Cria um array de valores x1 e x2, usando numpy
    x1 = a + np.arange(subintervalos) * h
    x2 = a + (np.arange(subintervalos) + 1) * h

    # Calcula o f(x1) e f(x2)
    fx1 = f(x1)
    fx2 = f(x2)

    # Encontra onde o sinal muda
    mask = fx1 * fx2 < 0

    # Cria o array de intervalos onde o sinal muda, usando o numpy
    intervalos_mudanca_sinal = np.column_stack((x1[mask], x2[mask]))

    return intervalos_mudanca_sinal


# Uso da função no intervalo [4, 11] com 100 subintervalos
raizes_intervalos = busca_incremental(f, 4, 11, 100)
print(f"Intervalos onde ocorre mudança de sinal: {raizes_intervalos}")

# Lista de raizes aproximadas (pontos médios dos intervalos onde ocorre mudança de sinal)
raizes_aproximadas = [(x[0] + x[1]) / 2 for x in raizes_intervalos]

# Plotando o gráfico com o seaborn
x = np.linspace(4, 11, 100)
y = f(x)

# Configuração do gráfico com seaborn
sns.set_theme()
plt.figure(figsize=(10, 6))
sns.lineplot(x=x, y=y, label="f(x) = log(x) + 3sin(x/2)")
plt.scatter(
    raizes_aproximadas,
    f(np.array(raizes_aproximadas)),
    color="red",
    label="Raízes aproximadas",
)
plt.title("Gráfico de f(x) e Raízes Aproximadas")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.axhline(0, color="blue")
plt.show()
