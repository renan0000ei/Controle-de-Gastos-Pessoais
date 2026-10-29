import json

contas =  []

def menu():
    print("\nMenu:")
    print("1 - Adicionar Receita")
    print("2 - Adicionar Despesas")
    print("3 - Listar Movimentações")
    print("4 - Consultar Saldo")
    print("5 - Excluir Movimentação")
    print("6 - Gerar Relatório")
    print("7 - Sair")

def Adicionar_Receita():
    
    descricao = input("digite a descrição: ")
    valor = float(input("digite seu valor: "))
    data = input("digite a data: ")

    controle = {
        # "id": ID,
        "descricao": descricao,
        "valor": valor,
        "tipo": "receita",
        "data": data
    }

    contas.append(controle)

    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(contas, arquivo, indent=4, ensure_ascii=False)

    print("receita adicionada com sucesso, uhuuu yes")

def Adicionar_Despesas():

    descricao = input("digite a descrição: ")
    valor = float(input("digite seu valor: "))
    data = input("digite a data: ")

    controle = {
        # "id": ID,
        "descricao": descricao,
        "valor": valor,
        "tipo": "despesa",
        "data": data
    }

    contas.append(controle)

    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(contas, arquivo, indent=4, ensure_ascii=False)

    print("despesas adicionada com sucesso, uhuuu yes")

def Lista_Movimentações():
    global controle

    with open("dados.json", "r", encoding="utf-8") as arquivo:
        contas = json.load(arquivo)

    for controle in contas:
        print(f"{controle["descricao"]}; {controle["valor"]}; {controle["tipo"]}; {controle["data"]}")

def Consultar_Saldo():
    global saldo
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

def Excluir_Movimentação():
    pass

def Gerar_Relatório():
    total_despesas = 0.00
    total_receitas = 0.00

    with open("dados.json", "r", encoding="utf-8") as arquivo:
        contas = json.load(arquivo)

    for controle in contas:
        if controle["tipo"] == "receita":
            total_receitas = total_receitas + controle["valor"]

        elif controle["tipo"] == "despesa":
            total_despesas = total_despesas + controle["valor"]

    print(f"total de receitas: R${total_receitas}")
    print(f"total de despesas: R${total_despesas}")
    print(f"seu saldo é de R${saldo}")
    
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