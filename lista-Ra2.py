# Exercício 1
# lista começa com [5, 10]. append(15) adiciona 15 ao final: [5, 10, 15].
# len(lista) retorna 3. Imprime 3.

# Exercício 2
# lista começa com [1, 2, 3]. insert(1, 10) insere 10 no índice 1.
# Lista vira [1, 10, 2, 3]. Imprime [1, 10, 2, 3].

# Exercício 3
# lista = [2, 4, 6]. lista[1] é 4. 4 * 2 = 8. Imprime 8.

# Exercício 4
# dados['x'] é 1, dados['y'] é 2. 1 + 2 = 3. Imprime 3.

# Exercício 5
# dados.get('b', 5) tenta buscar a chave 'b', que não existe.
# Como tem valor padrão, retorna 5 sem gerar erro. Imprime 5.

# Exercício 6
# total começa em 0. Loop percorre [1, 2, 3] somando cada valor.
# total = 1, depois 3, depois 6. Imprime 6.

# Exercício 7
# soma começa em 0. range(len(nums)) gera 0, 1, 2, 3.
# soma acumula nums[0]+nums[1]+nums[2]+nums[3] = 1+2+3+4 = 10. Imprime 10.

# Exercício 8
# lista = [10, 20, 30]. pop(0) remove o elemento do índice 0 (o 10).
# Lista vira [20, 30]. Imprime [20, 30].

# Exercício 9
# lista2 = lista não copia a lista, aponta para o mesmo objeto na memória.
# lista2.append(4) modifica o objeto original. print(lista) imprime [1, 2, 3, 4].

# Exercício 10
# dados começa com {'nome': 'João'}. dados['idade'] = 25 adiciona nova chave.
# Imprime {'nome': 'João', 'idade': 25}.

# Exercício 11
# m é uma matriz numpy 2x2. m[0, 1] acessa linha 0, coluna 1, que é 2. Imprime 2.

# Exercício 12
# m é uma matriz 2x3. m[1] acessa a linha de índice 1, que é [4, 5, 6]. Imprime [4 5 6].

# Exercício 13
# dados['a'] é 1. 1 + 5 = 6. Atualiza dados['a'] para 6. Imprime 6.

# Exercício 14
# lista = [2, 4, 6, 8]. Índice -1 acessa o último elemento, que é 8. Imprime 8.

# Exercício 15
# lista = [1, 2, 3]. del lista[1] remove o elemento do índice 1 (o 2).
# Lista vira [1, 3]. Imprime [1, 3].

# Exercício 16
# Loop percorre [1, 3, 5]. Imprime cada valor multiplicado por 2.
# Saída: 2, 6, 10.

# Exercício 17
# 'x' in dados verifica se a chave 'x' existe no dicionário. Existe. Imprime True.

# Exercício 18
# dados tem 2 chaves ('a' e 'b'). len(dados) retorna 2. Imprime 2.

# Exercício 19
# lista[1:] retorna todos os elementos a partir do índice 1 até o fim.
# Resultado: [20, 30]. Imprime [20, 30].

# Exercício 20
# m[:, 0] seleciona todas as linhas, coluna 0. Resultado: [1, 3]. Imprime [1 3].

# Exercício 21
# Uma lista é uma coleção ordenada e mutável de elementos.
# Pode conter tipos diferentes e permite duplicatas.
# Exemplo: frutas = ['maçã', 'banana', 'laranja']

# Exercício 22
# Um dicionário armazena pares chave-valor. Acessa-se pelo nome da chave.
# Exemplo: pessoa = {'nome': 'Ana', 'idade': 20} -> pessoa['nome'] retorna 'Ana'.

# Exercício 23
# append(x) sempre adiciona x ao final da lista.
# insert(i, x) adiciona x em uma posição específica i, deslocando os demais.

# Exercício 24
# pop() remove e retorna o último elemento da lista.
# pop(i) remove e retorna o elemento do índice i.

# Exercício 25
# dados['chave'] lança KeyError se a chave não existir.
# dados.get('chave') retorna None (ou um valor padrão) sem gerar erro.

# Exercício 26
# Acessar uma chave inexistente com colchetes gera KeyError e interrompe o programa.

# Exercício 27
# Índice negativo conta a partir do final da lista. -1 é o último, -2 é o penúltimo, etc.
# Exemplo: lista = [1, 2, 3] -> lista[-1] retorna 3.

