# Exercício 1
numeros = [1, 2, 3, 4, 5]
print(numeros)

# Exercício 2
cores = ['vermelho', 'azul', 'verde', 'amarelo']
print(cores[1])

# Exercício 3
numeros = [1, 2, 3]
numeros.append(10)
print(numeros)

# Exercício 4
frutas = ['maçã', 'banana', 'laranja']
frutas.remove('banana')
print(frutas)

# Exercício 5
itens = [10, 20, 30, 40, 50]
print(len(itens))

# Exercício 6
valores = [1, 3, 5, 7, 9]
print(7 in valores)

# Exercício 7
lista1 = [1, 2]
lista2 = [3, 4]
lista3 = lista1 + lista2
print(lista3)

# Exercício 8
letras = ['a', 'b', 'c', 'd']
letras.reverse()
print(letras)

# Exercício 9
numeros = [1, 2, 2, 3, 2, 4]
print(numeros.count(2))

# Exercício 10
precos = [10.5, 20.0, 15.5]
print(sum(precos))

# Exercício 11
lista_com_dup = [3, 1, 2, 1, 3, 4, 2]
vistos = []
for item in lista_com_dup:
    if item not in vistos:
        vistos.append(item)
print(vistos)

# Exercício 12
nums = [4, 7, 1, 9, 3]
maior = nums[0]
menor = nums[0]
for num in nums:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(f"Maior: {maior}, Menor: {menor}")

# Exercício 13
quadrados = [x**2 for x in range(1, 11)]
print(quadrados)

# Exercício 14
lista_mista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
impares = [x for x in lista_mista if x % 2 != 0]
print(impares)

# Exercício 15
lista = [1, 2, 3, 4, 5]
n = 2
n = n % len(lista)
lista = lista[-n:] + lista[:-n]
print(lista)

# Exercício 16
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
intersecao = []
for item in a:
    if item in b and item not in intersecao:
        intersecao.append(item)
print(intersecao)

# Exercício 17
matriz = [[1, 2], [3, 4], [5, 6]]
flat = []
for sublista in matriz:
    for item in sublista:
        flat.append(item)
print(flat)

# Exercício 18
lista = [38, 27, 43, 3, 9, 82, 10]
for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[j] < lista[i]:
            lista[i], lista[j] = lista[j], lista[i]
print(lista)

# Exercício 19
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maior_soma = nums[0]
soma_atual = nums[0]
for num in nums[1:]:
    if soma_atual + num > num:
        soma_atual = soma_atual + num
    else:
        soma_atual = num
    if soma_atual > maior_soma:
        maior_soma = soma_atual
print(maior_soma)

# Exercício 20
lista = [1, 2, 3]
resultado = [[]]
for num in lista:
    novas = []
    for perm in resultado:
        for i in range(len(perm) + 1):
            novas.append(perm[:i] + [num] + perm[i:])
    resultado = novas
print(resultado)