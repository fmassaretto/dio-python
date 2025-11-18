import Transacao

class Historico():
    def adiconar_transacao(self, transacao: Transacao):
        transacao.registrar()