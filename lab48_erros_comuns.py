"""
Erros mais comuns em Python => é importante saber ler e interpretar a saída de erros porque
ela pode ser essencial para efetuar correções no seu código.
    Traceback é a saída de erros de seu sistema

    ATENÇÃO =>> Como referência a todos os tupos de erros do Python consulte o endereço a seguir:
                https://docs.python.org/3/library/exceptions.html

    Os erros mais comuns são:
        - SyntaxError ->    ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o
                            Python não reconhece como parte da linguagem
                            Na definição de funções
                            def funcao:
                            print('Olá mundo!!!')
                            File "D:/OneDrive/CURSOS/UDEMY/LINGUAGENS/PYTHON/GeekPython/python_completo
                            /lab48_erros_comuns.py", line 22
                            def funcao:
                                    ^
                            SyntaxError: invalid syntax

                            No uso indevido de palavras reservadas da linguagem
                            None = 1
                            File "D:/OneDrive/CURSOS/UDEMY/LINGUAGENS/PYTHON/GeekPython/python_completo
                            /lab48_erros_comuns.py", line 33
                            None = 1
                            ^
                            SyntaxError: cannot assign to None

                            Usando uma palavra reservada da linguagem fora de seu escopo de atuação
                            File "D:/OneDrive/CURSOS/UDEMY/LINGUAGENS/PYTHON/GeekPython/python_completo
                            /lab48_erros_comuns.py", line 46
                            return
                            ^
                            SyntaxError: 'return' outside function

                            String sem aspas
                            print(Olá mundo!!!)
                            File "D:/OneDrive/CURSOS/UDEMY/LINGUAGENS/PYTHON/GeekPython/python_completo
                             /lab48_erros_comuns.py", line 55
                                print(Olá mundo!!!)
                                      ^
                            SyntaxError: invalid syntax


        - NameError ->  ocorre quando Python econtra uma variável ou função que não foi definida

                        Palavra não definida na linguagem Python
                        printf("Python para Ciência de Dados")
                        Traceback (most recent call last):
                        File "D:/OneDrive/CURSOS/UDEMY/LINGUAGENS/PYTHON/GeekPython/python_completo
                        /lab48_erros_comuns.py", line 7, in <module> printf("Python para Ciência de Dados")
                        NameError: name 'printf' is not defined

                        Função não definida

                        Traceback (most recent call last):
                        File "D:/OneDrive/CURSOS/UDEMY/LINGUAGENS/PYTHON/GeekPython/python_completo
                        /lab48_erros_comuns.py", line 66, in <module>
                            ola()
                        NameError: name 'ola' is not defined

                        Variável não definida
                        print(ola)
                        Traceback (most recent call last):
                        File "D:/OneDrive/CURSOS/UDEMY/LINGUAGENS/PYTHON/GeekPython/python_completo
                        /lab48_erros_comuns.py", line 79, in <module>
                            print(ola)
                        NameError: name 'ola' is not defined

                        Variável local não definida
                        a = 18
                        if a < 10:
                            msg = 'É menor que 10'
                        print(f'Simulando um erro de variável desconhecida no interior do bloco if  -> {msg}')
                        Traceback (most recent call last):
                        File "D:/OneDrive/CURSOS/UDEMY/LINGUAGENS/PYTHON/GeekPython/python_completo
                        /lab48_erros_comuns.py", line 92, in <module>
                            print(f'Simulando um erro de variável desconhecida no interior do bloco if  -> {msg}')
                        NameError: name 'msg' is not defined

        - TypeError ->  ocorre quando uma funçõ/operação/ação é aplicada a um tipo errado.

                        Incompatibilidade de tipos
                        print(len(555))
                        Traceback (most recent call last):
                        File "D:/OneDrive/CURSOS/UDEMY/LINGUAGENS/PYTHON/GeekPython/python_completo
                        /lab48_erros_comuns.py", line 108, in <module>
                            print(len(555))
                        TypeError: object of type 'int' has no len()

                        Não consigo concatenar uma string com uma lista vazia. A concatenação é entre strings
                        print('Ola' + [])
                        Traceback (most recent call last):
                        File "D:/OneDrive/CURSOS/UDEMY/LINGUAGENS/PYTHON/GeekPython/python_completo
                        /lab48_erros_comuns.py", line 119, in <module>
                            print('Ola' + [])
                        TypeError: can only concatenate str (not "list") to str

        - IndexError -> ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado
                        indexado utilizando um índice inválido.

                        Neste exemplo há apenas o elemento de índice zero na lista, observe o que ocorre quando
                        tentamos acessar o elemento de índice 2
                        lista = ['Olá']
                        print(f'Tentando acessar um elemento que não existe na lista -> {lista[2]}')
                        Traceback (most recent call last):
                        File "D:/OneDrive/CURSOS/UDEMY/LINGUAGENS/PYTHON/GeekPython/python_completo
                        /lab48_erros_comuns.py", line 133, in <module>
                            print(f'Tentando acessar um elemento que não existe na lista -> {lista[2]}')
                        IndexError: list index out of range

                        Neste exemplo estamos percorrendo uma string mas estrapolamos seus limites
                        print(f'Tentando acessar um elemento que não existe na lista -> {lista[0][10]}')
                        Traceback (most recent call last):
                        File "D:/OneDrive/CURSOS/UDEMY/LINGUAGENS/PYTHON/GeekPython/python_completo
                        /lab48_erros_comuns.py", line 144, in <module>
                            print(f'Tentando acessar um elemento que não existe na lista -> {lista[0][10]}')
                        IndexError: string index out of range

        - ValueError -> ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo
                        incorreto

                        Neste exemplo queremos converter uma string para inteiro, note que o inverso é possível
                        print(int('Ola'))
                        Traceback (most recent call last):
                        File "D:/OneDrive/CURSOS/UDEMY/LINGUAGENS/PYTHON/GeekPython/python_completo
                        /lab48_erros_comuns.py", line 159, in <module>
                            print(int('Ola'))
                        ValueError: invalid literal for int() with base 10: 'Ola'

        - KeyError ->   ocorre quando tentamos acessar um dicionário com uma chave que não existe.

                        Neste exemplo tentaremos acessar o dicionário com uma chave inexistente
                        dicionario = {}
                        print(f'Tetando imprimir o dicionário com uma chave inexistente -> {dicionario["Ola"]}')
                        Traceback (most recent call last):
                        File "D:/OneDrive/CURSOS/UDEMY/LINGUAGENS/PYTHON/GeekPython/python_completo
                        /lab48_erros_comuns.py", line 176, in <module>
                            print(f'Tetando imprimir o dicionário com uma chave inexistente ->
                            {dicionario["Ola"]}')
                        KeyError: 'Ola'

        - AttributeError -> ororre quando uma variável não tem um atributo/função.

                        Neste exemplo tentaremos atribuir uma tupla como atributo para a função sort() que
                        só recebe listas como atributo
                        tupla = 11, 2, 31, 4
                        print(f'Usando sort() -> próprio para lista numa tupla -> {tupla.sort()}')
                        Traceback (most recent call last):
                        File "D:/OneDrive/CURSOS/UDEMY/LINGUAGENS/PYTHON/GeekPython/python_completo
                        /lab48_erros_comuns.py", line 195, in <module>
                            print(f'Usando sort() -> próprio para lista numa tupla -> {tupla.sort()}')
                        AttributeError: 'tuple' object has no attribute 'sort'

        - IndentationError -> ocorre quando não respeitamos a identação do Python que é de 4 espaços

                        Neste exemplo, estamos criando uma função, mas não respeitamos a identação Python
                        def nova():
                        print('Olá')
                        File "D:/OneDrive/CURSOS/UDEMY/LINGUAGENS/PYTHON/GeekPython/python_completo
                        /lab48_erros_comuns.py", line 216
                            print('Olá')
                            ^
                        IndentationError: expected an indented block

    NOTA:   - Exceptions e Erros são sinônimos na programação
            - É importante ler e prestar muita atenção na saída de erro.
"""
# Exemplos

# SyntaxError
# def funcao:
#    print('Olá mundo!!!')

# None = 1

# return

# print(Olá mundo!!!)

# NameError
# printf("Python para Ciência de Dados")

# ola()

# print(ola)

# a = 18
# if a < 10:
#    msg = 'É menor que 10'
# print(f'Simulando um erro de variável desconhecida no interior do bloco if  -> {msg}')

# TypeError

# print(len(555))

# print('Ola' + [])

# IndexError

# lista = ['Olá']
# print(f'Tentando acessar um elemento que não existe na lista -> {lista[2]}')
# print(f'Tentando acessar um elemento que não existe na lista -> {lista[0][10]}')   IndexError: string index out of range

# ValueError

# print(int('Ola'))

# KeyError

# dicionario = {}
# print(f'Tetando imprimir o dicionário com uma chave inexistente -> {dicionario["Ola"]}')

# AttributeError

# tupla = 11, 2, 31, 4

# print(f'Usando sort() -> próprio para lista numa tupla -> {tupla}')

# IdentationError


# def nova():
# print('Olá')
