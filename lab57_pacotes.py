"""
Pacotes =>> é um diretório contendo uma coleção de módulos Python que podemos fazer uso em nossa codificação

    Módulos =>> é apenas um arquivo Python que pode conter diversas funções que podemos fazer uso em nossa
    codificação

    OBS.:   Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo chamado __init__.py
            Nas versões do Python 3.x não é mais obrigatório a utilização deste arquivo __init__.py, mas
            normalmente ainda é utilizado para manter a compatibilidade. É um arquivo vazio, utilizado apenas
            para assegurar a completa compatibilidade

    Exemplo :   Fazendo uso dos pacotes criados
                from geek import pacote_geek1, pacote_geek2
                from geek.python import pacote_python_geek3, pacote_python_geek4

                print(f'Testando o uso de pacotes -> pacote_geek1 ->> {pacote_geek1.pi}')
                print(f'Testando o uso de pacotes -> pacote_geek1 ->> {pacote_geek1.funcao1(4, 6)}')
                print(f'Testando o uso de pacotes -> pacote_geek2 ->> {pacote_geek2.curso}')
                print(f'Testando o uso de pacotes -> pacote_geek2 ->> {pacote_geek2.funcao2()}')

                print(f'Testando o uso de pacotes -> pacote_python_geek3 ->> {pacote_python_geek3.funcao3()}')
                print(f'Testando o uso de pacotes -> pacote_python_geek4 ->> {pacote_python_geek4.funcao4()}')

"""
# Fazendo uso dos pacotes criados importando funções específicas

from geek.pacote_geek1 import funcao1
from geek.python.pacote_python_geek4 import  funcao4

print(f'Importando uma função específica ->> {funcao1(10, 20)}')
print(f'Importando uma função específica ->> {funcao4()}')
