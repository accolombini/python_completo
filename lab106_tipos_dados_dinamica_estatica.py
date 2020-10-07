"""
Tipagem dinâmica x tipagem estática => A PEP 484 introduz aprimoramentos na linguagem, dentre eles a possibilidade de
trabalhar com tipos estáticos de dados

        - Duck Typing -> a classe do objeto é menos importante do que os métodos ue o definem
        - Type Hinting -> indicar formalmente um tipo de dado de forma estática em uma linguagem naturalmente dinâmica
"""

# Exemplo comum da tipagem dinâmica do Python

# idade = 42
# print(f'Idade tipo inteira gerada dinâmicamente -> {type(idade)} e seu valor é -> {idade}')  # <class 'int'>
# idade = 'Quarenta e dois'
# print(f'Idade tipo inteira gerada dinâmicamente -> {type(idade)} e seu valor é -> {idade}')  # <class 'str'>

# Exemplo trabalhando com Duck Typing


# class CisneNegro:

#    def __len__(self):
#        return 42

#    def abobora(self):
#        return 'Abobora'


# livro = CisneNegro()
# print(f'Podemos acessar o método __len__ -> {len(livro)} e seu tipo é -> {type(len(livro))}')  # <class 'int'>
# Note que livro pertence a classe CisneNegro, no entanto vimos que seu tipo de retorno foi <class 'int'>
# e não à classe CisneNegro
# print(f'Veja isso -> {livro.abobora()} e seu tipo é -> {type(livro.abobora())}')  # <class 'str'>
# print(f'Qual o tipo de livro? -> {type(livro)}')  # <class '__main__.CisneNegro'>

# nome = 'Manoel Bandeira'
# lista = [12, 34, 55, 49]
# dicio = {'carlos': 12, 'vanessa': 34, 'joana': 49}

# print(f'Imprimindo o tamanho das variáveis nome -> {len(nome)}')
# print(f'Imprimindo o tamanho das variáveis lista -> {len(lista)}')
# print(f'Imprimindo o tamanho das variáveis dicio -> {len(dicio)}')

# Entendendo Type Hinting -> note que definimos o tipo de dado para o argumento de entrada e definimos -> str: como
# sendo o retorno esperado para esta função

# def cumprimentar(nome: str) -> str:
#    return f'Olá, {nome}'


# print(f'{cumprimentar("Pedro")}')


# Mais um exemplo -> observe e repita

def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(80, '#')


print(f'{cabecalho("pedro malazarte")}')

print(f'{cabecalho("pedro malazarte", alinhamento=False)}')

print(f'{cabecalho("pedro malazarte", alinhamento="todos")}')  # Note que "todos" é uma string e uma string para
# Python é True
print(f'{cabecalho("pedro malazarte", alinhamento=None)}')  # Note que None é False para Python
