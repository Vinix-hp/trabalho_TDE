# Exercício 1
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
soma = 0
for linha in matriz:
    for elemento in linha:
        soma += elemento
print(soma)

# Exercício 2
n = int(input("Digite a ordem da matriz identidade: "))
identidade = []
for i in range(n):
    linha = []
    for j in range(n):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    identidade.append(linha)
for linha in identidade:
    print(linha)

# Exercício 3
matriz = [
    [10, 22, 3, 41],
    [5, 16, 37, 8],
    [19, 2, 31, 44],
    [13, 25, 7, 36]
]
numero = int(input("Digite um número para buscar: "))
encontrado = False
for linha in matriz:
    for elemento in linha:
        if elemento == numero:
            encontrado = True
if encontrado:
    print("Número encontrado na matriz.")
else:
    print("Número não encontrado na matriz.")

# Exercício 4
matriz = [
    [1, 2],
    [3, 4]
]
matriz[0], matriz[1] = matriz[1], matriz[0]
for linha in matriz:
    print(linha)

# Exercício 5
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
escalar = float(input("Digite o escalar: "))
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = matriz[i][j] * escalar
for linha in matriz:
    print(linha)

# Exercício 6
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
pares = 0
for linha in matriz:
    for elemento in linha:
        if elemento % 2 == 0:
            pares += 1
print(pares)

# Exercício 7
import random
matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(random.randint(1, 100))
    matriz.append(linha)

maior = matriz[0][0]
for linha in matriz:
    for elemento in linha:
        if elemento > maior:
            maior = elemento
for linha in matriz:
    print(linha)
print(f"Maior elemento: {maior}")

# Exercício 8
matriz = [
    [4, 8, 2],
    [6, 3, 9],
    [1, 5, 7]
]
for i, linha in enumerate(matriz):
    media = sum(linha) / len(linha)
    print(f"Média da linha {i+1}: {media}")

# Exercício 9
matriz = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
]
soma_diagonal = 0
for i in range(len(matriz)):
    soma_diagonal += matriz[i][i]
print(soma_diagonal)

# Exercício 10
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
m = len(matriz)
n = len(matriz[0])
transposta = []
for j in range(n):
    linha = []
    for i in range(m):
        linha.append(matriz[i][j])
    transposta.append(linha)
for linha in transposta:
    print(linha)

# Exercício 11
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
soma_colunas = []
for j in range(len(matriz[0])):
    total = 0
    for i in range(len(matriz)):
        total += matriz[i][j]
    soma_colunas.append(total)
print(soma_colunas)

# Exercício 12
matriz = [
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9]
]
simetrica = True
n = len(matriz)
for i in range(n):
    for j in range(n):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
if simetrica:
    print("A matriz é simétrica.")
else:
    print("A matriz não é simétrica.")

# Exercício 13
matriz = [
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
n = len(matriz)
for i in range(n):
    print(matriz[i][n - 1 - i])

# Exercício 14
A = [
    [1, 2],
    [3, 4]
]
B = [
    [5, 6],
    [7, 8]
]
linhas_A = len(A)
colunas_A = len(A[0])
colunas_B = len(B[0])
resultado = []
for i in range(linhas_A):
    linha = []
    for j in range(colunas_B):
        total = 0
        for k in range(colunas_A):
            total += A[i][k] * B[k][j]
        linha.append(total)
    resultado.append(linha)
for linha in resultado:
    print(linha)

# Exercício 15
matriz = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
]
n = len(matriz)
rotacionada = []
for j in range(n):
    linha = []
    for i in range(n - 1, -1, -1):
        linha.append(matriz[i][j])
    rotacionada.append(linha)
for linha in rotacionada:
    print(linha)