# ==========================================
# SIMULADOR DE CAIXA ELETRÔNICO
# Nome: Pamela Raiane
# Turma: 3º Técnico
# ==========================================

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

    if not valor_str.replace(".", "", 1).isdigit():
        print(VERMELHO + "Valor inválido." + RESET)
        return

    valor = float(valor_str)

    if valor <= 0:
        print(VERMELHO + "O valor deve ser positivo." + RESET)
        return

    saldo = saldo + valor

    extrato.append(f"Depósito: +R$ {valor:.2f}")

    print(VERDE + "Depósito realizado com sucesso!" + RESET)


# ----------------------------
# FUNÇÃO: sacar
# ----------------------------
def sacar():
    global saldo
    global extrato

    valor_str = input("Digite o valor para saque: ")

    if not valor_str.replace(".", "", 1).isdigit():
        print(VERMELHO + "Valor inválido." + RESET)
        return

    valor = float(valor_str)

    if valor <= 0:
        print(VERMELHO + "O valor deve ser positivo." + RESET)
        return

    if valor > saldo:
        print(VERMELHO + "Saldo insuficiente." + RESET)
        return

    saldo = saldo - valor

    extrato.append(f"Saque: -R$ {valor:.2f}")

    print(VERDE + "Saque realizado com sucesso!" + RESET)


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