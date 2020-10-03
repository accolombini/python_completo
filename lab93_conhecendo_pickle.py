# -*- coding:utf8 -*-  # Necessário para sistema operacional Windows quando se deseja escrever em arquivos
"""
Conhecendo pickle =>    nos permite salvar dados como se fosse um banco de dados rudimentar, os dados
                        são salvos em formato binário.
                        A função do Pickle é realizar o seguinte processo =>    Objeto Python -> Binarização
                                                                                Binarização -> objeto Pyhton
                        Este processo recebe o nome de serialização/deserialização.
                        NOTA: O módulo Pickle não é seguro contra dados maliciosos e desta forma não recomendado
                        trabalhar com arquvios pickle vindos de outras pessoas que você não conheça ou de
                        fontes desconhecidadas/duvidosas.

# Agora vamos ao Pickle => escrevendo num arquivo Pickle -> Binarização

with open('animais.pickle', 'wb') as arquivo:  # A flag wb -> siginifica escrita em binário
    pickle.dump((felix, pluto), arquivo)  # dump recebe um objeto, como temos mais de um, estamos usando uma tupla

arquivo.close()

"""

import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendo ...')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando ...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} está latindo ...')


# Vamos agora instanciar nossos objetos

felix = Gato('Felix')
pluto = Cachorro('Pluto')

# Agora vamos ao Pickle => lendo num arquivo Pickle -> Objeto Python

with open('animais.pickle', 'rb') as arquivo:  # A flag rb -> leitura de arquivo binário
    gato, cahorro = pickle.load(arquivo)  # O método load é usado para carregar o arquivo
    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é -> {type(gato)}')  # <class '__main__.Gato'>

    print(f'O cachorro chama-se {cahorro.nome}')
    cahorro.late()
    print(f'O tipo do cachorro é -> {type(cahorro)}')  # <class '__main__.Cachorro'>

arquivo.close()
