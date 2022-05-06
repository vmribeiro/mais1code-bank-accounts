# from {nome_do_arquivo} import {nome_da_classe}
# o nome do arquivo pode ser igual ou diferente do nome da classe
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

pessoa1 = PessoaFisica(nome = 'Joao', idade = 25, codigo_banco = 20, cpf = '123.123.123-53')
pessoa2 = PessoaJuridica(nome = 'Jonas LTDA', idade = 20, codigo_banco = 40, cnpj = '222.222.222/2222-22')

print(type(pessoa1))
print(type(pessoa2))