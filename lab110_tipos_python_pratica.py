"""
Tipos em Python na Prática -> deixando um pouco mais complexo

# Trabalhando com Type Hinting em tipos mais complexos -> olhando para as variáveis não para seu conteúdo

nomes: list = ['Ciencia', 'Dados']

versoes: tuple = (3, 5, 7)

opcoes: dict = {'ar': True, 'banco_couro': True}

valores: set = {3, 4, 5, 6}

print(f'Olhando para nossas variáveis tipadas listas -> {nomes}')
print(f'Olhando para nossas variáveis tipadas tuplas -> {versoes}')
print(f'Olhando para nossas variáveis tipadas dicionários -> {opcoes}')
print(f'Olhando para nossas variáveis tipadas set -> {valores}')
print(f'visualizando todos os tipos definidos -> {__annotations__}')
# {'nomes': <class 'list'>, 'versoes': <class 'tuple'>, 'opcoes': <class 'dict'>, 'valores': <class 'set'>}


-----------------------------------------------------------------------------


# Trabalhando com tipos mais complexos e agora olhando para seu conteúdo

from typing import Dict, List, Tuple, Set


nomes: List[str] = ['Ciencia', 'Dados']

versoes: Tuple[int, int, int] = (3, 5, 7)

opcoes: Dict[str, bool] = {'ar': True, 'banco_couro': True}

valores: Set[int] = {3, 4, 5, 6}

print(f'Olhando para nossas variáveis tipadas listas -> {nomes}')
print(f'Olhando para nossas variáveis tipadas tuplas -> {versoes}')
print(f'Olhando para nossas variáveis tipadas dicionários -> {opcoes}')
print(f'Olhando para nossas variáveis tipadas set -> {valores}')
print(f'visualizando todos os tipos definidos -> {__annotations__}')
# {'nomes': typing.List[str], 'versoes': typing.Tuple[int, int, int], 'opcoes': typing.Dict[str, bool],
# 'valores': typing.Set[int]}

----------------------------------------------------------------------------------------------------------

Acesse o site: https://www.alt-codes.net/suit-cards
    - Vamos usar naipes preenchido como pretos
    - Vamos usar naipes sem preenchimento como vermelhos

--------------------------------------------------------------------------------------------
# Testando o que temos até aqui

print(f'A constante NAIPES -> {NAIPES}')  # ['♠', '♡', '♢', '♣']
print(f'A constante CARTAS -> {CARTAS}')  # ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
print(f'Criando nosso baralho -> {criar_baralho()}')

--------------------------------------------------------------------------------------------
# Testando o que temos até aqui -> criada a função distribuir_cartas

baralho = criar_baralho()
print(f'Chamando distribuir_cartas -> {distribuir_cartas(baralho)}')

"""

import random

# Note que constantes em Python devem ser escritas em maiúsculas

NAIPES = '♠ ♡ ♢ ♣'.split()
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


def criar_baralho(aleatorio=False):
    """Cria um baralho com 52 cartas para jogar"""
    baralho = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho):
    """Gerencia a mão de cartas de acordo com o baralho gerado"""
    # Neste jogo teremos 4 jogadores
    return baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4]


def jogar():
    """Inicia um jogo de cartas para 4 jogadores"""
    cartas = criar_baralho(aleatorio=True)
    jogadores = 'P1 P2 P3 P4'.split()
    maos = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()
