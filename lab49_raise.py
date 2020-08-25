"""
Levantando os próprios erros com raise => lança exceções

    OBS.:   raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra em Python
            Para simplificar, pense no raise como sendo útil para que possamos criar as nossas próprias
            exceções e mensagens de erro.
            É preciso que o tipo de erro associado ao raise() seja um erro válido em Python, para saber
            os tipos de erros válidos consulte: https://docs.python.org/3/library/exceptions.html

    FORMA GERAL:    raise TipoDoErro('Mensagem do Erro')

            No exemplo a seguir definimos uma função e tratamos as exceções, observe o resultado
            def colore(texto, cor):
                if type(texto) is not str:
                    raise TypeError('Texto precisa ser uma string')
                if type(cor) is not str:
                    raise TypeError('Cor precisa ser uma string')
                print(f'O texto {texto} será impresso na cor {cor}')
            Traceback (most recent call last):
            File "D:/OneDrive/CURSOS/UDEMY/LINGUAGENS/PYTHON/GeekPython/python_completo/lab49_raise.py", line 25,
            in <module> colore('Olá mundo!!!', 4)
              File "D:/OneDrive/CURSOS/UDEMY/LINGUAGENS/PYTHON/GeekPython/python_completo/lab49_raise.py", line
              19, in colore
                raise TypeError('Cor precisa ser uma string')
            TypeError: Cor precisa ser uma string

    NOTA:   O raise, assim como o return, finaliza a função, ou seja, nada após o raise é executado.

"""

# Exemplo real


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Olá mundo!!!', 'azul')  # Tudo certo

# colore('Olá mundo!!!', 4)

# Refatorando a função e aprimorando o uso de raise


def colore(texto, cor):
    cores = 'verde', 'amarelo', 'azul', 'branco'
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa estar contida em cores: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Python para Ciência de Dados', 'branco')  # Tudo certo aqui!!!
# colore('Python para Ciência de Dados', 'lilás')   # Problema do tipo ValueError

# Refatorando para um tipo de erro diferente extraído da referência do Python ->> apenas para teste de raise() ok
# BaseException não se aplica a está função, mas é um tipo de Erro válido para Python


def colore(texto, cor):
    cores = 'verde', 'amarelo', 'azul', 'branco'
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise BaseException(f'A cor precisa estar contida em cores: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


# colore('Python para Ciência de Dados', 'lilás')   # Problema do tipo BaseException
