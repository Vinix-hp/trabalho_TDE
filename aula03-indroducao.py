# Exercício 1: Média de Notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Sua média é: {media:.2f}")
    

# Exercício 2: Calculadora de Desconto
preco = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o percentual de desconto (%): "))
valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto
print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
print(f"Valor final a pagar: R$ {preco_final:.2f}")


# Exercício 3: Par ou Ímpar
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print(f"O número {numero} é Par.")
else:
    print(f"O número {numero} é Ímpar.")


# Exercício 4: print() é a função padrão para exibir mensagens no console
print("Olá, mundo!")


# Exercício 5: int() converte o retorno do input() para número inteiro
idade = int(input("Digite sua idade: "))
print(f"Sua idade é {idade} anos.")


# Exercício 6: Python usa indentação para definir blocos de código
x = 10
if x > 5:
    print("x é maior que 5")
else:
    print("x é menor ou igual a 5")


# Exercício 7: o operador / retorna divisão real, // retorna só a parte inteira
print(7 / 2)   # 3.5
print(7 // 2)  # 3


# Exercício 8: == é o operador de comparação de igualdade
numero = int(input("Digite um número: "))
if numero == 10:
    print("O número é exatamente 10!")
else:
    print("O número é diferente de 10.")