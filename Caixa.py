

# ==========================================
# SIMULADOR DE CAIXA ELETRÔNICO
# Nome: Eloá Casarotto
# Turma: 3ºTec
# ==========================================

#Cores no terminal PY
VERMELHO = "\033[31m"
VERDE = "\033[032m"
AMARELO = "\033[033m"
AZUL = "\033[034m"
RESET = "\033[0m"

print("==========================================")
print("======SIMULADOR DE CAIXA ELETRÔNICO=======")
print("==========================================")



# ----------------------------
# VARIÁVEIS GLOBAIS
# ----------------------------
saldo = 1000.0
extrato = []
deposito = []


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
    if not valor_str.isdigit():
        print (VERMELHO+" Digite apenas números positivos! "+ RESET)
        

    else:
        print("Depósito realizado com sucesso!")

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
 
    try:
        valor = int(input("Digite o valor do saque:"))
        if valor <=0:
            print ("O saque deve ser maior que zero.")
       
        elif valor > saldo:
            print("Você não possui saldo suficiente.")
          
        else:
            print ("Saque efetuado.") 
    except ValueError:
        print ("Digite apenas números inteiros.")


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
        opcao_str = input("Escolha uma opção: ")
        if not opcao_str.isdigit():
            print(VERMELHO+"Opção inválida, digite apenas números!"+RESET)
            print("Apenas números maiores que zero")
            continue

        opcao = int(opcao_str)
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
            print (VERMELHO+"Escolha apenas 1, 2, 3, 4 ou 5"+RESET)


# ----------------------------
# EXECUÇÃO DO SISTEMA
# ----------------------------
main()
