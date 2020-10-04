"""
Métodos de Data e Hora =>   No uso de now() e today() há uma diferença importante, now() permite
                            que você parametrize exatamente o fuso horário (timezone). Já o método today()
                            não aceita parâmetros.

Exemplo -> now() e today()

agora = datetime.datetime.now()

print(f'Conhecendo nossa variável agora -> {agora}\nSeu tipo -> {type(agora)}\nSua representação -> {repr(agora)}')

hoje = datetime.datetime.today()

print(f'Conhecendo nossa variável hoje -> {hoje}\nSeu tipo -> {type(hoje)}\nSua representação -> {repr(hoje)}')

Conhecendo nossa variável agora -> 2020-10-04 12:33:25.158119
Seu tipo -> <class 'datetime.datetime'>
Sua representação -> datetime.datetime(2020, 10, 4, 12, 33, 25, 158119)
Conhecendo nossa variável hoje -> 2020-10-04 12:33:25.158119
Seu tipo -> <class 'datetime.datetime'>
Sua representação -> datetime.datetime(2020, 10, 4, 12, 33, 25, 158119)

----------------------------------------------------------------------------------------------
# Mudanças ocorrendo à meia noite - método combine()
# datetime.time() -> zera o cronômetro -> combine combina as especificações -> de hoje now() a um dia à meia noite (zero)
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

# Conhecendo o tipo de dado

hoje = datetime.datetime.now()
# datetime.datetime(2020, 10, 4, 12, 28, 40, 234529)
print(f'Sabendo que dia é hoje para confeir com a agende de um dia após -> {repr(hoje)}')

print(f'Conhecendo manutenção -> {manutencao}\nSeu tipo é -> {type(manutencao)}\nReproduzindo '
      f'manutencao -> {repr(manutencao)}')

Conhecendo manutenção -> 2020-10-05 00:00:00
Seu tipo é -> <class 'datetime.datetime'>
Reproduzindo manutencaodatetime.datetime(2020, 10, 5, 0, 0)


---------------------------------------------------------------------------------------
# Podemos estar interessados em encontrar o dia da semana -> usamos o método weekday()

# Reaproveitnado nossa manutenção, queremos saber o dia da semana de seu agendamento
# Os dias da semana para o método weekday começam em zero -> 0 -> segunda, 1 -> terça,
# 2 -> quarta, 3 -> quinta, 4 -> sexta 5 -> sábado e 6 -> domingo

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=3)), datetime.time())
print(f'Para qual dia da semana foi agendada nossa manutenção? -> {manutencao.weekday()}')

nascimento = input('Entre com a data de seu nascimento no formato dd/mm/yyyy: -> ')

# Precisamos converter de string para datetime

nascimento = nascimento.split('/')

nascimento = datetime.datetime(year=int(nascimento[2]), month=int(nascimento[1]), day=int(nascimento[0]))

print(f'Você nasceu numa(um) -> {nascimento.weekday()}')

# Melhorando nossa saída

if nascimento.weekday() == 0:
    print(f'Você nasceu numa segunda feira')
elif nascimento.weekday() == 1:
    print(f'Você nasceu numa terça feira')
elif nascimento.weekday() == 2:
    print(f'Você nasceu numa quarta feira')
elif nascimento.weekday() == 3:
    print(f'Você nasceu numa quinta feira')
elif nascimento.weekday() == 4:
    print(f'Você nasceu numa sexta feira')
elif nascimento.weekday() == 5:
    print(f'Você nasceu num sábado')
elif nascimento.weekday() == 6:
    print(f'Você nasceu num domingo')

-------------------------------------------------
# Formatando datas/horas com strftime() (String Format Time) -> dd/mm/aaaa hora:minuto
# Para maiores informações consulte a documentação oficial => https://docs.python.org/3/library/datetime.html

hoje = datetime.datetime.today()

print(f'Vamos ver hoje no formato padrão americano -> {hoje}')  # 2020-10-04 16:01:57.628627

hoje_formatado = hoje.strftime('%d/%m/%Y')  # Fique atento, ano com 4 digitos -> Y maíuculo => com 2 dígitos y minúsuclo

print(f'Vamos ver hoje no formato definido pelo usuário -> {hoje_formatado}')  # 04/10/2020

------------------------------------------------------------------------------

# Melhorando a formatação

# Formatando datas/horas com strftime() (String Format Time) -> dd/mm/aaaa hora:minuto
# Para maiores informações consulte a documentação oficial => https://docs.python.org/3/library/datetime.html

hoje = datetime.datetime.today()

print(f'Vamos ver hoje no formato padrão americano -> {hoje}')  # 2020-10-04 16:01:57.628627

hoje_formatado = hoje.strftime('%d de %B de %Y')  # Fique atento, ano com 4 digitos -> Y maíuculo =>
# com 2 dígitos y minúsuclo

print(f'Vamos ver hoje no formato definido pelo usuário -> {hoje_formatado}')  # 04/10/2020


-------------------------------------------------------------------------------------
# Criando uma função para escrever data num padrão mais amigável


def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Marco de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'

-----------------------------------------------------------------------------------------
import datetime
from textblob import TextBlob


# Refatorando o código da função formata_data() com o uso da nova biblioteca textblob => pip install textblob
# Para maiores informações consulte: https://textblob.readthedocs.io/en/dev/
# Formatando datas/horas com strftime() (String Format Time) -> dd/mm/aaaa hora:minuto
# Para maiores informações consulte a documentação oficial => https://docs.python.org/3/library/datetime.html


# O módulo TextBlob possui um método chamado translate que permite a tradução para a linguagem desejada, observe
# Atenção esse não é um processo recomendado, você irá perceber como a performance cai, além da necessidade de estar
# conectado na Internet


def formata_data(data):
    return f"Em {data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"


hoje = datetime.datetime.today()

print(f'Usando a função para formatar data -> {formata_data(hoje)}')  # Em 4 de Outubro de 2020

-------------------------------------------------------------------------------
# Outra forma de se converter uma string em um datetime é usando o método strptime() -> observe a seguir

nascimento = datetime.datetime.strptime('10/03/1988', '%d/%m/%Y')

print(f'Conhecendo o método strptime() -> {nascimento}\nSeu tipo é -> {type(nascimento)}')  # <class 'datetime.datetime'>

nascimento = input('Qual sua data de nascimento? dd/mm/aaaa: ')
# Tratando a string com strptime()
nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')

print(f'Você nascesu em -> {nascimento} após o uso de  strptime()')

---------------------------------------------------------------------------------------------------


# Em algum momento podemos estar interessados na hora e não na data

almoco = datetime.time(12, 30, 0)

print(f'Seu horário de almoço é -> {almoco}')

# Marcando o tempo de execução do nosso código com timeit -> calcule o tempo disso

# loop for -> com comprehension

tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f'Tempo de execução do for -> {tempo}')

# List Comprehension

tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(f'Tempo de execução com list comprehensio -> {tempo}')

# Usando Map

tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(f'Tempo de execução usando map -> {tempo}')

"""
# Mais fácil fazer do que falar, então vamos praticar

import functools
import timeit


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num**num + 5
    return soma


# print(f'Imprimindo o resultado de teste -> {teste(5)}')
# O método partial de functools recebe dois parâmetros, a função e o número de vezes que será executada,
# no caso, estamos executando a função teste, passando como parâmetro o número 2 -> n = 2
# O método timeit executara partial por um número de vezes, no caso 10000
# partial -> permite analisar se sua função é performática -> lembre-se sempre disso
print(timeit.timeit(functools.partial(teste, 2), number=10000))  # 6.876334699999999
