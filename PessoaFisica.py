import Pessoa

class PessoaFisica(Pessoa):

    def __init__(self, nome, idade, codigo_banco, cpf):
        super().__init__(nome, idade, codigo_banco, cpf)
        self.cpf = cpf