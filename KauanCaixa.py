import random

#Cores no Terminal PY
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
RESET = "\033[0m"

# ==========================================
# SIMULADOR DE CAIXA ELETRÔNICO
# Nome: Kauan Stipp 
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
    print(AZUL + "\n====== CAIXA ELETRÔNICO ======" + RESET)
    print(AZUL + "1 - Consultar Saldo" + RESET)
    print(AZUL + "2 - Depositar" + RESET)
    print(AZUL + "3 - Sacar" + RESET)
    print(AZUL + "4 - Ver Extrato" + RESET)
    print(AZUL + "5 - Sair" + RESET)


# ----------------------------
# FUNÇÃO: consultar_saldo
# ----------------------------
def consultar_saldo():
    global saldo
    print(AMARELO + f"\nSaldo atual: R$ {saldo:.2f}" + RESET)


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

    if not valor_str.replace(".", "", 1).isdigit():
        print(VERMELHO + "Valor inválido." + RESET)
        return

    valor = float(valor_str)

    # TODO 2:
    # Verificar se o valor é positivo.
    # Caso não seja, exibir mensagem de erro e retornar.

    if valor <= 0:
        print(VERMELHO + "O valor deve ser positivo." + RESET)
        return

    # TODO 3:
    # Atualizar o saldo.

    saldo = saldo + valor

    # TODO 4:
    # Registrar a operação na lista extrato.

    extrato.append(f"Depósito: +R$ {valor:.2f}")

    print(VERDE + "Depósito realizado com sucesso!" + RESET)


# ----------------------------
# FUNÇÃO: sacar
# ----------------------------
def sacar():
    global saldo
    global extrato

    valor_str = input("Digite o valor para saque: ")

    # TODO 5:
    # Validar se a entrada é numérica.

    if not valor_str.replace(".", "", 1).isdigit():
        print(VERMELHO + "Valor inválido." + RESET)
        return

    valor = float(valor_str)

    # TODO 6:
    # Verificar se o valor é positivo.

    if valor <= 0:
        print(VERMELHO + "O valor deve ser positivo." + RESET)
        return

    # TODO 7:
    # Verificar se há saldo suficiente.

    if valor > saldo:
        print(VERMELHO + "Saldo insuficiente." + RESET)
        return

    # TODO 8:
    # Atualizar saldo.

    saldo = saldo - valor

    # TODO 9:
    # Registrar operação no extrato.

    extrato.append(f"Saque: -R$ {valor:.2f}")

    print(VERDE + "Saque realizado com sucesso!" + RESET)


# ----------------------------
# FUNÇÃO: ver_extrato
# ----------------------------
def ver_extrato():
    global extrato

    print(AMARELO + "\n====== EXTRATO ======" + RESET)

    # TODO 10:
    # Verificar se a lista está vazia.
    # Se estiver, informar que não há movimentações.

    if len(extrato) == 0:
        print(VERMELHO + "Nenhuma movimentação realizada." + RESET)
        return

    # TODO 11:
    # Percorrer a lista e exibir as operações.

    for operacao in extrato:
        print(AMARELO + operacao + RESET)


# ----------------------------
# FUNÇÃO PRINCIPAL
# ----------------------------
def main():

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        # TODO 12:
        # Validar se a opção é numérica.

        if not opcao.isdigit():
            print(VERMELHO + "Entrada inválida. Digite um número." + RESET)
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
            print(AZUL + "Encerrando sistema..." + RESET)
            break

        else:
            print(VERMELHO + "Opção inválida!" + RESET)


# ----------------------------
# EXECUÇÃO DO SISTEMA
# ----------------------------
main()