"""
Documentando funções com Docstrings

OBS.:   1- Podemos ter acesso  à documentação de uma função em Python utiliando a propriedade especial __doc__
        2- Podemos fazer acesso a documentação com a função help() -> use mais frequentemente quando em um
        terminal Python

"""
# No exemplo a seguir temos acesso à documentacão do método print() => Docstrings
print(f'Teste da impressão de docstring -> {print.__doc__}')
print(help(print()))

# Exemplos -> gerando um docstring para nossa função diz_oi() => docstrings gerado a partir de """docstrings"""


def diz_oi():
    """Uma função que retorna a expressão Oi quando chamada. Não há parâmetros de entrada"""
    return 'Oi!!!'


print(f'Testando a função diz_oi() -> {diz_oi()}')
print(f'Visualizando a documentação da função diz_oil() <$> {diz_oi.__doc__}')


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' à 'potencia' informada.
    :param numero: Número que desejamos gerar o exponencial.
    :param potencia: Potência que queremos gerar o exponencial. Por padrão será 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'.
    """
    return numero ** potencia


print(f'O valor de 2 ao cubo é -> {exponencial(2, 3)}')
print(f'Visualizando a documentação da função exponencial() <$> {exponencial.__doc__}')
