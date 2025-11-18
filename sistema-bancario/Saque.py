from Transacao import Transacao

class Saque(Transacao):
    _valor: float = 0.0
    
    def registrar(conta):
        Saque._valor = conta._valor