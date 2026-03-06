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
limite_diario = 2000.00



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
           valor_str = input(VERDE+"\nDigite o valor para depósito: "+RESET)
           valor = float(valor_str)
           if valor<=0:
               print(VERMELHO+"O valor do depósito NÃO pode ser negativo ou zero"+RESET)
           elif valor>0:
               print("\nValor válido")
               break
       except ValueError:
           print(VERMELHO+"Valor Inválido"+RESET)
          
   # TODO 3:
   # Atualizar o saldo.


   saldo = saldo+valor


   # TODO 4:
   # Registrar a operação na lista extrato.

   extrato.append(f"\nDepósito: + {valor:.2f}")
  
   print(VERDE+"\nDepósito realizado com sucesso!"+RESET)



# ----------------------------
# FUNÇÃO: sacar
# ----------------------------
def sacar():
    global saldo
    global extrato
    global limite_diario

   # TODO 5:
   # Validar se a entrada é numérica.

   # TODO 6:
   # Verificar se o valor é positivo.

   # TODO 7:
   # Verificar se há saldo suficiente.
    if limite_diario == 0:
        print(AMARELO+"\nSeu limite diário acabou :(. Para sacar novamente, altere o valor de saque diário ou volte outro dia."+RESET)
        main(tentativas)
    else:
        while True:
            try:
                valor_str = input(VERDE+"\nDigite o valor para saque: "+RESET)
                valor = float(valor_str)
                if valor<=0:
                    print(VERMELHO+"O valor do saque NÃO pode ser negativo ou zero"+RESET)
                elif valor>saldo:
                    print(VERMELHO+"Saldo insuficiente. Verifique seu saldo"+RESET)
                elif (limite_diario-valor)<0:
                    print(VERMELHO+"Valor de saque diário excedido"+RESET)
                    print(AMARELO+f"Valor ainda disponível: {limite_diario:.2f}"+RESET)
                elif valor>0 and valor<=saldo:
                    print(VERDE+"\nValor válido"+RESET)
                    break
            except ValueError:
                print(VERMELHO+"Valor Inválido"+RESET)


   # TODO 8:
   # Atualizar saldo.

 
   # TODO 9:
   # Registrar operação no extrato.
    confirmacao_str = input(VERDE+f"\nConfirma o saque no valor de {valor:.2f}?(digite 's' para SIM/digite 'n' para NÃO): "+RESET).lower()
    if confirmacao_str =="s":
        extrato.append(f"\nSaque: - {valor:.2f}")
        saldo = saldo - valor
        limite_diario = limite_diario - valor
        print(VERDE+"\nSaque realizado com sucesso!"+RESET)
        print(VERDE+f"\nLimite de saque diário restante: {limite_diario:.2f}"+RESET)
        
    elif confirmacao_str=="n":
        print(VERDE+"Saque cancelado"+RESET)
        


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
        print(AZUL+"\n====== EXTRATO ======"+RESET)
        for historico in extrato:
            print(historico)


def senha():
    global senhaSecreta
    global tentativas
    tentativas = 1
    total_tentativas = 3
    print(AZUL+"\n====== CAIXA ELETRÔNICO ======"+RESET)
    print(AZUL+"\n==== SENHA REQUERIDA ===="+RESET)
    while tentativas <= total_tentativas:
        try:
            if  tentativas == 3:
                print(VERMELHO+"\nAPENAS 1 TENTATIVA RESTANTE"+RESET)
                senha_str = input(VERDE+"Digite a Senha: "+RESET)
                senha = int(senha_str)
            else:
                senha_str = input(VERDE+"\nDigite a Senha(6 dígitos): "+RESET)
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
    main(tentativas)


# ----------------------------
# FUNÇÃO PRINCIPAL
# ----------------------------
def main(tentativas):
    
    while True:
        

        try:
            if tentativas == 4:
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




            elif opcao == 6:
               print(AZUL+"Encerrando sistema..."+RESET)
               break
            else:
               print(VERMELHO+"Opção inválida!"+RESET)
        except ValueError:
            print(VERMELHO+"Opção Inválida"+RESET)




# ----------------------------
# EXECUÇÃO DO SISTEMA
# ----------------------------
senha()





