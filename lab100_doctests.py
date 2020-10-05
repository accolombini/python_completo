"""
Doctests -> Importante => dentro do doctests o Python não reconhece aspas duplas, é preciso ser aspas simples.

        NOTA:   - um grande inconveniente dos doctests é que devemos reproduzir com exatidão nossas saídas
                - Tome muito cuidado com o uso de comentários e das aspas, simples, duplas e triplas duplas


Doctests são testes que colocamos na docstring das funções/métodos Python.


def soma(a, b):
    # soma os números a e b

    #>>> soma(1, 2)
    #3

    #>>> soma(4, 6)
    #10
    #
    return a + b


Para rodar um test do doctest:

python -m doctest -v nome_do_mobulo.py

# Saída

Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    doctests
1 items passed all tests:
   1 tests in doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

# Outro Exemplo, Aplicando o TDD

def duplicar(valores):
    #duplica os valores em uma lista

    #>>> duplicar([1, 2, 3, 4])
    #[2, 4, 6, 8]

    #>>> duplicar([])
    #[]

    #>>> duplicar(['a', 'b', 'c'])
    #['aa', 'bb', 'cc']

    #>>> duplicar([True, None])
    #Traceback (most recent call last):
    #   ...
    #TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    #
    #return [2 * elemento for elemento in valores]


# Erro inesperado...

OBS: Dentro do doctest, o Python não reconhece string com aspas duplas. Precisa ser aspas simples.

def fala_oi():
    #Fala oi

    #>>> fala_oi()
    #'oi'
    #
    # return "oi"

Usando TDD -> observe

def duplicar(valores):
    #duplica os valores em uma lista
    #>>> duplicar([1, 2, 3, 4, 5])
    #[2, 4, 6, 8, 10]
    #>>> duplicar([])
    #[]
    #>>> duplicar(['a', 'b', 'c'])
    #['aa', 'bb', 'cc']
    #>>> duplicar([True, None])
    #Traceback (most recent call last):
    #    ...  # Os três pontos sinalizam para o Python a existência de algo no retorno do erro
    #TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    #
    #return [2 * elemento for elemento in valores]

# Erro inesperado ...Neste caso o problema esta nas aspas, o teste espera aspas duplas, mas o retorno foi aspas simples
# "oi"  # problemas com as aspas duplas que não serão reconhecidas dentro das aspas triplas
# Para resolver o problema usamos aspas simples => 'oi' -> uso das aspas simples para resolver o problema


#def fala_oi():
#    Fala oi
    #>>> fala_oi()
    #'oi'
    #
    # return "oi"


"""


# Um último caso estranho.também em TDD ... Ele passa no PyCharm, mas não passa em outra IDE, por exemplo Sublime Text
# Ocorre que digitei dois espaços após o True quando deveria ter finalizado em True sem espaços

def verdade():
    """Retorna verdade

    >>> verdade()
    True
    """
    return True
