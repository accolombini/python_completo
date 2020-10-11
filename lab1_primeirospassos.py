'''
PEP 8  Python Enhancement Proposal (Propostas de aprimoramento do Python) -> https://www.python.org/dev/peps/
São orientações para que se construa códigos Python de qualidade. A ideia da PEP8 é a que possamos aprimorar e customizar a forma de escrever código Python -> alguns deles a seguir:
1- Utilize Camel Case para atribuir nomes de classes;
class Calculadora:
    pass


class CalculadoraCientifica:
    pass

2- Pule duas linhas após comentários e após uma classe;

3- Utilize nomes em minúsculo, separados por undeline para funções e variáveis;
def soma():
    pass


def soma_dois():
    pass


numero = 4
numero_impar = 5

4- Utilize 4 espaços para identação (Não use TAB) >>= isso é muito importante (funciona como um delimitador para o Python)
if 'a' in 'banana':
    print('tem')

5- Linhas em branco -> separar comentários ininiais e definições de classes e funções com duas linhas em branco
Métodos dentro de uma classe devem ser separados com uma única linha em branco;

6- Imports completos -> devem ser sempre feitos em linhas separadas. Importes parciais podem ser feitos na mesma linha separados por vírgulas;
# import Errado
import sys, os
# import Certo
import sys
import os
# Não há problema em escrever:
from types import StringType, ListType
# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:
from types import (
    StringType,
    ListType,
    SetType,
    OutrosType
)
# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e antes de constantes # ou variáveis globais.

7- Espaços em expressões e instruções -> fique atento
# Não faça:
funcao( algo[ l ], { outro: 2 } )
# Faça:
funcao(algo[l], {outro: 2})
# Não faça:
algo (1)
# Faça
algo(1)
# Não faça:
dict ['chave'] = list [indice]
# Faça
dict['chave'] = list[indice]
# Não faça
x             =  2
y              = 20
variavel_longa = 8
# Faça
x = 2
y = 20
variavel_longa = 8

8- Temine sempre uma instrução com uma nova linha

'''

import this
