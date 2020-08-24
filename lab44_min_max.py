"""
Min e Max => retorna o menor ou o maior valor em um iterável (todos os iteráveis) ou o menor/maior de dois ou mais elementos

    ATENÇÃO:    podemos passar quaquer número de valores para serem comparados ->> Python devolvera mim ou max ou
                ambos como queira
                Para explorar o máximo dos recursos de min() e max() utilize o help, observe que usaremos, por exemplo
                o parâmetro key ->> que recebe uma função (lambda, por exemplo)
                help(max) ou herl(min)

                Help on built-in function max in module builtins:
                    max(...)
                    max(iterable, *[, default=obj, key=func]) -> value
                    max(arg1, arg2, *args, *[, key=func]) -> value

                    With a single iterable argument, return its biggest item. The
                    default keyword-only argument specifies an object to return if
                    the provided iterable is empty.
                    With two or more arguments, return the largest argument.

                Na própria IDE TECLE ctrl SOBRE A FUNÇÃO e terá acesso a:
                ef min(*args, key=None): # known special case of min

                    min(iterable, *[, default=obj, key=func]) -> value
                    min(arg1, arg2, *args, *[, key=func]) -> value

                    With a single iterable argument, return its smallest item. The
                    default keyword-only argument specifies an object to return if
                    the provided iterable is empty.
                    With two or more arguments, return the smallest argument.
"""

lista = [1, 8, 4, 2, 99, 3, 101, 0]
print(f'Testanto min() e max() em uma lista ->> min {min(lista)} e max ->> {max(lista)}')
tupla = (1, 8, 4, 2, 99, 3, 101, 0)
print(f'Testanto min() e max() em uma tupla ->> min {min(tupla)} e max ->> {max(tupla)}')
conjunto = {1, 8, 4, 2, 99, 3, 101, 0}
print(f'Testanto min() e max() em um set ->> min {min(conjunto)} e max ->> {max(conjunto)}')
dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 2, 'e': 99, 'f': 3, 'g': 101, 'h': 0}
print(f'Testanto min() e max() em um dicionário ->> min {min(dicionario)} e max ->> {max(dicionario)}')  # Retorna as chaves de min e max
print(f'Testanto min() e max() em um dicionário ->> min {min(dicionario.values())} e max ->> {max(dicionario.values())}')  # Retorna min e max em valores

print(f'--------------------------------------Subindo o nível------------------------------')
# Nosso desafio agora será criar um programa que receba dois valores do usuário e mostre o maior

# val1 = int(input('Informe o primeiro valor: '))
# val2 = int(input('Informe o segundo valor:  '))
# print(f'Tudo fica fácil com Python --> menor - min ->> {min(val1, val2)} - o maior ->> {max(val1, val2)}')

# Não há limites para Python ->> veja a seguir alguns exemplos

print(f'Sem limite - min ->> {min(4, 67, 234)} - max ->> {max(4, 67, 234)}')
print(f'Sem limite - min ->> {min("a", "b", "cebola")} - max ->> {max("a", "b", "cebola")}')
print(f'Sem limite - min ->> {min("a", "b", "c", "d", "e", "f")} - max ->> {max("a", "b", "c", "d", "e", "f")}')
print(f'Sem limite - min ->> {min(2.55, 7.98, 9.56, 1.23, 8)} - max ->> {max(2.55, 7.98, 9.56, 1.23, 8)}')
print(f'Sem limite - min ->> {min("Python para Ciência de Dados")} - max ->> {max("Python para Ciência de Dados")}')
# Observe que na string o menor valor é o espaço e o maior o ê

print(f'--------------------------------------Outros exemplos------------------------------')
nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
print(f'Min e max em uma lista de strings - min ->> {min(nomes)} - max ->> {max(nomes)}')
# Note que o retorno de maior ou maior leva em conta a ordem alfabética e nao o tamanho da String

# Para tratar essa questão e retornar o que se espera, como Maior Ollivander e menor Tim ->> vamos usar lambda
print(f'Usando lambda min ->> {min(nomes, key=lambda nome: len(nome))} - max ->> {max(nomes, key=lambda nome: len(nome))}')

# Elevando o grau de complexidade ->> uso do key
musicas = [
    {"titulo": "Thundestruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock in'roll, too young to die", "tocou": 32}
]

print(f'Usando a chave key min ->> {min(musicas, key=lambda musica: musica["tocou"])}\nmax ->> {max(musicas, key=lambda musica: musica["tocou"])}')

# DESAFIO =>> IMPRIMA somente o título da música mais e menos tocada

print(f'Usando a chave key min ->> {min(musicas, key=lambda musica: musica["tocou"])["titulo"]}\nmax ->> {max(musicas, key=lambda musica: musica["tocou"])["titulo"]}')

print(f'Usando a chave key min ->> {min(musicas, key=lambda musica: musica["tocou"])["tocou"]}\nmax ->> {max(musicas, key=lambda musica: musica["tocou"])["tocou"]}')

# DESAFIO =>> como encontrar a música mais e menos tocada sem usar max(), min() e lambda?

maximo, minimo = 0, 99999

print(f'Iniciando as variáveis maximo ->> {maximo} e minimo {minimo}')
for musica in musicas:
    if musica['tocou'] > maximo:
        maximo = musica['tocou']

for musica in musicas:
    if musica['tocou'] == maximo:
        print(f'Note que agora teve que escovar bits max ->> {musica["titulo"]}')

for musica in musicas:
    if musica['tocou'] < minimo:
        minimo = musica['tocou']

for musica in musicas:
    if musica['tocou'] == minimo:
        print(f'Note que agora teve que escovar bits min ->> {musica["titulo"]}')
