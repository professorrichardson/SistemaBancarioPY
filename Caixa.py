# ==========================================
# SIMULADOR DE CAIXA ELETRÔNICO
# Nome: tiago
# Turma: técnico em desmvolvimento de sistemas
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

    # TODO 1: Validar se a entrada é numérica.
    if not valor_str.replace('.', '', 1).isdigit():
        print("Erro: valor inválido. Digite um número.")
        return

    valor = float(valor_str)

    # TODO 2: Verificar se o valor é positivo.
    if valor <= 0:
        print("Erro: o valor para depósito deve ser positivo.")
        return

    # TODO 3: Atualizar o saldo.
    saldo += valor

    # TODO 4: Registrar a operação na lista extrato.
    extrato.append(f"Depósito: R$ {valor:.2f}")

    print("Depósito realizado com sucesso!")


# ----------------------------
# FUNÇÃO: sacar
# ----------------------------
def sacar():
    global saldo
    global extrato

    valor_str = input("Digite o valor para saque: ")

    # TODO 5: Validar se a entrada é numérica.
    if not valor_str.replace('.', '', 1).isdigit():
        print("Erro: valor inválido. Digite um número.")
        return

    valor = float(valor_str)

    # TODO 6: Verificar se o valor é positivo.
    if valor <= 0:
        print("Erro: o valor para saque deve ser positivo.")
        return

    # TODO 7: Verificar se há saldo suficiente.
    if valor > saldo:
        print("Erro: saldo insuficiente.")
        return

    # TODO 8: Atualizar saldo.
    saldo -= valor

    # TODO 9: Registrar operação no extrato.
    extrato.append(f"Saque: R$ {valor:.2f}")

    print("Saque realizado com sucesso!")


# ----------------------------
# FUNÇÃO: ver_extrato
# ----------------------------
def ver_extrato():
    global extrato

    print("\n====== EXTRATO ======")

    # TODO 10: Verificar se a lista está vazia.
    if not extrato:
        print("Não há movimentações no extrato.")
        return

    # TODO 11: Percorrer a lista e exibir as operações.
    for operacao in extrato:
        print(operacao)


# ----------------------------
# FUNÇÃO PRINCIPAL
# ----------------------------
def main():

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        # TODO 12: Validar se a opção é numérica.
        if not opcao.isdigit():
            print("Erro: escolha uma opção válida.")
            continue

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