
# ==========================================
# SIMULADOR DE CAIXA ELETRÔNICO
# Nome: Laura Menegazzo Boeing
# Turma: 3ºTec
# ==========================================

#Cores no terminal PY
VERMELHO = "\033[31m"
VERDE = "\033[032m"
AMARELO = "\033[033m"
AZUL = "\033[034m"
RESET = "\033[0m"

print(AZUL+"=========================================="+RESET)
print(AZUL+"======SIMULADOR DE CAIXA ELETRÔNICO======="+RESET)
print(AZUL+"=========================================="+RESET)



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
    print(AZUL+"\n====== CAIXA ELETRÔNICO ======\n"+RESET)
    print("1 - Consultar Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Ver Extrato")
    print("5 - Sair\n")


# ----------------------------
# FUNÇÃO: consultar_saldo
# ----------------------------

def consultar_saldo():
    global saldo
    print(AMARELO+f"\nSaldo atual: R$ {saldo:.2f}"+RESET)


# ----------------------------
# FUNÇÃO: depositar
# ----------------------------
def depositar():
    global saldo
    global extrato

    try:
        valor_str = input(AMARELO+"Digite o valor para depósito: "+RESET)

        if valor_str == 0:
            saldo+= valor_str
            print(VERMELHO+"O caixa só aceita números positivos!"+RESET)
            return

        valor_str = float(valor_str)

        if valor_str <= 0:
            print(VERMELHO+"O valor deve ser maior que zero!"+RESET)
            return
    except ValueError:
        print(VERMELHO+"Digite apenas números!"+RESET)
        return

       
    valor = float(valor_str)

    if valor <= 0:
          print(VERMELHO+"O caixa só aceita números positivos!"+RESET)

    else:
        print(VERDE+"Depósito realizado com sucesso!"+RESET)
         

    valor = float(valor)


    extrato.append("Depósito: +R$ {:.2f}".format(valor))
    
    saldo = saldo + valor


# ----------------------------
# FUNÇÃO: sacar
# ----------------------------
def sacar():
    global saldo
    global extrato

    valor_str = input(AMARELO+"Digite o valor para saque: "+RESET)

    try:
        valor = float(valor_str)  # Converte para float
    except ValueError:
        print(VERMELHO+"Erro: Digite um valor numérico válido!"+RESET)
        return

    if valor > saldo:
        print(VERMELHO+"Saldo insuficiente para saque!"+RESET)
        return
    elif valor > 1000:
        print(VERMELHO+"O caixa não permite saque maior que R$ 1000."+RESET)
        return
    elif valor <= 0:
        print(VERMELHO+"O caixa só aceita números positivos!"+RESET)
        return
    else:
        saldo -= valor
        extrato.append(f"Saque: -R$ {valor:.2f}")
        print(VERDE+"Saque realizado com sucesso!"+RESET)
        return

    valor = float(valor_str)

    print(VERDE+"Saque realizado com sucesso!"+RESET)

# ----------------------------
# FUNÇÃO: ver_extrato
# ----------------------------
def ver_extrato():
    global saldo
    global extrato

    print(AZUL+"\n====== EXTRATO ======"+RESET)
    if len (extrato) == 0:
       print (VERMELHO+"Nenhuma operação realizada"+RESET)

    else:
      for operacao in extrato:
          print(operacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")

# ----------------------------
# FUNÇÃO PRINCIPAL
# ----------------------------
def main():

    while True:
        exibir_menu()
        opcao_str = input(AZUL+"Escolha uma opção: "+RESET)
        if not opcao_str.isdigit():
            print(VERMELHO+"Opção inválida, digite apenas números!"+RESET)
            print(VERMELHO+"Apenas números maiores que zero"+RESET)
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
