"""
Funções com retorno =>> em Python, quando uma função não retorna nenhum valor, o retorno será do tipo >>= None

OBS.:
    1- funções Python que retornam valores, devem retornar estes valores com a palavra reservada >>= return
    2- não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos
    passar a execução da função diretamente para outra função
    3- a palavra reservada >>= return finaliza a função, ou seja, ela sai da execução da função
    4- podemos ter em uma função diferentes >>= returns; mas a função retornará apenas um dos returns
    5- podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores

"""
from random import random

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Imprimindo numeros -> {numeros}')  # print() -> é um exemplo de função sem retorno
ret = numeros.pop()  # pop() -> é um exemplo de função com retorno
print(f'Imprimindo numeros após o uso da função pop() -> {numeros} \nO valor de retorno de pop() ret é -> {ret}')

print(f'-----------------------------SEPARADOR----------------------------')

# Exemplo de função sem retorno


def quadrado_de_7():  # ATENÇÃO -> esta função não retorna o quadrado de 7 e sim imprime seu valor ->> OBSERVE
    print(f'O quadrado de 7  apartir de uma função sem retorno é -> {7 * 7}')


# Chamando a função
quadrado_de_7()

# Definindo uma função com retorno -> observe -> estamos refatorando nosso código (melhorando o código)


def quadrado_de_8():
    return 8 * 8


print(f'Imprimendo o quadrado de 8 a partir de uma função com retorno -> {quadrado_de_8()}')

print(f'-----------------------------SEPARADOR----------------------------')

# Refatorando mais uma de nossas funções -> diz_oi()


def diz_oi():
    return 'Oi '


print(f'Chamando a função diz_oi diretamente na função print() -> {diz_oi()}')
alguem = 'Manoel!'
print(f'Incrementando o uso da função com uma variáve -> {diz_oi() + alguem}')

print(f'-----------------------------SEPARADOR----------------------------')

# Exemplo 1 => return finalizando a função


def diz_oi():
    print(f'Estou sendo executdo dentro de diz_oi() antes do return')
    return 'Oi'
    print(f'Estou sendo executado após o return note que estou forçando a identaçao -> {"ATENÇÃO"} \nEsta linha nunca será  executada -> return finaliza a função')


print(f'Agora estou executando diz_oi() extenamente à função -> {diz_oi()}\nNote que o print() anterior não aconteceu')

# Exemplo 2 => podemos ter em uma função diferentes returns -> OBSERVE

variavel = False


def nova_funcao():
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


if variavel:
    print(f'Testando a função nova_função() com variável igual a True -> {nova_funcao()}')
elif variavel is None:
    print(f'Testando a função nova_função() com variável igual a None -> {nova_funcao()}')
else:
    print(f'Testando a função nova_função() com variável igual a False -> {nova_funcao()}')

# Exemplo 3 => podemos em uma função retornar qualquer tipo de dados e até mesmo múltiplos valores -> OBSERVE


def outra_funcao():
    return 2, 3, 4, 5  # Estamos retornando múltiplos valores -> note que para Python isso é uma Tupla


num1, num2, num3, num4 = outra_funcao()

print(f'O valor de num1 é -> {num1}')
print(f'O valor de num2 é -> {num2}')
print(f'O valor de num3 é -> {num3}')
print(f'O valor de num4 é -> {num4}')

print(f'Ou então teriámos o mesmo resultado imprimindo a função -> {outra_funcao()} \nSeu tipo será -> {type(outra_funcao())}')

print(f'-----------------------------SEPARADOR----------------------------')

# Vamos agora criar uma função para jogar uma moeda => precisaremos importar random


def joga_moeda():
    # Gera um número pseudo randomico entre 0 e 1
    valor = random()  # Note que está variável é desnecessária uma vez que random() retorna valor
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


# Executando a funçõ joga_moeda()
print(f'Jogando uma moeda -> {joga_moeda()}')

# Refatornando o códio joga_moeda()


def joga_moeda():
    # Gera um número pseudo randomico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


# Executando a funçõ joga_moeda()
print(f'Jogando uma moeda -> {joga_moeda()}')

print(f'-----------------------------SEPARADOR----------------------------')

# Erros comuns na utilização do retorno, que na verdade nem é erro de fato, mas sim uma codificação desnecessária


def eh_impar():
    numero = 8
    if numero % 2 != 0:
        print(f'O número é impar e seu valor é -> {numero}')
        return True
    else:  # Este else é absolutamente desnecessário, pois return já encerra a ação
        print(f'O número é par e seu valor é -> {numero}')
        return False


# Executando a função eh_impar()
print(f'Executando a função eh_impar() {eh_impar()}')

# Refatorando a função eh_impar() -> retirando o else -> OBSERVE a limpeza no código

numero = 33


def eh_impar():
    if numero % 2 != 0:
        return True
    return False


# Executando a função eh_impar()
print(f'Executando a função eh_impar() {eh_impar()} e seu valor é -> {numero}')
