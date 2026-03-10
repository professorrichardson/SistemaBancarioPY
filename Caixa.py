# ==========================================
# SIMULADOR DE CAIXA ELETRÔNICO
# Nome:
# Turma:
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
"Implementação da funcionalidade de saque com validação"
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
# FUNÇÃO: sacargit commit -m "Implementação da funcionalidade de saque com validação"
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


def ver_extrato():
    global extrato
    global saldo

    print("\n====== EXTRATO ======")
    
    # TODO 10: Verificar se a lista está vazia
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        # TODO 11: Percorrer a lista e exibir
        for operacao in extrato:
            print(operacao)
    
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("======================")
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


