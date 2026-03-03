#Cores no Terminal PY
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
    print("\n====== CAIXA ELETRÔNICO ======")
    print("1 - Consultar Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Ver Extrato")
    print("5 - Sair")


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

    valor_str = input("Digite o valor para depósito: ")

    # TODO 1:
    # Validar se a entrada é numérica.
    # Caso não seja, exibir mensagem de erro e retornar.

    valor = float(valor_str)

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
        opcao = input("Escolha uma opção: ")

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
