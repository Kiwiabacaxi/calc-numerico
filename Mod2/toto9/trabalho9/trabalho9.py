import numpy as np

valores_coeficientes = [[6, 2, 1, -1],
                        [-2, 7, -1, 1],
                        [-1, 1, 8, 1],
                        [2, 2, 1, 9]]

vetor_coeficientes = np.array(valores_coeficientes)
resultado = np.array([2, 0.5, 2, 1])



tolerancia = 0.02




def gauss_seidel(A: np.ndarray, b: np.ndarray, tolerance=tolerancia):
    size = A.shape[0]
    vetor_aproximacao = np.zeros(size)
    
    iteracoes = 0
    while True:
        antiga_aproximacao = np.copy(vetor_aproximacao)

        for i in range(len(vetor_aproximacao)):
            vetor_aproximacao[i] = (b[i] - np.dot(A[i, :i], vetor_aproximacao[:i]) - np.dot(A[i, (i+1):], antiga_aproximacao[i+1:])) / A[i, i]

        erro_maximo = max([abs(x - y) for x, y in zip(antiga_aproximacao, vetor_aproximacao)])
        if erro_maximo < tolerance:
            break
    
        iteracoes += 1
    
    print("Resultado final após", iteracoes, "iterações:")
    print(vetor_aproximacao)

gauss_seidel(vetor_coeficientes, resultado)