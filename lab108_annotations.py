"""
Trabalhando com Annotations -> continuação

# Considerações sobre annotations

# Correto

texto: str
) -> str:
alinhamento: bool = True

# Incorreto

texto:str
texto : str
)->str:
) ->str:
alinhamento:bool=True
alinhamento : bool = True
alinhamento :bool=True
alinhamento: bool= True

"""

# Trabalhando com Annotations -> imagine que desejamos saber quais são os annotations utilizados

import math


def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio


print(f'Conhecendo Annotations -> {circunferencia.__annotations__}')  # {'raio': <class 'float'>, 'return': <class 'float'>}

# Como usar -> dica

nome: str = 'Arthur Dutra'
peso: float = 90.0
ativo: bool = True

# Conferindo
print(f'Nome -> {nome} - seu tipo -> {type(nome)}')
print(f'Peso -> {peso} - seu tipo -> {type(peso)}')
print(f'Ativo -> {ativo} - seu tipo -> {type(ativo)}')

ativo = 'princesa'
print(f'Ativo -> {ativo} - seu tipo -> {type(ativo)}')

# Note que Python executará o código acima, pois é Dinâmicamente tipada, PyChar irá avisá-lo realçando o problema
# Por fim, quando solicitar a impressão de annotation, ativo será tratado como bool e não como string
print(__annotations__)  # {'nome': <class 'str'>, 'peso': <class 'float'>, 'ativo': <class 'bool'>}


class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando ...'


# Instanciando um objeto para teste

p = Pessoa(nome='Arthur Dutra', idade= 89, peso=78.9)
print(f'{p.__dict__}')

# Atenção -> uma instância não possui annotations

# print(f'{p.__annotations__}')  # AttributeError: 'Pessoa' object has no attribute '__annotations__'

# Agora os métodos sim possuem annotations, observe
print(f'O método andar da Classe Pessoa -> {p.andar.__annotations__}')

# Não se esqueça o construtor é um método, logo têm annotations, oberve
print(f'Annotations do construtor -> {p.__init__.__annotations__}')
