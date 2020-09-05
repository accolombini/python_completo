"""
Funções de Maior Grandeza => Higher Order Functions - HOF

        O que isso significa?
            - Quando uma linguagem de programação suporte HOF, indica que podemos ter funções que retornam outras
            funções como resultado ou mesmo que podemos passar funções como argumentos para outras funções, e até
            criar variáveis do tipo de funções nos nossos programas.

        OBS.:   1- Em Python, as funções são Cidadões de Primeira Classe, First Class Citizen.
                2- Em Python, podemos também ter funções dentro de funções, que são conhecidas por
                Nested Functions, ou também Inner Functions (Funções Internas).
                3- Inner Functions (Funções Internas / Nested Functions) podem acessar o escopo de funções
                mais externas

"""
# Importando para os exemplos
from random import choice

# Exemplo -> definindo as funções ->> Observe funções de maior grandeza


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return round(a / b, 2)


def calcular(num1, num2, funcao):  # Note que calcular() recebe uma função como parâmetro
    return funcao(num1, num2)  # Observe que o retorno de calcular é a execução da funcao (resultado)


# Testando as funções
print(f'Testando a função calcular com a função somar() -> {calcular(4, 3, somar)}')
print(f'Testando a função calcular com a função diminuir() -> {calcular(4, 3, diminuir)}')
print(f'Testando a função calcular com a função multiplicar() -> {calcular(4, 3, multiplicar)}')
print(f'Testando a função calcular com a função dividir() -> {calcular(4, 3, dividir)}')


# Exemplo -> Nested Functions ->> Funções Aninhadas

def cumprimento(pessoa):  # Função mais externa
    def humor():  # Função interna
        return choice(('E aí - ', 'Suma daqui - ', 'Gosto muito de você - '))
    return humor() + pessoa  # Observe que é aqui que a função humor() é chamada e executada

# Teste da função cumprimento()


print(f'Cumprimento em teste -> {cumprimento("Mario")}')
print(f'Cumprimento em teste -> {cumprimento("Helena")}')


# Retornando funções de outras funções


def faz_me_rir():
    def rir():
        return choice(('hahahahahah', 'kkkkkkkkkkkk', 'yayayayayayayaya'))
    return rir  # Note que não estamos executando a função e sim a retornando para quem chamou -> faz_me_rir()


# Testando retorno de função
rindo = faz_me_rir()  # Observe que rindo será do tipo -> <class 'function'> (retorno de uma função)
print(f'Resultado de faz_me_rir -> {rindo()} - seu tipo é -> {type(rindo)}')  # Tipo rindo -> <class 'function'>


# Inner functions acessando funções mais externas


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahahah - ', 'lolololololo - ', 'kkkkkkkkkk - '))
        return f'{risada} {pessoa}'  # Observe que pessoa está no escopo da função mais externa
    return dando_risada  # Observe que estamos retornando a função, não estamos executnado.


# Testando Inner
rindo_novamente = faz_me_rir_novamente('Ferdinando')  # Novamente rindo_novamente será do tipo -> <class 'function'>
print(f'Testando a função Inner acessando o escopo de funções mais externas -> {rindo_novamente()}')
