"""
    [Recendo dados do usuário]
    Em Python tudo o que estiver entre aspas simples '', aspas duplas "", aspas simples triplas ''' e aspas duplas
    triplas são considerados strings

"""
# Exemplo do uso do print antigo Python 2.x
# print("Qual o seu nome?")
# Atenção => toda entrada de dados feita via input é convertida para o tipo string automaticamente =>> não esqueça!!!
# nome = input()  # input => solicita uma entrada de dados via terminal. Tecnicamente é um __builtins__
# Processamentox, y,z ...
# ... Saída
# print('Seja bem vindo/a %s' %nome)
# print('Qual sua idade?')
# idade = input()
# Processamentox, y,z ...
# ... Saída
# print('A/o %s tem %s anos' % (nome, idade))

# Exemplo novo Python 3.x
# print('A/O {0} tem {1} anos' .format(nome, idade))

# Exemplo final => print atual -> a partir do Python 3.6
nome = input('Qual o seu nome: ')
# idade = input('Qual sua idade: ')

# Outra opção é fazer o cast na entrada do dado, observe

idade = int(input('Qual é sua idade: '))
print(f'Seja bem vindo(a) {nome} que tem {idade} anos')
"""
    int(idade) =>> é um cast
    cast é a conversão de um tipo de dados em outro, observe que estamos fazendo um operação e idade inicialmente é do tipo string em função de ser uma entrada de dados via input()
    
"""
print(f'O/A {nome} nasceu em {2020 - idade}')
