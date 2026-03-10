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
senhaSecreta = 123456
limite_diario = 0
limite_diario_novo = 2000
sobra_limite = limite_diario_novo
opcao = 0

# ----------------------------
# FUNÇÃO: exibir_menu
# ----------------------------
def exibir_menu():
    print(AZUL+"\n====== CAIXA ELETRÔNICO ======"+RESET)
    print("1 - Consultar Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Ver Extrato")
    print("5 - Alterar Limite")
    print("6 - Sair")

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
    print(AZUL+"\n==============================="+RESET)
    print(VERDE+f"\nDepósito no valor de R${valor:.2f} realizado com sucesso!"+RESET)


# ----------------------------
# FUNÇÃO: sacar
# ----------------------------
def sacar():
    global saldo
    global extrato
    global limite_diario_novo
    global sobra_limite
    global limite_diario
  # TODO 5:
  # Validar se a entrada é numérica.

  # TODO 6:
  # Verificar se o valor é positivo.

  # TODO 7:
  # Verificar se há saldo suficiente.
    if saldo ==0:
       print(AMARELO+"\nNão há saldo disponível"+RESET)
       main(tentativas)
    if sobra_limite == 0:
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
                elif sobra_limite<valor:
                   print(VERMELHO+"Valor de saque diário excedido"+RESET)
                   print(AMARELO+f"Valor ainda disponível: {sobra_limite:.2f}"+RESET)
                elif valor>0 and valor<=saldo and valor<=sobra_limite:
                   print(VERDE+"\nValor válido"+RESET)
                   break
            except ValueError:
               print(VERMELHO+"Valor Inválido"+RESET)

  # TODO 8:
  # Atualizar saldo.

  # TODO 9:
  # Registrar operação no extrato.
    
    while True:
        confirmacao_str = input(VERDE+f"\nConfirma o saque no valor de {valor:.2f}?(digite 's' para SIM/digite 'n' para NÃO): "+RESET).lower()
        if confirmacao_str =="s":
            extrato.append(f"\nSaque: - {valor:.2f}")
            saldo = saldo - valor
            sobra_limite = sobra_limite - valor
            print(AZUL+"\n============================"+RESET)
            print(VERDE+"\nSaque realizado com sucesso!"+RESET)
            print(AMARELO+f"\nLimite de saque diário restante: {sobra_limite:.2f}"+RESET)
            print(AMARELO+f"\nSaldo disponível: {saldo:.2f}"+RESET)
            break
        
        elif confirmacao_str=="n":
            print(AZUL+"\n==============="+RESET)
            print(VERDE+"\nSaque cancelado"+RESET)
            print(AZUL+"\n==============="+RESET)
            break

        else:
            print(AZUL+"\nDigite 's' ou 'n'"+RESET)


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
        print(AMARELO+"Não foi realizado nenhum depósito ou saque até o momento :)"+RESET)


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
               senha = str(input(VERDE+"\nDigite a Senha: "+RESET))
            else:
               senha = str(input(VERDE+"\nDigite a Senha(6 dígitos): "+RESET))
            senha_int = int(senha)
            if senha_int != senhaSecreta:
                if len(senha)<6 or len(senha)>6:
                    print("\nA senha deve conter 6 dígitos numéricos")
                else:
                    print(VERMELHO+"\nSenha incorreta! "+ AZUL+"Tente novamente"+RESET)
                    print(AMARELO+f"Tentativas restantes: {total_tentativas-tentativas}"+RESET)
                    tentativas = tentativas +1
               
            elif senha_int == senhaSecreta:
                print(AZUL+"\n=================================="+RESET)
                print(VERDE+"\nSenha correta! Iniciando sistema!"+RESET)
                break
          
        except ValueError:
            print(VERMELHO+"\nNão são válidos espaços em branco e letras!"+RESET)
    main(tentativas)

def limite():
    global a
    global limite_diario
    global limite_diario_novo
    global sobra_limite
    entrada = "" 
    print(AZUL+"\nPara alterar seu limite de saque diário, é necessário digitar um cpf válido"+RESET)
    while True:
        try:
            entrada = input("\nDigite o cpf: ")
            if len(entrada)<11:
                print(VERMELHO+"\nO CPF deve conter 11 dígitos"+RESET)
            else: break

        except ValueError:
            print(VERMELHO+"\nErro"+RESET)

    for n in entrada:
        if not n.isdigit():
            print(VERMELHO+"\nNão são aceitos caracteres no CPF"+RESET)
            limite()

    lista1 = [int(n) for n in list(entrada)]
    lista2 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    lista1.pop(9)
    lista1.pop(9)

    a = 0
    soma = 0
    while a != 9:
        resultado = lista1[a]*lista2[a]
        soma = soma + resultado
        a = a+1
            
    sobra = soma % 11
    if sobra == 0 or sobra ==1:
        num1 = 0
    elif sobra > 1:
        num1 = 11 - sobra


    lista1.append(num1)
    lista2.insert(0, 11)

    soma = 0
    a = 0
    resultado = 0
    while a != 10:
        resultado = lista1[a]*lista2[a]
        soma = soma + resultado
        a = a+1

    sobra = soma % 11
    if sobra == 0 or sobra==1:
        num2 = 0
    elif sobra>1:
        num2 = 11 - sobra

    lista1.append(num2)

    lista_formatada = "".join(map(str, lista1))
    entrada_formatada = "".join(map(str, entrada))


    if lista_formatada == entrada_formatada:
        print(VERDE+"\nCPF Válido"+RESET)
        validez = 1
    else:
        print(VERMELHO+"\nInválido"+RESET)
        main(tentativas)
        validez = 0
    if validez == 1:
        limite_diario = limite_diario_novo
        while True:
            try:
                limite_diario_novo = float(input(AZUL+f"\nDefina o novo limite diário (atual = {limite_diario:.2f}): "+RESET))
                if limite_diario_novo<=0:
                    print(VERMELHO+"\nO valor do limite NÃO pode ser negativo ou zero"+RESET)
                elif limite_diario_novo<=sobra_limite:
                    print(VERDE+"\nvalor válido"+RESET)

                    sobra_limite = (limite_diario_novo)

                    print(AZUL+"================================="+RESET)
                    print(VERDE+f"\nNovo limite definido: {limite_diario_novo:.2f}"+RESET)
                    print(VERDE+f"\nLimite de saque ainda disponível: {sobra_limite:.2f}"+RESET)
                    main(tentativas)
                elif limite_diario_novo>0:
                    print("\nValor válido")
                    break
            except ValueError:
                print(VERMELHO+"Valor Inválido"+RESET)
        
        sobra_limite = (limite_diario_novo - limite_diario) + sobra_limite  
        print(AZUL+"================================="+RESET)
        print(VERDE+f"\nNovo limite definido: {limite_diario_novo:.2f}"+RESET)
        print(VERDE+f"\nLimite de saque ainda disponível: {sobra_limite:.2f}"+RESET)
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



            elif opcao ==5:
                limite()




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

def inicia():
    global opcao

    if opcao==0:
        senha()
    else:
        print
        
inicia()











