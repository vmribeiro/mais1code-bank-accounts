from Pessoa import Pessoa

class PessoaJuridica(Pessoa):

    def __init__(self, nome, idade, codigo_banco, cnpj):
        super().__init__(nome, idade, codigo_banco)
        self.cnpj = cnpj
