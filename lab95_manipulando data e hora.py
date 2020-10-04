"""
Manipulando data e hora => eventualmente precisamos trabalhar com Data e Hora.

        NOTA:   Python nos ajuda, pois possui um método built-in (integrado) para se trabalhar
        com data e hora chamado datetime

# Conhecendo o datetime - Primeiro, precisamos importá-lo

import datetime

print(f'Para conhecê-lo basta usarmos o comando dir -> {dir(datetime)}')  # 'datetime' -> observe que dentro do
# módulo datetime existe também uma classe datetime

# Vamos conhecer os limites de datetime

print(f'Limite máximo de anos -> {datetime.MAXYEAR}')
print(f'Limite mínimo de anos -> {datetime.MINYEAR}')

# Neste exemplo vamos acessar a classe datetime e internamente o método now()
# datetime trabalha com os seguintes parâmetros ->> (year, month, day, hour, minute, second, microsecond)

print(f'O tempo exato em que estamos agora é -> {datetime.datetime.now()}')  # 2020-10-03 21:21:40.325535

# Podemos ver a representação deste método, usaremos o já conhecido método repr

print(f'A representação do método acima é -> {repr(datetime.datetime.now())}')
# datetime.datetime(2020, 10, 3, 21, 24, 47, 503790)

# Podemos fazer um ajuste na data/hora e para isso usaremos o método replace()

inicio = datetime.datetime.now()

print(f'O valor de inicio é -> {inicio}')  # 2020-10-03 21:29:52.689860

# Nosso objetivo é alterar o horário para: 22:0:0:0 -> Note que não estamos alterando a data

inicio = inicio.replace(hour=22, minute=0, second=0, microsecond=0)

print(f'O valor de inicio é alterado é -> {inicio}')  # 2020-10-03 22:00:00


# Imagine uma situação na qual você precisa criar uma data e hora

import datetime

evento = datetime.datetime(2021, 1, 1, 0)
print(f'Qual é o tipo de evento? -> {type(evento)}')  # <class 'datetime.datetime'>
print(f'E se o usuário te fornece essa data 31/8/2020 qual seu tipo? -> {type("31/8/2020")}')  # <class 'str'>
print(f'Vamos testar se nossa agenda está legal -> {evento}')

# Mas então, como converter uma data fornecida pelo usuário em uma data Python, e assim, poder
# usar todos os recursos da linguagem para manipular essa data?

nascimento = input('Informe a data de seu nascimento dd/mm/yyyy: ')
print(f'Você nasceu em -> {nascimento} e seu tipo é {type(nascimento)}')

# Não queremos o tipo string queremos datetime, ok

nascimento = nascimento.split('/')  # Com o split estamos separando pela / e
# criando uma lista de string separando pela barra

print(f'Após o uso do split. Você nasceu em -> {nascimento} e seu tipo é {type(nascimento)}')
# ['20', '08', '1976'] e seu tipo é <class 'list'>

# Vamos agora converter nossa lista de string em inteiros usando o cast int em datetime, observe:

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(f'Nascimento após a convesão -> {nascimento} e seu tipo é -> {type(nascimento)}')
# 1765-03-11 00:00:00 e seu tipo é -> <class 'datetime.datetime'>

"""

# Vamos agora fazer acesso individualizado para cada elemento de data e hora

import datetime

evento = datetime.datetime.now()

print(f'{evento.year}', end=' ')
print(f'{evento.month}', end=' ')
print(f'{evento.day}', end=' ')
print(f'{evento.hour}', end=' ')
print(f'{evento.minute}', end=' ')
print(f'{evento.second}', end=' ')
print(f'{evento.microsecond}', end=' ')
