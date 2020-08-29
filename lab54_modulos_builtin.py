"""
Módulos Builtin => são módulos integrados que já vem instalados no Python

    Ao instalar Python os módulos builtin são instalados também, a única coisa é que eles não são carregados sem
    que você demande explicitamente esse desejo.
    Para conhecer um pouco sobre os módulos builtins digite dir(__builtins). Para uma lista completa e maiores
    detalhes consulte: https://docs.python.org/3/py-modindex.html

    ATENÇÃO:    Utilizando alias (apelidos) para módulos/funções => recurso importante para codificação profissional
                Exemplo: import random as rdm   -> neste caso estamos definindo que o nome do módulo random
                será ->> rdm =>> print(rdm.random())
                Exemplo: from random import randint as rdi, random as rdm -> neste caso estamos definindo que
                o nome da função randint será ->> rdi e oo nome da função random será ->> rdm
                =>> print(rdi(5, 89)) =>> print(rdm())
                Podemos importar todas as funções de um módulo utilizando *
                Exemplo: from random import * -> importante embora o resultado da importação sejam todas as funções
                do módulo random, seu efeito na codificação é importante, pois nesse caso, você não fica preso à
                necessidade de utilizar o nome do módulo para chamar uma função, você poderá chamar a função diretamente
                Exemplo: print(random()) -> e se o import fosse => import random -> print(random.random()) => você teria
                que usar o nome do módulo antes do nome da função
                Costumamos utilizar tuple para colocar múltiplos imports de um mesmo módulo e escrevemos um módulo por
                linha, Exemplo: from random import (
                                                    random,
                                                    randint,
                                                    shuffle,
                                                    choice
                                                    )

"""
from random import (
                    random,
                    randint,
                    shuffle,
                    choice
                    )
print(f'Usando random() -> {random()}')
print(f'Usando randint() -> {randint(2, 8)}')
lista = ["A", "J", "Q", "K"]
print(f'A lista antes do shuffle era -> {lista}')
shuffle(lista)
print(f'Usando shuffle() -> {lista}')
print(f'Usando choice() -> {choice("Python")}')
