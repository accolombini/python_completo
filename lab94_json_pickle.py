# -*- coding:utf8 -*-  # Necessário para sistema operacional Windows quando se deseja escrever em arquivos
"""
JSON E PICKLE =>    JSON => JavaScript Object Notation -> muito empregad em API de empresas como Twitter,
                    Facebook, Youtube ... e terceiros (nós desenvolvedores).
                    JSON => trabalham com aspas duplas -> daí a necessidade do metodo dumps()
                    Integrando o json com o pickle  => precisamos instalar uma biblioteca -> pip install jsonpickle

import json

# O método dumps é importante, pois é ele que pega seu objeto e transforma para o formato JSON
ret = json.dumps(['produto', {'PlayStation 4': ('2TB', 'Novo', '220V', 2340)}])

print(f'O tipo de ret é -> {type(ret)}')  # <class 'str'>
print(f'O valor de ret é -> {ret}')  # ["produto", {"PlayStation 4": ["2TB", "Novo", "220V", 2340]}]

# Trabalhando com JSON

import json


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


# Instanciando objeto

felix = Gato('Felix', 'Vira-Lata')

print(f'Conhecendo o dict de felix -> {felix.__dict__}')

ret = json.dumps(felix.__dict__)

print(f'O valor de ret no formato JSON é -> {ret}')

# Trabalhando com JSON e Pickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


# Instanciando objeto

felix = Gato('Felix', 'Vira-Lata')

ret = jsonpickle.encode(felix)

print(f'Vamos conhecer ret -> {ret}')

# Trabalhando com JSON e Pickle => refatorando ...
# Escrevendo o arquivo json/pickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


# Instanciando objeto

felix = Gato('Felix', 'Vira-Lata')

# Note que o método encode é necessário para modelar nosso objeto para o formato jsonpickle

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)

arquivo.close()


"""

# Trabalhando com JSON e Pickle => refatorando ...
# Lendo o arquivo json/pickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


# Note que o método decode é necessário para decodificar nosso objeto

with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(f'O valor de ret -> {ret}')  # <__main__.Gato object at 0x000001FAD25DBF10>
    print(f'O tipo de ret -> {type(ret)}')  # <class '__main__.Gato'>
    print(f'O nome do objeto -> {ret.nome}')
    print(f'A raça de ret é -> {ret.raca}')

arquivo.close()
