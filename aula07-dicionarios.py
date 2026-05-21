# Exercício 1
pessoa = {'nome': 'Ana', 'idade': 25, 'cidade': 'Curitiba'}
chave = input("Digite uma chave (nome, idade, cidade): ")
if chave in pessoa:
    print(pessoa[chave])
else:
    print("Chave não encontrada.")

# Exercício 2
precos = {'arroz': 10.0, 'feijão': 8.5, 'macarrão': 5.0}
produto = input("Qual produto deseja alterar? ")
if produto in precos:
    novo_preco = float(input("Novo preço: "))
    precos[produto] = novo_preco
    print(precos)
else:
    print("Produto não encontrado.")

# Exercício 3
dados = {}
nome = input("Digite um nome: ")
idade = int(input("Digite a idade: "))
dados[nome] = idade
print(dados)

# Exercício 4
pares = []
for i in range(3):
    chave = input(f"Digite a chave {i+1}: ")
    valor = input(f"Digite o valor {i+1}: ")
    pares.append((chave, valor))
dicionario = dict(pares)
print(dicionario)

# Exercício 5
dados = {'nome': 'Carlos', 'cidade': 'SP', 'profissão': 'dev'}
resposta = input("Deseja apagar todos os dados? (sim/não): ")
if resposta.lower() == 'sim':
    dados.clear()
print(dados)

# Exercício 6
original = {'nome': 'Maria', 'idade': 30, 'cidade': 'RJ'}
copia = original.copy()
copia['cidade'] = 'SP'
print("Original:", original)
print("Cópia:", copia)

# Exercício 7
nomes = input("Digite os nomes separados por vírgula: ").split(',')
nomes = [n.strip() for n in nomes]
dicionario = dict.fromkeys(nomes, 0)
print(dicionario)

# Exercício 8
alunos = {'Ana': 9.0, 'Carlos': 7.5, 'Maria': 8.0}
nome = input("Digite o nome do aluno: ")
nota = alunos.get(nome, "Aluno não encontrado.")
print(nota)

# Exercício 9
produtos = {'arroz': 10.0, 'feijão': 8.5, 'macarrão': 5.0}
print("Chaves:", list(produtos.keys()))
print("Valores:", list(produtos.values()))
print("Pares:", list(produtos.items()))

# Exercício 10
dados = {'nome': 'João', 'idade': 22, 'cidade': 'BH', 'curso': 'TI'}
chave = input("Digite uma chave para remover com pop(): ")
if chave in dados:
    dados.pop(chave)
removido = dados.popitem()
print(f"Removido com popitem(): {removido}")
nova_chave = input("Nova chave para adicionar: ")
novo_valor = input("Novo valor: ")
dados.update({nova_chave: novo_valor})
print(dados)

# Exercício 11
usuarios = {'Ana': 25, 'Carlos': 30, 'Maria': 22}

while True:
    print("\n--- MENU ---")
    print("1. Exibir usuários")
    print("2. Buscar usuário")
    print("3. Adicionar usuário")
    print("4. Atualizar idade")
    print("5. Remover usuário (pop)")
    print("6. Remover último (popitem)")
    print("7. Copiar e alterar")
    print("8. Criar com fromkeys")
    print("9. Atualizar com update")
    print("10. Limpar tudo (clear)")
    print("11. Criar com dict()")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("Nomes:", list(usuarios.keys()))
        print("Idades:", list(usuarios.values()))
        print("Pares:", list(usuarios.items()))

    elif opcao == '2':
        nome = input("Nome do usuário: ")
        resultado = usuarios.get(nome, "Usuário não encontrado.")
        print(resultado)

    elif opcao == '3':
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        usuarios[nome] = idade
        print("Usuário adicionado.")

    elif opcao == '4':
        nome = input("Nome do usuário: ")
        if nome in usuarios:
            nova_idade = int(input("Nova idade: "))
            usuarios[nome] = nova_idade
            print("Idade atualizada.")
        else:
            print("Usuário não encontrado.")

    elif opcao == '5':
        nome = input("Nome para remover: ")
        if nome in usuarios:
            usuarios.pop(nome)
            print("Usuário removido.")
        else:
            print("Usuário não encontrado.")

    elif opcao == '6':
        if usuarios:
            removido = usuarios.popitem()
            print(f"Removido: {removido}")
        else:
            print("Dicionário vazio.")

    elif opcao == '7':
        copia = usuarios.copy()
        nome = input("Qual usuário alterar na cópia? ")
        if nome in copia:
            nova_idade = int(input("Nova idade na cópia: "))
            copia[nome] = nova_idade
        print("Original:", usuarios)
        print("Cópia:", copia)

    elif opcao == '8':
        nomes = input("Nomes separados por vírgula: ").split(',')
        nomes = [n.strip() for n in nomes]
        idade_padrao = int(input("Idade padrão: "))
        novo = dict.fromkeys(nomes, idade_padrao)
        print("Novo dicionário:", novo)

    elif opcao == '9':
        qtd = int(input("Quantos usuários adicionar? "))
        novos = {}
        for _ in range(qtd):
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            novos[nome] = idade
        usuarios.update(novos)
        print("Dicionário atualizado:", usuarios)

    elif opcao == '10':
        confirmacao = input("Tem certeza? Isso apaga tudo (sim/não): ")
        if confirmacao.lower() == 'sim':
            usuarios.clear()
            print("Dicionário limpo.")

    elif opcao == '11':
        qtd = int(input("Quantos pares? "))
        tuplas = []
        for _ in range(qtd):
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            tuplas.append((nome, idade))
        novo = dict(tuplas)
        print("Novo dicionário:", novo)

    elif opcao == '0':
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")