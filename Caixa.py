# ==========================================
# SIMULADOR DE CAIXA ELETRÔNICO
# Nome: Vinícius Silva Xister
# Turma: 3 Tec
# ==========================================


#CORES
#========================
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
RESET = "\033[0m"
#========================


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


   # TODO 1:
   # Validar se a entrada é numérica.
   # Caso não seja, exibir mensagem de erro e retornar.


   while True:
       try:
           valor_str = input("Digite o valor para depósito: ")
           valor = float(valor_str)
           if valor<=0:
               print("O valor do depósito NÃO pode ser negativo ou zero")
           elif valor>0:
               print("Valor válido")
               break
       except ValueError:
           print("Valor Inválido")
          
          


   # TODO 2:
   # Verificar se o valor é positivo.
   # Caso não seja, exibir mensagem de erro e retornar.


   # TODO 3:
   # Atualizar o saldo.


   saldo = saldo+valor


   # TODO 4:
   # Registrar a operação na lista extrato.

   extrato.append(f"Depósito: + {valor}")
  
   print("Depósito realizado com sucesso!")




# ----------------------------
# FUNÇÃO: sacar
# ----------------------------
def sacar():
   global saldo
   global extrato


   # TODO 1:
   # Validar se a entrada é numérica.
   # Caso não seja, exibir mensagem de erro e retornar.


   # TODO 4:
   # Registrar a operação na lista extrato.


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


   print("\n====== EXTRATO ======\n")
   print(*extrato, sep="\n")


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


       try:
          
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
               print(VERMELHO+"Opção inválida!"+RESET)
       except ValueError:
           print(VERMELHO+"Opção Inválida"+RESET)




# ----------------------------
# EXECUÇÃO DO SISTEMA
# ----------------------------
main()





