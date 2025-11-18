import Conta

class Cliente:
    _endereco: str = ''
    _contas: list[Conta] = []
    
    def __init__(self, endereco):
        self.endereco = endereco
        
    def realizar_transacao(self, conta: Conta, transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta: Conta):
        self._contas.append(conta)