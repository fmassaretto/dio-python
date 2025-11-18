import Cliente
import Historico
import Saque
import Deposito

class Conta:
    _saldo: float = 0.0
    _num_conta: int = 0
    _agencia: str = ''
    _cliente: Cliente = None
    _historico: Historico = None
    
    # def __init__(self, cliente: Cliente):
    #     self.agencia = '0001'
    #     self.numero_conta = self.gerar_numero_conta()
    #     self._cliente = cliente
        
    def saldo(self):
        return self._saldo
    
    def nova_conta(self, cliente: Cliente, numero_conta: int):
        self._cliente = cliente
        self._num_conta = numero_conta
        self._agencia = '0001'
        
        return self
    
    def sacar(self, valor: float) -> bool:
        if valor > self._saldo:
            return False
        
        self._saldo -= valor
        self._historico.adicionar_transacao(Saque(valor))
        
        return True
    
    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            return False
        
        self._saldo += valor
        self._historico.adicionar_transacao(Deposito(valor))
        
        return True
        
    def gerar_numero_conta(self):
        Conta.num_conta += 1
        return Conta.num_conta