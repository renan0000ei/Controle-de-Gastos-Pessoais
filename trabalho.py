import json

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
    pass

def Adicionar_Despesas():
    pass

def Lista_Movimentações():
    pass

def Consultar_Saldo():
    pass

def Excluir_Movimentação():
    pass

def Gerar_Relatório():
    pass

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