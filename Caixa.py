# ==========================================
# SIMULADOR DE CAIXA ELETRÔNICO
# Nome: Nicolas, Guilherme, Pedro
# Turma: 3° tec
# ==========================================




# ----------------------------
# VARIÁVEIS GLOBAIS
# ----------------------------
saldo = 1000.0
extrato = []




# ----------------------------
# FUNÇÃO: realizar_cadastro (LOGIN)
# ----------------------------
def realizar_cadastro():
    print(" --- CADASTRO INICIAL --- ")
    while True:
        try:
            login_usuario = input("Digite seu novo login: ")
            senha_usuario = input("Digite sua nova senha (mínimo 6 caracteres): ")


            if len(login_usuario) < 1:
                print("Erro: Login não pode estar vazio.")
            elif len(senha_usuario) < 6:
                print("Erro: Senha deve ter no mínimo 6 caracteres.")
            else:
                print("\nLogin e senha cadastrados com sucesso!")
                print(f"Bem-vindo ao sistema, {login_usuario}!")
                return login_usuario  # Retorna o nome para o sistema saber quem logou


        except ValueError:
            print("Ocorreu um erro inesperado. Por favor, tente novamente.")




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
# FUNÇÕES DE OPERAÇÃO
# ----------------------------
def consultar_saldo():
    global saldo
    print(f"\nSaldo atual: R$ {saldo:.2f}")




def depositar():
    global saldo
    global extrato
    valor_str = input("Digite o valor para depósito: ")
    try:
        valor = float(valor_str)
        if valor <= 0:
            print("Valor inválido! O valor deve ser positivo.")
            return
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    except ValueError:
        print("Valor inválido! Por favor, digite um número.")




def sacar():
    global saldo
    global extrato
    valor_str = input("Digite o valor para saque: ")
    try:
        valor = float(valor_str)
        if valor <= 0:
            print("Valor inválido! O valor deve ser positivo.")
            return
        if valor > saldo:
            print("Saldo insuficiente!")
            return
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        print("Saque realizado com sucesso!")
    except ValueError:
        print("Valor inválido! Por favor, digite um número.")




def ver_extrato():
    global extrato
    print("\n====== EXTRATO ======")
    if not extrato:
        print("Não há movimentação para exibir")
        return
    for operacao in extrato:
        print(operacao)




# ----------------------------
# FUNÇÃO PRINCIPAL
# ----------------------------
def main():
    # 1º Passo: O login aparece aqui, antes de qualquer coisa
    usuario = realizar_cadastro()


    # 2º Passo: Entra no loop do menu
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")


        if not opcao.isdigit():
            print("Opção inválida. Por favor, digite um número.")
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
            print(f"Encerrando sistema... Até logo, {usuario}!")
            break
        else:
            print("Opção inválida!")




# ----------------------------
# EXECUÇÃO DO SISTEMA
# ----------------------------
if __name__ == "__main__":
    main()



