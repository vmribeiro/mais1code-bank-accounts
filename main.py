class Pessoa(object):

    def __init__(self, nome, idade, codigo_banco):
        self.nome = nome
        self.idade = idade
        self.codigo_banco = codigo_banco
    
    def depositar(valor):
        print('Valor depositado')

    def exibir_saldo():
        print('Saldo de 10.00')


class PessoaFisica(Pessoa):

    def __init__(self, nome, idade, codigo_banco, cpf):
        super().__init__(nome, idade, codigo_banco)
        self.cpf = cpf


class PessoaJuridica(Pessoa):

    def __init__(self, nome, idade, codigo_banco, cnpj):
        super().__init__(nome, idade, codigo_banco)
        self.cnpj = cnpj


pessoa1 = PessoaFisica(nome = 'Joao', idade = 25, codigo_banco = 20, cpf = '123.123.123-53')
pessoa2 = PessoaJuridica(nome = 'Jonas LTDA', idade = 20, codigo_banco = 40, cnpj = '222.222.222/2222-22')

print(type(pessoa1))
print(type(pessoa2))