# Exercício 28
# for elemento in lista itera diretamente sobre os valores.
# for i in range(len(lista)) itera sobre os índices, útil quando precisa da posição.

# Exercício 29
# Uma matriz em Python é uma lista de listas, onde cada sublista representa uma linha.
# Exemplo: m = [[1, 2], [3, 4]] é uma matriz 2x2.

# Exercício 30
# NumPy é uma biblioteca para computação numérica. Oferece arrays multidimensionais
# eficientes e funções matemáticas. Usado para matrizes, álgebra linear e ciência de dados.

# Exercício 31
numeros = [4, 8, 15, 16, 23]
soma = 0
for n in numeros:
    soma += n
print(soma)

# Exercício 32
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares = 0
for n in numeros:
    if n % 2 == 0:
        pares += 1
print(f"Pares: {pares}")

# Exercício 33
alunos = {'Ana': 9.0, 'Carlos': 7.5, 'Maria': 8.0}
for aluno, nota in alunos.items():
    print(f"{aluno}: {nota}")

# Exercício 34
lista = [10, 20, 30, 40, 50]
numero = int(input("Digite um número: "))
if numero in lista:
    print("Está na lista.")
else:
    print("Não está na lista.")

# Exercício 35
lista = [5, 12, 3, 18, 7, 25]
for n in lista:
    if n > 10:
        print(n)

# Exercício 36
dados = {'nome': 'Ana', 'idade': 20, 'cidade': 'Curitiba'}
chave = input("Qual chave deseja atualizar? ")
novo_valor = input("Novo valor: ")
if chave in dados:
    dados[chave] = novo_valor
    print(dados)
else:
    print("Chave não encontrada.")

# Exercício 37
lista = [6, 8, 4, 10, 7]
soma = 0
for n in lista:
    soma += n
media = soma / len(lista)
print(f"Média: {media:.2f}")

# Exercício 38
lista = [3, -1, 7, -4, 0, -2, 5]
sem_negativos = []
for n in lista:
    if n >= 0:
        sem_negativos.append(n)
print(sem_negativos)

# Exercício 39
nomes = []
while True:
    nome = input("Digite um nome (ou 'fim' para parar): ")
    if nome.lower() == 'fim':
        break
    nomes.append(nome)
print(nomes)

# Exercício 40
dados = {'nome': 'João', 'idade': 30, 'cidade': 'SP'}
chave = input("Qual chave deseja verificar? ")
if chave in dados:
    print("Chave existe.")
else:
    print("Chave não existe.")

# Exercício 41
lista = [1, 3, 2, 3, 5, 3, 7]
numero = int(input("Qual número contar? "))
contagem = 0
for n in lista:
    if n == numero:
        contagem += 1
print(f"Aparece {contagem} vez(es).")

# Exercício 42
lista = [4, 9, 2, 17, 5, 11]
maior = lista[0]
for n in lista:
    if n > maior:
        maior = n
print(f"Maior: {maior}")

# Exercício 43
produtos = {'arroz': 10.0, 'feijão': 8.5, 'macarrão': 5.0}
for produto in produtos:
    produtos[produto] = produtos[produto] * 0.90
for produto, preco in produtos.items():
    print(f"{produto}: R$ {preco:.2f}")

# Exercício 44
lista = [1, 2, 3, 4, 5, 6, 7]
soma_impares = 0
for n in lista:
    if n % 2 != 0:
        soma_impares += n
print(f"Soma dos ímpares: {soma_impares}")

# Exercício 45
lista = [1, 2, 3, 4, 5]
invertida = []
for i in range(len(lista) - 1, -1, -1):
    invertida.append(lista[i])
print(invertida)

# Exercício 46 - com listas
matriz = [
    [1, 2],
    [3, 4]
]
for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()

# Exercício 47 - com listas
matriz = [
    [1, 2],
    [3, 4]
]
soma = 0
for linha in matriz:
    for elemento in linha:
        soma += elemento
print(f"Soma: {soma}")

# Exercício 48 - com listas
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(len(matriz)):
    print(matriz[i][i])

# Exercício 49 - com numpy
import numpy as np
m = np.array([[1, 2], [3, 4]])
print(m * 2)

# Exercício 50 - com numpy
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A + B)