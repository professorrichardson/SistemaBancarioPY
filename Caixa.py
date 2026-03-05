# ==========================================
# SIMULADOR DE CAIXA ELETRÔNICO
# Nome:Emanuelly Campos Heerdt
# Turma:3 tec
# ==========================================
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
RESET = "\033[0m"
# ----------------------------
# VARIÁVEIS GLOBAIS
# ----------------------------
saldo = 1000.0
extrato = []


# ----------------------------
# FUNÇÃO: exibir_menu
# ----------------------------
def exibir_menu():
    print(AZUL+"\n=============================="+RESET)
    print(AZUL+"\n====== CAIXA ELETRÔNICO ======"+RESET)
    print(AZUL+"\n=============================="+RESET)
    print(VERDE+"1 - Consultar Saldo"+RESET)
    print(VERDE+"2 - Depositar"+RESET)
    print(VERDE+"3 - Sacar"+RESET)
    print(VERDE+"4 - Ver Extrato"+RESET)
    print(VERDE+"5 - Sair"+RESET)


# ----------------------------
# FUNÇÃO: consultar_saldo
# ----------------------------
def consultar_saldo():
    global saldo
    print(f"\nSaldo atual: R$ {saldo:.2f}")


# ----------------------------
# FUNÇÃO: depositar
# ----------------------------
def depositar():
    global saldo
    global extrato

    valor = input("Digite o valor para depósito: ")

    if valor <= 0:
          print("O caixa só aceita números positivos!")
          

    # TODO 1:
    # Validar se a entrada é numérica.
    # Caso não seja, exibir mensagem de erro e retornar.
    valor = float(valor_str)

    if valor <= 0:
          print("O caixa só aceita números positivos!")
    elif valor > 1000:
          print("O caixa não permite saque maior que R$ 1000.")
          

    valor = float(valor)

    # TODO 2:
    # Verificar se o valor é positivo.
    # Caso não seja, exibir mensagem de erro e retornar.

    # TODO 3:
    # Atualizar o saldo.

    # TODO 4:
    # Registrar a operação na lista extrato.

    print("Depósito realizado com sucesso!")


# ----------------------------
# FUNÇÃO: sacar
# ----------------------------
def sacar():
    global saldo
    global extrato

    valor_str = input("Digite o valor para saque: ")

    # TODO 5:
    # Validar se a entrada é numérica.

    valor = float(valor_str)

    # TODO 6:
    # Verificar se o valor é positivo.

    # TODO 7:
    # Verificar se há saldo suficiente.

    # TODO 8:
    # Atualizar saldo.

    # TODO 9:
    # Registrar operação no extrato.

    print("Saque realizado com sucesso!")


# ----------------------------
# FUNÇÃO: ver_extrato
# ----------------------------
def ver_extrato():
    global extrato

    print("\n====== EXTRATO ======")

    # TODO 10:
    # Verificar se a lista está vazia.
    # Se estiver, informar que não há movimentações.

    # TODO 11:
    # Percorrer a lista e exibir as operações.


# ----------------------------
# FUNÇÃO PRINCIPAL
# ----------------------------
def main():

    while True:
        exibir_menu()
        opcao = input(AMARELO+"Escolha uma opção: "+RESET)

        # TODO 12:
        # Validar se a opção é numérica.

        opcao = int(opcao)

        if opcao == 1:
            consultar_saldo()

        elif opcao == 2:
            depositar()

        elif opcao == 3:
            sacar()

        elif opcao == 4:
            ver_extrato()

        elif opcao == 5:
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida!")


# ----------------------------
# EXECUÇÃO DO SISTEMA
# ----------------------------
main()
