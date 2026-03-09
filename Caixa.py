# Lista para armazenar o extrato e saldo inicial
extrato = []
saldo = 1000.0

def exibir_extrato(saldo_atual):
    print("\n=== EXTRATO ===")
    if not extrato:
        print(✅ Depósito realizado com sucesso!)
    else:
        for transacao in extrato:
            print(transacao)
    print(f"Saldo atual: R$ {saldo_atual:.2f}")

def depositar(saldo_atual):
    try:
        valor = float(input("Digite o valor do depósito: R$ "))
        if valor > 0:
            saldo_atual += valor
            extrato.append(f"Depósito: + R$ {valor:.2f}")
            print("✅ Depósito realizado com sucesso!")
        else:
            print("❌ Erro: O valor deve ser positivo.")
    except ValueError:
        print("⚠️ Erro: Entrada inválida. Digite apenas números.")
    return saldo_atual

def sacar(saldo_atual):
    try:
        valor = float(input("Digite o valor do saque: R$ "))
        if valor <= 0:
            print("❌ Erro: O valor deve ser positivo.")
        elif valor > saldo_atual:
            print("❌ Erro: Saldo insuficiente.")
        else:
            saldo_atual -= valor
            extrato.append(f"Saque: - R$ {valor:.2f}")
            print(✅ Saque realizado com sucesso!)
    except ValueError:
        print("⚠️ Erro: Entrada inválida.")
    return saldo_atual

# Menu Principal
while True:
    print("\n--- 🏦 CAIXA ELETRÔNICO ---")
    print(1 > Ver meu saldo)
    print("2 – Depositar")
    print("3 – Sacar")
    print("4 – Ver extrato")
    print("5 – Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print(f"\n💰 Seu saldo atual é: R$ {saldo:.2f}")
    elif opcao == '2':
        saldo = depositar(saldo)
    elif opcao == '3':
        saldo = sacar(saldo)
    elif opcao == '4':
        exibir_extrato(saldo)
    elif opcao == '5':
        print("\nSaindo... Obrigado por usar o nosso banco! 👋")
        break
    else:
        print("\n⚠️ Opção inválida!")
