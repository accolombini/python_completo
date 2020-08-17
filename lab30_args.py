"""
Entendnendo o *args _ trata-se de um parâmetro especial de uma função

    - O *args é um parâmetro, como outro qualquer. Isso significa que você poderá chamá-lo de qualquer coisa
    desde que inicie com um *
    Por exenplo -> o parâmetro a seguir poderia ser um args =>> *nparam
    - Mas por convenção, foi adotado o uso de *args para definir esse parâmetro

    Afinal o que é o *args?
    O parâmetro *args utilizado em uma função, coloca os valores extras informados como
    entradas em um tupla. Então, como já é sabido =>> tuplas são imutáveis ...

NOTE =>> o asterisco * serve para que informemos ao Python que estamos passando como argumento uma coleção de dados
Desta forma, ele saberá que precisará antes desmpacotar estes dados. Isto é válido para todas as coleções a menos do Dicionário

"""

# Exemplos de *args =>> fazendo a coisa de forma errada ou menos profissional


def soma_todos_numeros(num1=1, num2=2, num3=3):
    return num1 + num2 + num3


print(f'Teste da função soma_todos_numeros -> {soma_todos_numeros(1, 3, 5)}')
print(f'Teste da função soma_todos_numeros -> {soma_todos_numeros(1, 3)}')
# print(f'Teste da função soma_todos_numeros -> {soma_todos_numeros(1, 3, 5, 7)}')  # Retorna TypError

# Exemplo <=> entendendo o *args
# Primeiramente apenas refatorando a função anterior e substituindo os parâmetros por *args
# Observe o poder de se trabalhar com tuplas na função a seguir => Tudo
# o que foi aprendido para tuplas se aplica em *args


def soma_todos_numeros(*args):
    return sum(args)


print(f'Chamando soma_todos_os_numeros sem argumentos -> {soma_todos_numeros()}')
print(f'Chamando soma_todos_os_numeros com argumentos -> {soma_todos_numeros(1)}')
print(f'Chamando soma_todos_os_numeros com argumentos -> {soma_todos_numeros(1, 2)}')
print(f'Chamando soma_todos_os_numeros com argumentos -> {soma_todos_numeros(1, 2, 3)}')
print(f'Chamando soma_todos_os_numeros com argumentos -> {soma_todos_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9)}')
print(f'Chamando soma_todos_os_numeros com argumentos -> {soma_todos_numeros(1, 2, 3, 4.55, 5, 6, 7, 8, 9.89)}')

# Exemplo <=> na funçã a seguir temos valores que são obrigatórios e *args


def soma_todos_numeros(nome, email, *args):
    return f'{nome} + {email} + {sum(args)}'


print(f'Chamando soma_todos_os_numeros sem argumentos -> {soma_todos_numeros("Alberto", "aa@bb.com")}')
print(f'Chamando soma_todos_os_numeros com argumentos -> {soma_todos_numeros("Alberto", "aa@bb.com",1)}')
print(f'Chamando soma_todos_os_numeros com argumentos -> {soma_todos_numeros("Alberto", "aa@bb.com", 1, 2.25)}')

# Outro exemplo de utilização do *args


def verifica_info(*args):
    if 'Python' in args and 'Ciência de Dados' in args:
        return 'O sucesso está em suas mãos... Bem vindo!!!'
    return 'Eu não tenho certeza ...'


print(f'Testando *args -> {verifica_info()}')
print(f'Testando *args -> {verifica_info(1.55, 3.14, 10, True, "Macaco", "Python","Linguagem R")}')
print(f'Testando *args -> {verifica_info(20, 22.67, "Python", "Ciência de Dados", "Linguagem R")}')
print(f'Testando *args -> {verifica_info(20, 22.67, "Python", "Ciência de Dados", "Linguagem R", False, "Abóbora")}')


# Mais um exemplo com *args


def soma_todos_numeros(*args):
    return sum(args)


print(f'Mais um teste de *args com a função soma_todos_numeros -> {soma_todos_numeros()}')
print(f'Mais um teste de *args com a função soma_todos_numeros -> {soma_todos_numeros(1, 2, 3, 7)}')
#  print(f'Mais um teste de *args com a função soma_todos_numeros -> {soma_todos_numeros("Jaca", 7, 3, 2, 1)}')  # TypeError

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#  print(f'Mais um teste de *args com a função soma_todos_numeros -> {soma_todos_numeros(numeros)}')  # TypeError

# Para entendermos esses erros, vamos refatorar nossa função soma_todos_numeros()


def soma_todos_numeros(*args):
    print(f'O que temos em *args -> {args}')
    return sum(args)


# print(f'Mais um teste de *args com a função soma_todos_numeros -> {soma_todos_numeros(numeros)}')
# ([1, 2, 3, 4, 5, 6, 7, 8, 9],) -> note que *args está convertendo nossa lista de entrada numa tupla com essa característica


# Entendido o problema, precisamos resolver. Para resolver esse problema vamos usar o Desempacotador
# Revisando desempacotador

num = [1, 2, 3]

num1, num2, num3 = num  # Desempacotamento

print(f'Mais um teste de *args com a função soma_todos_numeros -> {soma_todos_numeros(num1, num2, num3)}')


# Existe uma forma incrível de fazer isso quando se trabalha com *args ->> observe
# NOTE =>> o asterisco * serve para que informemos ao Python que estamos passando como argumento uma coleção de dados
# Desta forma, ele saberá que precisará antes desmpacotar estes dados.

print(f'Mais um teste de *args com a função soma_todos_numeros -> {soma_todos_numeros(*numeros)}')
