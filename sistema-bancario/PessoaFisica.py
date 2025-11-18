from Cliente import Cliente

class PessoaFisica (Cliente):
    
    def __init__(self,nome, cpf, lista_cpfs, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = self.verifica_cpf(cpf, lista_cpfs)
        self.data_nascimento = data_nascimento
        
    def verifica_cpf(self, cpf, lista_cpf):
        if cpf in lista_cpf:
            raise ValueError("CPF já cadastrado.")
        
        return cpf
        