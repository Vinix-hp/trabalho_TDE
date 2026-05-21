# Exercício 1
# x = 2, a condição x * 2 > 3 é 4 > 3, que é verdadeira. Imprime "A".

# Exercício 2
# Loop com i assumindo os valores 1, 2, 3. Imprime i * 2 a cada iteração.
# Saída: 2, 4, 6

# Exercício 3
# n = 7, 7 % 2 == 0 é falso. Cai no else. Imprime "Ímpar".

# Exercício 4
# s começa em 0. Loop com i = 0, 1, 2. s += 2 três vezes, s = 6. Imprime 6.

# Exercício 5
# i começa em 0. while i < 2: imprime i (0, depois 1), incrementa i.
# Saída: 0, 1

# Exercício 6
# x = 10. Não é < 5. elif x < 15 é verdadeiro (10 < 15). Imprime "B".

# Exercício 7
# n = 0. Em Python, 0 é considerado falso. Cai no else. Imprime "False".

# Exercício 8
# Loop com i assumindo os valores 2, 3, 4, 5. Imprime cada um.
# Saída: 2, 3, 4, 5

# Exercício 9
# soma começa em 0. Loop com i = 1, 2, 3. soma acumula 1+2+3 = 6. Imprime 6.

# Exercício 10
# x = 3, y = 4. x == y é falso. Cai no else. Imprime "2".

# Exercício 11
numero = int(input("Digite um número: "))
if numero % 3 == 0:
    print("É múltiplo de 3.")
else:
    print("Não é múltiplo de 3.")

# Exercício 12
numero = int(input("Digite um número: "))
if 10 <= numero <= 20:
    print("Está entre 10 e 20.")
else:
    print("Não está entre 10 e 20.")

# Exercício 13
idade = int(input("Digite sua idade: "))
if idade < 18:
    print("Menor de idade.")
elif idade < 60:
    print("Adulto.")
else:
    print("Idoso.")

# Exercício 14
numero = int(input("Digite um número: "))
if numero > 0 and numero % 2 == 0:
    print("É positivo e par.")
else:
    print("Não é positivo e par.")

# Exercício 15
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
if a == b == c:
    print("Os três números são iguais.")
else:
    print("Os números não são todos iguais.")

# Exercício 16
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
if a < b:
    print(f"O menor é {a}.")
else:
    print(f"O menor é {b}.")

# Exercício 17
temperatura = float(input("Digite a temperatura: "))
if temperatura < 15:
    print("Fria.")
elif temperatura <= 30:
    print("Agradável.")
else:
    print("Quente.")

# Exercício 18
usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")
if usuario == "admin" and senha == "1234":
    print("Login realizado com sucesso.")
else:
    print("Usuário ou senha incorretos.")

# Exercício 19
valor = float(input("Digite o valor: "))
if valor > 200:
    desconto = valor * 0.20
elif valor > 100:
    desconto = valor * 0.10
else:
    desconto = 0
print(f"Valor com desconto: {valor - desconto:.2f}")

# Exercício 20
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
if a >= b and a >= c:
    print(f"O maior é {a}.")
elif b >= a and b >= c:
    print(f"O maior é {b}.")
else:
    print(f"O maior é {c}.")

# Exercício 21
soma = 0
for i in range(1, 11):
    soma += i
print(f"Soma de 1 a 10: {soma}")

# Exercício 22
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Exercício 23
soma = 0
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero
print(f"Média: {soma / 5:.2f}")

# Exercício 24
negativos = 0
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero < 0:
        negativos += 1
print(f"Quantidade de negativos: {negativos}")

# Exercício 25
soma = 0
while True:
    numero = int(input("Digite um número (0 para parar): "))
    if numero == 0:
        break
    soma += numero
print(f"Soma: {soma}")

# Exercício 26
maiores = 0
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    if numero > 5:
        maiores += 1
print(f"Quantidade maiores que 5: {maiores}")

# Exercício 27
pares = 0
while True:
    numero = int(input("Digite um número (negativo para parar): "))
    if numero < 0:
        break
    if numero % 2 == 0:
        pares += 1
print(f"Quantidade de pares: {pares}")

# Exercício 28
numero = int(input("Digite um número: "))
fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
print(f"{numero}! = {fatorial}")

# Exercício 29
numero = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Exercício 30
aprovadas = 0
for i in range(5):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    if nota >= 7:
        aprovadas += 1
print(f"Notas >= 7: {aprovadas}")