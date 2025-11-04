
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
lista_cpfs = []
usuarios = []

def menu():
    menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [u] Criar Usuário
        [cc] Criar Conta Corrente
        [e] Extrato
        [q] Sair
        => """
    
    return input(menu)

def depositar(saldo, extrato, /):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, limite, extrato, numero_saques, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo,extrato

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main(limite, saldo, extrato, numero_saques, LIMITE_SAQUES):
    while True:
        opcao = menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato = sacar(saldo=saldo, limite=limite, extrato=extrato, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "u":
            criar_usuario()
        
        elif opcao == "cc":
            criar_conta()
        
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def criar_conta():
    cpf = input("Informe o CPF do usuário para abertura da conta: ")
    usuario_encontrado = None
            
    for usuario in usuarios:
        if usuario.cpf == cpf:
            usuario_encontrado = usuario
            break
            
    if usuario_encontrado:
        conta = Conta(usuario_encontrado)
        print("Conta criada com sucesso!")
        print(f"Agência: {conta.agencia}")
        print(f"Número da Conta: {conta.numero_conta}")
    else:
        print("Usuário não encontrado, por favor cadastre o usuário antes de abrir uma conta.")

def criar_usuario():
    cpf = input("Informe o CPF (somente números): ")
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")
            
    try:
        usuario = Usuario(nome, cpf, lista_cpfs, data_nascimento, endereco)
        usuarios.append(usuario)
        lista_cpfs.append(cpf)
        print("Usuário cadastrado com sucesso!")
    except ValueError as e:
        print(e)
            
            
class Usuario:
    def __init__(self, nome, cpf, lista_cpfs, data_nascimento, endereco):
        self.nome = nome
        self.cpf = self.verifica_cpf(cpf, lista_cpfs)
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        
    def verifica_cpf(self, cpf, lista_cpf):
        if cpf in lista_cpf:
            raise ValueError("CPF já cadastrado.")
        
        return cpf
    
class Conta:
    num_conta = 0
    
    def __init__(self, usuario):
        self.agencia = '0001'
        self.numero_conta = self.gerar_numero_conta()
        self.usuario = usuario
        
    def gerar_numero_conta(self):
        Conta.num_conta += 1
        return Conta.num_conta

main(limite, saldo, extrato, numero_saques, LIMITE_SAQUES)