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
senhaSecreta = 12345
valid0 = 0




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
   print(f"\n"+VERDE+"Saldo atual: R$ "+AMARELO+ f"{saldo:.2f}"+RESET)




# ----------------------------
# FUNÇÃO: depositar
# ----------------------------
def depositar():
   global saldo
   global extrato


   # TODO 1:
   # Validar se a entrada é numérica.
   # Caso não seja, exibir mensagem de erro e retornar.

   # TODO 2:
   # Verificar se o valor é positivo.
   # Caso não seja, exibir mensagem de erro e retornar.


   while True:
       try:
           valor_str = input(VERDE+"Digite o valor para depósito: "+RESET)
           valor = float(valor_str)
           if valor<=0:
               print(VERMELHO+"O valor do depósito NÃO pode ser negativo ou zero"+RESET)
           elif valor>0:
               print("Valor válido")
               break
       except ValueError:
           print(VERMELHO+"Valor Inválido"+RESET)
          
   # TODO 3:
   # Atualizar o saldo.


   saldo = saldo+valor


   # TODO 4:
   # Registrar a operação na lista extrato.

   extrato.append(f"Depósito: + {valor:.2f}")
  
   print(VERDE+"Depósito realizado com sucesso!"+RESET)



# ----------------------------
# FUNÇÃO: sacar
# ----------------------------
def sacar():
   global saldo
   global extrato


   # TODO 5:
   # Validar se a entrada é numérica.

   # TODO 6:
   # Verificar se o valor é positivo.

   # TODO 7:
   # Verificar se há saldo suficiente.


   while True:
       try:
            valor_str = input("Digite o valor para saque: ")
            valor = float(valor_str)
            if valor<=0:
               print(VERMELHO+"O valor do saque NÃO pode ser negativo ou zero"+RESET)
            elif valor>saldo:
                print(VERMELHO+"Saldo insuficiente"+RESET)
            elif valor>0 and valor<=saldo:
               print("Valor válido")
               break
       except ValueError:
           print(VERMELHO+"Valor Inválido"+RESET)


   # TODO 8:
   # Atualizar saldo.


   saldo = saldo - valor


   # TODO 9:
   # Registrar operação no extrato.

   extrato.append(f"\nSaque: - {valor:.2f}")
  
   print(VERDE+"Saque realizado com sucesso!"+RESET)


# ----------------------------
# FUNÇÃO: ver_extrato
# ----------------------------
def ver_extrato():
    global extrato

   # TODO 10:
   # Verificar se a lista está vazia.
   # Se estiver, informar que não há movimentações.
   
    if not extrato:
       print(AZUL+"\n====== EXTRATO ======\n"+RESET)
       print(AMARELO+"Não foi realizado nenhum depósito ou saque até )o momento"+RESET)

   # TODO 11:
   # Percorrer a lista e exibir as operações.

    elif extrato:
        print(AZUL+"\n====== EXTRATO ======\n"+RESET)
        print(*extrato, sep="\n")


# ----------------------------
# FUNÇÃO PRINCIPAL
# ----------------------------
def main():
    global senhaSecreta
    tentativas = 1
    total_tentativas = 3
    print(AZUL+"\n====== CAIXA ELETRÔNICO ======"+RESET)
    print(AZUL+"\n==== SENHA REQUERIDA ===="+RESET)
    while tentativas < 4:
        try:
            senha_str = input(VERDE+"\nDigite a Senha: "+RESET)
            senha = int(senha_str)
            if senha != senhaSecreta:
                print(VERMELHO+"Senha incorreta! "+ AZUL+"Tente novamente"+RESET)
                print(AMARELO+f"Tentativas restantes: {total_tentativas-tentativas}"+RESET)
                tentativas = tentativas +1
            elif senha == senhaSecreta:
                print("Senha correta! Iniciando sistema!")
                break
        except ValueError:
            print("Erro")
            

    while True:


        try:
            if tentativas== 4:
                print(VERMELHO+"Número de tentativas excedidas. Encerrando sistema"+RESET)
                break
          
            exibir_menu()
            opcao = input("Escolha uma opção: ")

            opcao = int(opcao)

            # TODO 12:
            # Validar se a opção é numérica.

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
        except ValueError:
            print(VERMELHO+"Opção Inválida"+RESET)




# ----------------------------
# EXECUÇÃO DO SISTEMA
# ----------------------------
main()





