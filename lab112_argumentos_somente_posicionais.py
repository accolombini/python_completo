"""
Novidades da versão 3.8 => argumentos somente posicionais ->> argumentos posicionais são aqueles que não podem
ser nomeados, por exemplo float(valor=67.3) -> Python emitirá uma mensagem de erro dizendo que você não pode
nomear um argumento float(), isso significa que se trata de um argumento posicional, ou seja, ele existe na
sintaxe, mas não pode ter valor alterado, ou melhor nomeado. TypeError: float() takes no keyword arguments

    NOTA:   - tudo o que estiver antes da barra / será tratado como argumento somente posicional
            observe as variações nos exemplos abaixo
            - podemos na contra mão dos argumentos somente posicionais desejar obrigar que o usuário informe os
            argumentos, para isso, usamos * -> observe a funcção cumprimenta_v5. Note que, no caso do *, estamos
            informando que todos os argumentos após o asterisco deverão ser informados obrigatoriamente


"""

# Contextualizando

valor = '67.3'
print(f'O tipo de valor é {type(valor)} - podemos usar um cast e teremos -> {float(valor)}\n'
      f'E seu tipo agora é -> {type(float(valor))}')


def cumprimenta_v1(nome):  # O que fazemos
    return f'Olá {nome}!!!'


print(f'Saudando -> {cumprimenta_v1("Pedro")}')
print(f'Mostrando que não estou usando argumentos somente posicionais -> {cumprimenta_v1(nome="Mario")}')


# Para definirmos um argumento comosendo somente posicional devemos usar a / ->> observe no exemplo a seguir
def cumprimenta_v2(nome, /):
    return f'Olá {nome}!!!'


print(f'Saudando -> {cumprimenta_v2("Pedro José")}')
# print(f'Mostrando que não estou usando argumentos somente posicionais -> {cumprimenta_v2(nome="Mario")}')
# TypeError: cumprimenta_v2() got some positional-only arguments passed as keyword arguments: 'nome'

# Note que podemos ter quantos argumentos posicionais quisermos em uma função


def cumprimenta_v3(nome, sobrenome, /, mensagem='Olá seja bem vindo!!!'):
    return f'{mensagem} {nome} {sobrenome}'


print(f'Explorando o conceito de argumentos posicionais -> '
      f'{cumprimenta_v3("Pedro", "Manoel", mensagem="O desafio começa hoje")}')
# print(f'Explorando o conceito de argumentos posicionais -> {cumprimenta_v3("Pedro", sobrenome="Manoel")}')
# TypeError: cumprimenta_v3() got some positional-only arguments passed as keyword arguments: 'sobrenome'


# Obrigando que o argumento seja especificado

def cumprimenta_v4(*, nome):
    return f'Olá {nome}'


print(f'Obrigando a entrar com o argumento -> {cumprimenta_v4(nome="Marcos")}')
# print(f'Obrigando a entrar com o argumento veja quando não especifico -> {cumprimenta_v4("Marcos")}')
# TypeError: cumprimenta_v4() takes 0 positional arguments but 1 was given

# Misturando tudo em uma única função


def cumprimenta_v5(nome, /, mensagem1='Olá', *, mensagem2):
    return f'{mensagem1} {nome} {mensagem2}'


print(f'Tudo junto -> {cumprimenta_v5("Pedro", mensagem1="Boa noite", mensagem2="Descanse!")}')
print(f'Tudo junto -> {cumprimenta_v5("Manoel", mensagem2="Excelente!!!")}')
# print(f'Tudo junto -> {cumprimenta_v5(nome="Pedro", mensagem1="Boa noite", mensagem2="Descanse!")}')
# TypeError: cumprimenta_v5() got some positional-only arguments passed as keyword arguments: 'nome'
# print(f'Tudo junto -> {cumprimenta_v5("Pedro", mensagem1="Boa noite")}')
# TypeError: cumprimenta_v5() missing 1 required keyword-only argument: 'mensagem2'
