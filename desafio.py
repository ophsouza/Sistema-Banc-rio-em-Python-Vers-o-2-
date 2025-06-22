# ===================== FUNÇÕES BÁSICAS =====================

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("✅ Depósito realizado com sucesso.")
    else:
        print("❌ Valor inválido para depósito.")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("❌ Saldo insuficiente.")
    elif valor > limite:
        print("❌ Saque excede o limite permitido.")
    elif numero_saques >= limite_saques:
        print("❌ Limite de saques diários atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("✅ Saque realizado com sucesso.")
    else:
        print("❌ Valor inválido.")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Sem movimentações." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=============================\n")


# ===================== USUÁRIOS E CONTAS =====================

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ").strip()
    usuario_existente = [u for u in usuarios if u["cpf"] == cpf]
    if usuario_existente:
        print("❌ Usuário já cadastrado com este CPF.")
        return

    nome = input("Nome completo: ").strip()
    nascimento = input("Data de nascimento (dd-mm-aaaa): ").strip()
    endereco = input("Endereço (logradouro, nro - bairro - cidade/UF): ").strip()

    usuarios.append({
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": nascimento,
        "endereco": endereco
    })

    print("✅ Usuário cadastrado com sucesso!")


def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if usuario:
        contas.append({
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        })
        print(f"✅ Conta criada com sucesso. Número: {numero_conta}")
        return numero_conta + 1
    else:
        print("❌ Usuário não encontrado. Cadastre-o primeiro.")
        return numero_conta


def listar_contas(contas):
    print("\n===== CONTAS CADASTRADAS =====")
    for conta in contas:
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}")
    print("==============================\n")


# ===================== MENU PRINCIPAL =====================

def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    LIMITE_VALOR = 500

    saldo = 0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        menu = """
========= MENU =========
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas
[q] Sair
=> """
        opcao = input(menu).strip().lower()

        if opcao == "d":
            valor = float(input("Valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=LIMITE_VALOR,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = criar_conta(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("✅ Encerrando o sistema. Até logo!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")


# Executa o programa
main()
