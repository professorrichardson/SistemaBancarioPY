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
   try:
       numero = float(valor_str)
   except ValueError:
       print("Valor inválido! Por favor, digite um número.")
       return


   valor = float(valor_str)


   # TODO 2:
   if valor <= 0:
       print("Valor invalido! O valor deve ser positivo.")
       return


   # TODO 3:
   saldo += valor


   # TODO 4:
   extrato.append(f"deposito: R$ {valor:.2f}")
   print("Depósito realizado com sucesso!")




# ----------------------------
# FUNÇÃO: sacar
# ----------------------------
def sacar():
   global saldo
   global extrato


   valor_str = input("Digite o valor para saque: ")


   # TODO 5:
   try:
       numero = float(valor_str)
   except ValueError:
       print("valor invalido! Por favor, digite um numero.")
       return


   valor = float(valor_str)


   # TODO 6:
   if valor <= 0:
       print("Valor invalido! O valor deve ser positivo.")
       return


   # TODO 7:
   if valor > saldo:
       print("Saldo insuficiene!")
       return


   # TODO 8:
   saldo -= valor


   # TODO 9:
   extrato.append(f"saque: R$ {valor:.2f}")




   print("Saque realizado com sucesso!")

# ----------------------------
# FUNÇÃO: ver_extrato
# ----------------------------
def ver_extrato():
   global extrato


   print("\n====== EXTRATO ======")


   # TODO 10:
   if not extrato:
       print("Não há movimentação para exibir")
       return


   # TODO 11:
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
       if not opcao.isdigit():
           print("Opção invalida. Porfavor tente novamente.")


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
if __name__ == "__main__":
   main()



