# ==========================================
# SIMULADOR DE CAIXA ELETRÔNICO
# Nome: Nicolas, Guilherme, Pedro
# Turma:3° Tecnico em Desenvolvimento de Sistema
# ==========================================

# ----------------------------
# VARIÁVEIS GLOBAIS
# ----------------------------
saldo = 3000.0
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
     # Tenta converter para float para aceitar inteiros e decimais
    try:
        valor = float(valor_str)
        print(f"entrada valida {valor}")
     
    except ValueError:
        # Se falhar, exibe erro e retorna
        print("Valor inválido! Por favor, digite um número.")
        return

    valor = float(valor_str)

    # TODO 2:
    if valor <= 0:
        # 2. Exibir mensagem de erro
        print("Valor inválido! O valor deve ser positivo.")
        #retorna
        return
    print(f"Processando o valor positivo {valor}")

    # TODO 3:
    saldo += valor
    print(f"Novo saldo após depósito: R$ {saldo:.2f}")

    # TODO 4:
    extrato.append(f"Depósito: R$ {valor:.2f}")

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
    try:
        #tenta converter para float para aceitar inteiros e decimais
        valor = float(valor_str)
        print(f"entrada valida {valor}")
     
    except ValueError:
        # Se falhar, exibe erro e retorna
        print("Valor inválido! Por favor, digite um número.")
        return

    valor = float(valor_str)

    # TODO 6:
    if valor <= 0:
        # Exibir mensagem de erro e retornar
        print("Valor inválido! O valor deve ser positivo.")
        # interroper a execução aqui mesmo para o resto do código não ser executado
        return
    # se for positivo, exibe mensagem de processamento
    print(f"Processando o valor positivo {valor}")

    # TODO 7:
    # Verificar se há saldo suficiente.
    if valor > saldo:
        # Se não houver, exibir mensagem de erro e retornar
        print("Saldo insuficiente! Operação cancelada.")
        return
    print(f"Saldo suficiente para o saque de {valor}")

    # TODO 8:
    #atualiza o saldo subtraindo o valor do saque
    saldo -= valor
    #exibe o novo saldo após o saque
    print(f"Novo saldo após saque: R$ {saldo:.2f}")

    # TODO 9:
    extrato.append(f"Saque: R$ {valor:.2f}")

    print("Saque realizado com sucesso!")


# ----------------------------
# FUNÇÃO: ver_extrato
# ----------------------------
def ver_extrato():
    global extrato

    print("\n====== EXTRATO ======")

    # TODO 10:

    # Verifica se a lista está vazia
    if not extrato:
        print("Não há movimentações para exibir.")
    else:
            # Processa a lista se não estiver vazia
        print(f"Movimentações encontradas: {len(extrato)}")

    # TODO 11:
    # Percorrer a lista e exibir as operações.
    if not extrato:
        print("Não há movimentações para exibir.")
    else:
        for operacao in extrato:
            print(operacao)


# ----------------------------
# FUNÇÃO PRINCIPAL
# ----------------------------
def main():

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        # TODO 12:
        # Validar se a opção é numérica.
        try:
            # Tenta converter a variável 'opcao' (que provavelmente veio de um input)
            # para um número inteiro (int).
            opcao = int(opcao)
            # Se a conversão for bem-sucedida, exibe a opção válida.
            print(f"Opção válida: {opcao}")
        except ValueError:
            # Se a conversão falhar (ex: usuário digitou letras),
            # o código cai aqui e evita que o programa trave.
            print("Opção inválida! Por favor, digite um número.")
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
