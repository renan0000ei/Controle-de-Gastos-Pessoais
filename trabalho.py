# importa o arquivo json
import json

# cria a lista das contas e o id
contas =  []
Id = 0

# função que mostra as opções do menu
def menu():
    print("\nMenu:")
    print("1 - Adicionar Receita")
    print("2 - Adicionar Despesas")
    print("3 - Listar Movimentações")
    print("4 - Consultar Saldo")
    print("5 - Excluir Movimentação")
    print("6 - Gerar Relatório")
    print("7 - Sair")

# função que ajuda a iniciar a leitura do json, adiciona o id a cada movimentação, 
# pede as informações da movimentação, coloca elas em uma lista, coloca a lista no dicionario e salva no json(versão receita)
def Adicionar_Receita():
    global contas

    with open("dados.json", "r+", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

        if conteudo == "":
            arquivo.write("[]")
            arquivo.seek(0)

    with open("dados.json", "r", encoding="utf-8") as arquivo:
        contas = json.load(arquivo)

    Id = 0

    for controle in contas:
        controle["id"] = Id = Id + 1

    Id += 1

    descricao = input("digite a descrição: ")
    valor = float(input("digite seu valor: "))
    data = input("digite a data: ")

    controle = {
        "id": Id,
        "descricao": descricao,
        "valor": valor,
        "tipo": "receita",
        "data": data
    }

    contas.append(controle)

    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(contas, arquivo, indent=4, ensure_ascii=False)

# função que ajuda a iniciar a leitura do json, adiciona o id a cada movimentação, 
# pede as informações da movimentação, coloca elas em um dicionario, coloca o dicoinario na lista e salva no json(versão despesa)
def Adicionar_Despesas():
    global contas

    with open("dados.json", "r+", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

        if conteudo == "":
            arquivo.write("[]")
            arquivo.seek(0)

    with open("dados.json", "r", encoding="utf-8") as arquivo:
        contas = json.load(arquivo)

    Id = 0

    for controle in contas:
        controle["id"] = Id = Id + 1

    Id += 1

    descricao = input("digite a descrição: ")
    valor = float(input("digite seu valor: "))
    data = input("digite a data: ")

    controle = {
        "id": Id,
        "descricao": descricao,
        "valor": valor,
        "tipo": "despesa",
        "data": data
    }

    contas.append(controle)

    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(contas, arquivo, indent=4, ensure_ascii=False)

# funçõa que le o arquivo e mostra as movimentações dentro dele
def Lista_Movimentações():
    global controle

    with open("dados.json", "r", encoding="utf-8") as arquivo:
        contas = json.load(arquivo)

    for controle in contas:
        print(f"id: {controle["id"]}; descrição: {controle["descricao"]}; valor: {controle["valor"]}; tipo: {controle["tipo"]}; data: {controle["data"]}")

# funçõa que cria o saldo e o calcula com base na receita e nas despesas dentro do json
def Consultar_Saldo():
    global controle

    saldo = 0.00

    with open("dados.json", "r", encoding="utf-8") as arquivo:
        contas = json.load(arquivo)

    for controle in contas:
        if controle["tipo"] == "receita":
            saldo = saldo + controle["valor"]

        elif controle["tipo"] == "despesa":
            saldo = saldo - controle["valor"]
    print(f"seu saldo é de R${saldo}")

# função que remove movimentação com base no id e atualiza a ordem dentro do json e após isso salvba la dentro
def Excluir_Movimentação():
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        contas = json.load(arquivo)

    Id = int(input("Digite o ID da movimentação que deseja excluir: "))

    for controle in contas:
        if controle["id"] == Id:
            contas.remove(controle)

            Id = 1

            for controle in contas:
                controle["id"] = Id
                Id += 1

            with open("dados.json", "w", encoding="utf-8") as arquivo:
                json.dump(contas, arquivo, indent=4, ensure_ascii=False)

            print("Movimentação excluída com sucesso!")
            return

    print("ID não encontrado.")

# função que calcula o valor de despesas e receitas e calcula o saldo novamente também 
def Gerar_Relatório():
    total_despesas = 0.00
    total_receitas = 0.00
    saldo = 0.00

    with open("dados.json", "r", encoding="utf-8") as arquivo:
        contas = json.load(arquivo)

    for controle in contas:
        if controle["tipo"] == "receita":
            total_receitas = total_receitas + controle["valor"]

        elif controle["tipo"] == "despesa":
            total_despesas = total_despesas + controle["valor"]

    for controle in contas:
        if controle["tipo"] == "receita":
            saldo = saldo + controle["valor"]

        elif controle["tipo"] == "despesa":
            saldo = saldo - controle["valor"]

    print(f"total de receitas: R${total_receitas}")
    print(f"total de despesas: R${total_despesas}")
    print(f"seu saldo é de R${saldo}")

# função que permite o usuario escolher qual opção do menu ele quer
while True:
    menu()
    opc = input("Escolha uma opção: ").strip()
    if opc == "1":
        Adicionar_Receita()         
    elif opc == "2":
        Adicionar_Despesas()
    elif opc == "3":
        Lista_Movimentações()
    elif opc == "4":
        Consultar_Saldo()
    elif opc == "5":
        Excluir_Movimentação()
    elif opc == "6":
        Gerar_Relatório()
    elif opc == "7":
        print("Saindo . . .")
        break
    else:
        print("Opção invalida. Tente novamente.")