from datetime import date
from Conta import Conta

class ContaCorrente(Conta):
    _limite: float = 500.0
    _limite_saques: int = 3
        
        