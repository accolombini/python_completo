"""
Doctests -> o próprio teste serve como documentação de seu sistema, mas é muito mais que isso.
"""

# Trabalhando com doctests


def soma(a, b):
    """soma os valores a e b
    >>> soma(1, 2)  # Isso é um Doctests -> ou seja um teste dentro da documentação do seu código
    3
    """
    return a + b


# Teste da função soma()
print(f'O resultado de soma é -> {soma(3, 7)}')  # O resultado de soma é -> 10
