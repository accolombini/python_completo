"""
Usando ferramentas para checagem de tipos em Python -> MyPy

    - Para maiores informações consulte: http://mypy-lang.org/
"""

# Reaproveitando o código do laboratório anterior


# def cabecalho(texto: str, alinhamento: bool = True) -> str:
#    if alinhamento:
#        return f"{texto.title()}\n{'-' * len(texto)}"
#    else:
#        return f" {texto.title()} ".center(80, '#')


# Refatorando para testes -> note a importância de trabalhar com dados estáticos

def cabecalho(texto, alinhamento=True):
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(80, '#')

"""

Quando trabalhamos com tipagem dinâmica veja o retorno MyPy -> Note que é inútil. Mesmo havendo problemas com tipos
$ mypy lab107_check_tipos_mypy.py
Success: no issues found in 1 source file

"""
print(f'{cabecalho("pedro malazarte")}')

print(f'{cabecalho("pedro malazarte", alinhamento=None)}')

print(f'{cabecalho("pedro malazarte")}')

print(f'{cabecalho("pedro malazarte", alinhamento="Mane")}')

# print(f'{cabecalho("pedro malazarte", alinhamento="todos")}')  # Note que "todos" é uma string e uma string para
# Python é True
# print(f'{cabecalho("pedro malazarte", alinhamento=None)}')  # Note que None é False para Python

"""
Resposta de NuPy:
$ mypy lab107_check_tipos_mypy.py
lab107_check_tipos_mypy.py:21: error: Argument "alinhamento" to "cabecalho" has incompatible type "str"; expected "bool"
lab107_check_tipos_mypy.py:23: error: Argument "alinhamento" to "cabecalho" has incompatible type "None"; expected "bool"
Found 2 errors in 1 file (checked 1 source file)

"""

# Vamos corrigir o problema e executar novamente com MyPy


print(f'{cabecalho("pedro malazarte", alinhamento=False)}')
print(f'{cabecalho("pedro malazarte", alinhamento=True)}')

"""
Resposta de MyPy:
$ mypy lab107_check_tipos_mypy.py
Success: no issues found in 1 source file

"""
