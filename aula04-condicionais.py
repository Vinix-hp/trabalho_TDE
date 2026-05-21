# Exercício 1: Votação — verifica se tem idade para votar
idade = int(input("Digite sua idade: "))
if idade >= 16:
    print("Você já pode votar!")
else:
    print("Você ainda não tem idade para votar.")


# Exercício 2: Positivo, Negativo ou Zero
numero = int(input("Digite um número inteiro: "))
if numero > 0:
    print(f"O número {numero} é Positivo.")
elif numero < 0:
    print(f"O número {numero} é Negativo.")
else:
    print("O número é Zero.")


# Exercício 3: Desconto de 10% para compras acima de R$ 100
compra = float(input("Digite o valor total da compra: R$ "))
if compra > 100:
    valor_final = compra - (compra * 0.10)
    print(f"Desconto aplicado! Valor final: R$ {valor_final:.2f}")
else:
    print(f"Valor da compra: R$ {compra:.2f}")
    print("Nas compras acima de R$ 100, você ganha 10% de desconto!")


# Exercício 4: Classifica o aluno com base na nota
nota = float(input("Digite sua nota: "))
if nota >= 9.0:
    print("Parabéns!! Você foi aprovado!")
elif nota >= 7.0:
    print("Aprovado.")
elif nota >= 4.0:
    print("Em Recuperação.")
else:
    print("Reprovado.")


# Exercício 5: Par ou Ímpar usando o operador %
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print(f"O número {numero} é Par.")
else:
    print(f"O número {numero} é Ímpar.")


# Exercício 6: Compara dois números e informa o maior
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 > num2:
    print(f"O primeiro número ({num1}) é maior.")
elif num2 > num1:
    print(f"O segundo número ({num2}) é maior.")
else:
    print("Os dois números são iguais.")


# Exercício 7: Verifica se o usuário digitou o login correto
usuario_correto = "admin"
usuario = input("Digite seu nome de usuário: ")
if usuario == usuario_correto:
    print("Acesso concedido.")
else:
    print("Usuário desconhecido.")


# Exercício 8: Calcula o IMC e classifica o resultado
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")
if imc > 25:
    print("Acima do peso ideal.")
else:
    print("Peso dentro da normalidade.")


# Exercício 9: Classifica o triângulo pelos lados
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))
if lado1 == lado2 == lado3:
    print("Triângulo Equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo Isósceles.")
else:
    print("Triângulo Escaleno.")


# Exercício 10: Verifica se o número é múltiplo de 5
numero = int(input("Digite um número: "))
if numero % 5 == 0:
    print(f"{numero} é múltiplo de 5.")
else:
    print(f"{numero} não é múltiplo de 5.")


# Exercício 11: Classifica o nadador por faixa etária
idade = int(input("Digite a idade do nadador: "))
if 5 <= idade <= 7:
    print("Categoria: Infantil A.")
elif 8 <= idade <= 10:
    print("Categoria: Infantil B.")
elif 11 <= idade <= 13:
    print("Categoria: Juvenil A.")
elif 14 <= idade <= 17:
    print("Categoria: Juvenil B.")
elif idade >= 18:
    print("Categoria: Adulto.")
else:
    print("Idade fora das categorias permitidas.")


# Exercício 12: Calcula o preço da passagem por km rodado
distancia = float(input("Digite a distância da viagem (km): "))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"Valor da passagem: R$ {preco:.2f}")


# Exercício 13: Verifica se o ano é bissexto
ano = int(input("Digite um ano: "))
if ano % 4 == 0:
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")


# Exercício 14: Aplica aumento salarial conforme faixa de salário
salario = float(input("Digite o salário do funcionário: R$ "))
if salario > 1621.00:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
print(f"Aumento: R$ {aumento:.2f} | Novo salário: R$ {salario + aumento:.2f}")


# Exercício 15: Calcula a multa para quem ultrapassar 80 km/h
velocidade = float(input("Digite a velocidade do carro (km/h): "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"Você foi multado! Multa: R$ {multa:.2f}")
else:
    print("Velocidade dentro do limite.")


# Exercício 16: Converte Celsius para Fahrenheit ou Kelvin
celsius = float(input("Digite a temperatura em Celsius: "))
opcao = input("Converter para Fahrenheit (F) ou Kelvin (K)? ").strip().upper()
if opcao == "F":
    print(f"{celsius}°C = {(celsius * 9 / 5) + 32:.2f}°F")
elif opcao == "K":
    print(f"{celsius}°C = {celsius + 273.15:.2f}K")
else:
    print("Opção inválida.")


# Exercício 17: Calcula quantas latas de tinta são necessárias
import math
area = float(input("Digite a área a ser pintada (m²): "))
latas = math.ceil((area / 3) / 18)
if latas <= 1:
    print("Você precisará de apenas uma lata. Custo: R$ 80,00")
else:
    print(f"Você precisará de {latas} latas. Custo: R$ {latas * 80:.2f}")


# Exercício 18: Aprova ou nega empréstimo com base na prestação vs salário
valor_casa = float(input("Valor da casa: R$ "))
salario = float(input("Salário mensal: R$ "))
anos = int(input("Prazo para pagamento (anos): "))
prestacao = valor_casa / (anos * 12)
print(f"Prestação mensal: R$ {prestacao:.2f} | Limite: R$ {salario * 0.30:.2f}")
if prestacao <= salario * 0.30:
    print("Empréstimo APROVADO!")
else:
    print("Empréstimo NEGADO. Prestação ultrapassa 30% do salário.")


# Classificação das estruturas:
# Simples (só if): nenhum neste exercício
# Composta (if/else): exercícios 1, 3, 5, 7, 8, 10, 12, 13, 14, 15, 17, 18
# Aninhada (if/elif/else): exercícios 2, 4, 6, 9, 11, 16