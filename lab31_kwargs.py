"""
**kwargs -> pdoeria ter qualquer nome como **abc, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas direfente do *args que coloca valores extras em uma tupla, o **kwargs
exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário.

OBS.:   - Os parâmetros *args e **kwargs não são obrigatórios
        - Nas nossas funções podemos ter =>> NESSA ORDEM!!!:
            - Parâmetos obrigatórios;
            - *args;
            - Parâmetros default (não obrigatórios)
            - **kwargs
            - Cuidado para não nomear os argumentos quando estiver trabalhando com parâmentros obrigatórios e *args
        - Dicionários podem ser desempacotados com **kwargs =>> basta utilizar ** antes do dicionário

"""


# Exemplo de **kwargs


def cores_favoritas(**kwargs):
    print(f'Conhecendo o **kwargs -> {kwargs}')


cores_favoritas(cor1='Cinza', cor2='Preto')
cores_favoritas(João='Cinza', Pedro='Branco', Zezinho='Amarelo', Petunia='Lilás')
cores_favoritas(a=1.12, b=3.14, c=False, João='Cinza', Pedro='Branco', Zezinho='Amarelo', Petunia='Lilás')


# Exemplo ->> refatornado a função cores_favoristas para apliar o uso do **kwargs -> observe a diferença no uso
# dos argumentos a, b e c


def cores_favoritas(a, b, c, **kwargs):
    print(f'Conhecendo o **kwargs -> {a, b, c, kwargs}')


cores_favoritas(1.35, 3.14, True, João='Cinza', Pedro='Branco', Zezinho='Amarelo', Petunia='Lilás')


# Exemplo ->> melhorando nossa função explorando o poder dos dicionários


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de/a {pessoa.title()} é {cor}')


cores_favoritas(João='Cinza', Pedro='Branco', Zezinho='Amarelo', Petunia='Lilás')

# OBS.:   - Os parâmetros *args e **kwargs não são obrigatórios
cores_favoritas()
cores_favoritas(jaca='verde')


# Exemplo =>> complicando um pouco as coisas -> acompanhe


def cumprimento_especial(**kwargs):
    if 'Ciência' in kwargs and kwargs['Ciência'] == 'Python':
        return f'Você merce um cumprimento especial -> Seja bem vindo ser Pythonico!!!'
    elif 'Ciência' in kwargs:
        return f'{kwargs["Ciência"]} ->> Ser normal apenas um Olá para você!!!!!'
    return f'Criatura não sei quem é você!!!'


print(f"Chamando cumprimento_especial() -> {cumprimento_especial(Ciência='Python')}")
print(f"Chamando cumprimento_especial() -> {cumprimento_especial(Ciência='Vinho')}")
print(f"Chamando cumprimento_especial() -> {cumprimento_especial(Jaca='Madura')}")


# Exemplo -> uso de parâmetros diversos respeitando a ordem


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'Dados -> {nome.title()} tem {idade} anos!!!')
    print(args)
    if solteiro:
        print(f'O/A cidadão/dã -> {nome.title()} é Solteiro/ra')
    else:
        print(f'O/A cidadão/dã -> {nome.title()} é Casado/a')
    print(kwargs)


minha_funcao(8, 'Mariana')
minha_funcao(nome='Julia', idade=35, solteiro=True)
minha_funcao(18, 'Fernanda', 4, 5, 88.7, solteiro=True)
minha_funcao(34, 'Fred', eu='Não', voce='onde')
minha_funcao(81, 'Juca', 3.14, 9, 3.75, php=False, python=True)
minha_funcao(35, 'Julia', 4, 5, 88.7, solteiro=True, pedro='Amarelo', juca='Vede abacate')
minha_funcao(idade=35, nome='Julia', args=(4, 5, 88.7), solteiro=True, pedro='Amarelo', juca='Vede abacate')


# minha_funcao(idade=35, nome='Julia', 1, 2, 3, solteiro=True, pedro='Amarelo', juca='Vede abacate')  # SyntaxError


# Entenda porque a ordem é importante que seja respeitada e seguida nos parâmtros da declaração

# Função com a ordem correta


def mostra_tudo(a, b, *args, instrutor='nerd', **kwargs):
    return [a, b, args, instrutor, kwargs]


print(f'O que podemos esperar de mostra_tudo -> {mostra_tudo(1, 22)}')
print(f'O que podemos esperar de mostra_tudo -> {mostra_tudo(1, 22, "Julia")}')
print(f'O que podemos esperar de mostra_tudo -> {mostra_tudo(1, 22, "Julia", "Marcos", instrutor="Márcio")}')
print(
    f'O que podemos esperar de mostra_tudo -> {mostra_tudo(1, 22, "Julia", "Marcos", instrutor="Márcio", verde="abacate", vermelho="morango")}')


# Função com a ordem incorreta de parâmetros -> atenção!!!!


def mostra_tudo(a, b, instrutor='nerd', *args, **kwargs):
    return [a, b, instrutor, args, kwargs]


print(f'O que podemos esperar de mostra_tudo -> {mostra_tudo(1, 2, 3, sobrenome="Veroneze", cargo="Instrutor")}')


# Observe que o instrutor virou 3 e *args está vazio ()

# Exemplo => desempacotar com **kwargs -> Nesta função estaremos separando nomes de sobrenomes


def mostra_nomes(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}'


nomes = {'nome': 'João', 'sobrenome': 'do Pulo'}
# print(f'Testantdo a função mostra_nomes ->> {mostra_nomes(nomes)}') Irá resultar em um erro -> TypeError
# TypeError: mostra_nomes() takes 0 positional arguments but 1 was given
print(f'Testantdo a função mostra_nomes ->> {mostra_nomes(**nomes)}')  # Observe o poder so **kwarks


# Exemplos de desempacotamento sem o uso do **kwargs >>= fique atento às diferenças


def soma_multiplos_numeros(a, b, c):
    print(f'A soma dos dados de entrada é ->> {a + b + c}')


lista = [1, 2, 3]
tupla = (4, 5, 6)
conjunto = {7, 8, 9}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

# Agora o que acontece se tivermos um dicionário? ->> Observe o uso dos asteriscos * e ** e o resultado
# ATENÇÃO =>> para que isso funcione o nome das chaves do dicionário devem ser os mesmos dos parâmetros da função

dicionario = {'a': 10, 'b': 11, 'c': 12}
soma_multiplos_numeros(*dicionario)
soma_multiplos_numeros(**dicionario)

# Exemplo ->> observe o que acontece aoo alterar o nome das chaves ->> Note que isso são limitações do não uso do **kwargs

dicionario = {'d': 10, 'e': 11, 'f': 12}
soma_multiplos_numeros(*dicionario)  # Sem problemas aqui


# soma_multiplos_numeros(**dicionario)  # Aqui teremos TypeError
# TypeError: soma_multiplos_numeros() got an unexpected keyword argument 'd'

# Refatorando a função adiconando **kwargs além dos parâmetros obrigatórios


def soma_multiplos_numeros(a, b, c, **kwargs):
    print(f'A soma dos dados de entrada é ->> {a + b + c} {kwargs}')


# Fique atento aos usos dos parâmetros
dicionario = dict(a=1, b=33, c=7, nome="Pedroso")
soma_multiplos_numeros(**dicionario)
soma_multiplos_numeros(**dicionario, instrutor='James')
