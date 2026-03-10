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
senha_secreta = 200909
limite_diario = 3

def senha():
    while True:
        try:
            senha = int(input(AMARELO+"Digite a sua senha: "+RESET))
            if senha == senha_secreta:
                print(VERDE+"Senha correta!"+RESET)
                main()
            elif senha!=senha_secreta:
                print(VERMELHO+" Senha incorreta: tente novamente "+RESET)
        except ValueError:
            print(VERMELHO+"Erro"+RESET)

# ----------------------------
# FUNÇÃO: exibir_menu
# ----------------------------
def exibir_menu():
    print(AZUL+"\n====== CAIXA ELETRÔNICO ======"+RESET)
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
    print(AZUL+f"\nSaldo atual: R$ {saldo:.2f}"+RESET)


# ----------------------------
# FUNÇÃO: depositar
# ----------------------------
def depositar():
    global saldo
    global extrato
    while True:
        try:

            valor_str = float(input("Digite o valor para depósito: "))

            # TODO 1:
            # Validar se a entrada é numérica.
            # Caso não seja, exibir mensagem de erro e retornar.
            
            if valor_str<=0:
                print(VERMELHO+"Erro: Digite apenas numeros positivos!"+RESET)

            else:
                break
        except ValueError:
            print(VERMELHO+"Erro: Digite apenas números!"+RESET)
    # TODO 2:
    # Verificar se o valor é positivo.
    # Caso não seja, exibir mensagem de erro e retornar.
    


    valor = float(valor_str)

    saldo += valor
    extrato.append(AZUL+f"Depósito: + R${valor:.2f}"+RESET)
    print(VERDE+f"Depósito de R${valor:.2f} foi realizado com sucesso!"+RESET)

    # TODO 3:
    # Atualizar o saldo.

    # TODO 4:
    # Registrar a operação na lista extrato.



# ----------------------------
# FUNÇÃO: sacar
# ----------------------------
def sacar():
    global saldo
    global extrato

    while True:
        try:

            valor_str = float(input("Digite o valor para sacar: "))

            # TODO 1:
            # Validar se a entrada é numérica.
            # Caso não seja, exibir mensagem de erro e retornar.
            
            if valor_str<=0:
                print(VERMELHO+"Erro: Digite apenas numeros positivos!"+RESET)

            else:
                break
        except ValueError:
            print(VERMELHO+"Erro: Digite apenas números!"+RESET)

    # TODO 5:
    # Validar se a entrada é numérica.

    valor = float(valor_str)


    saldo -= valor
    extrato.append(AMARELO+f"Saque: - R${valor:.2f}"+RESET)
    print(VERDE+f" Saque de R${valor:.2f} foi realizado com sucesso!"+RESET)


    # TODO 6:
    # Verificar se o valor é positivo.

    # TODO 7:
    # Verificar se há saldo suficiente.

    # TODO 8:
    # Atualizar saldo.

    # TODO 9:
    # Registrar operação no extrato.



# ----------------------------
# FUNÇÃO: ver_extrato
# ----------------------------
def ver_extrato():
    global extrato

   
    
    if not extrato:
        print(AZUL+"\n ===== EXTRATO =====\n"+RESET)
        print(VERDE+" Não foi realizado nenhum depósito ou saque "+RESET)

    else:
        print("\n====== EXTRATO ======")
        for n in (extrato):
            print("\n",n)
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
            print(AZUL+"Encerrando sistema..."+RESET)
            break

        else:
            print(VERMELHO+"Opção inválida!"+RESET)


# ----------------------------
# EXECUÇÃO DO SISTEMA
# ----------------------------

senha()
