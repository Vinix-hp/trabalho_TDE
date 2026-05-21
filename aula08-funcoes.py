# Exercício 1
def somar(a, b):
    return a + b

print(somar(3, 5))

# Exercício 2
def multiplicar(a, b):
    return a * b

print(multiplicar(4, 6))

# Exercício 3
def mensagem(nome):
    print(f"Olá, {nome}!")

mensagem("Maria")

# Exercício 4
def maior(a, b):
    if a > b:
        return a
    return b

print(maior(10, 7))

# Exercício 5
def dividir(a, b):
    return a // b, a % b

quociente, resto = dividir(10, 3)
print(f"Quociente: {quociente}, Resto: {resto}")

# Exercício 6
def par_ou_impar(n):
    return n % 2 == 0

print(par_ou_impar(4))
print(par_ou_impar(7))

# Exercício 7
# A função teste() imprime 'Olá' mas não tem return, então retorna None.
# O print(resultado) vai exibir None.
def teste():
    print('Olá')

resultado = teste()
print(resultado)

# Exercício 8
def apresentar(nome, idade, cidade):
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

# Exercício 9
apresentar("Ana", 20, "Curitiba")           # posicionais
apresentar(nome="Ana", cidade="Curitiba", idade=20)  # nomeados

# Exercício 10
# apresentar('Ana', 'Curitiba', 20) funciona sem erro, mas os dados ficam
# na ordem errada: nome='Ana', idade='Curitiba', cidade=20.
apresentar('Ana', 'Curitiba', 20)

# Exercício 11
def saudacao(nome, periodo='dia'):
    print(f"Bom {periodo}, {nome}!")

# Exercício 12
saudacao("Carlos")           # usa valor padrão
saudacao("Carlos", "tarde")  # substitui o padrão

# Exercício 13
# def exemplo(a=1, b): causa SyntaxError.
# Parâmetros com valor padrão devem sempre vir depois dos sem valor padrão.
# Correto seria: def exemplo(b, a=1):
def exemplo(b, a=1):
    print(a, b)

exemplo(5)

# Exercício 14
def somar_todos(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total

print(somar_todos(1, 2, 3, 4, 5))

# Exercício 15
def mostrar_dados(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

mostrar_dados(nome="Ana", idade=20, cidade="Curitiba")

# Exercício 16
# *args recebe argumentos posicionais extras como uma tupla.
# **kwargs recebe argumentos nomeados extras como um dicionário.
# Usa-se *args quando não se sabe quantos valores serão passados,
# e **kwargs quando não se sabe quais nomes serão usados.
def exemplo_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

exemplo_args_kwargs(1, 2, 3, nome="Ana", cidade="Curitiba")

# Exercício 17
# A variável x dentro de teste() é local, não afeta o x de fora.
# Saída: 5 (de dentro da função), depois 10 (o x global).
x = 10
def teste():
    x = 5
    print(x)

teste()
print(x)

# Exercício 18
# contador += 1 dentro da função causa UnboundLocalError porque Python trata
# contador como variável local ao ver a atribuição, mas ela não foi definida localmente.
# A correção é declarar global contador.
contador = 0
def incrementar():
    global contador
    contador += 1

incrementar()
incrementar()
print(contador)

# Exercício 19
def triplo(x):
    return x * 3

minha_funcao = triplo
print(minha_funcao(5))

# Exercício 20
def executar(funcao, valor):
    return funcao(valor)

print(executar(triplo, 4))

# Exercício 21
quadrado = lambda x: x ** 2
print(quadrado(6))

# Exercício 22
dobrados = list(map(lambda x: x * 2, [1, 2, 3, 4, 5]))
print(dobrados)

# Exercício 23
pares = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
print(pares)

# Exercício 24
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

print(fatorial(5))

# Exercício 25
def contagem(n):
    if n < 0:
        return
    print(n)
    contagem(n - 1)

contagem(5)

# Exercício 26
# def erro(n): return n * erro(n - 1) nunca para porque não tem caso base.
# A função vai chamar a si mesma infinitamente até estourar a pilha (RecursionError).
# A correção é adicionar o caso base:
def erro_corrigido(n):
    if n == 0:
        return 1
    return n * erro_corrigido(n - 1)

print(erro_corrigido(4))

# Exercício 27
def media(lista):
    """
    Calcula e retorna a média aritmética dos elementos de uma lista de números.

    Parâmetros:
        lista (list): lista de números inteiros ou reais.

    Retorno:
        float: média dos valores da lista.
    """
    return sum(lista) / len(lista)

print(media([4, 8, 6, 10]))

# Exercício 28
help(media)

# Exercício 29
def calculadora(a, b, operacao):
    if operacao == 'somar':
        return a + b
    elif operacao == 'subtrair':
        return a - b
    elif operacao == 'multiplicar':
        return a * b
    elif operacao == 'dividir':
        return a / b
    else:
        return "Operação inválida"

print(calculadora(10, 5, 'somar'))
print(calculadora(10, 5, 'dividir'))

# Exercício 30
def processar_dados(*args, **kwargs):
    print("Valores recebidos:", args)
    print("Dados nomeados:", kwargs)

processar_dados(1, 2, 3, nome="Ana", cidade="Curitiba")