"""
Entendendo Iterators e Iterables => o objetivo dessa prática é entender o que é iterators e o que são iterables.

        Iterator =>>    um objeto que pode ser iterado.
                        um objeto que retorna um dado, sendo um elemento por vez quando uma função
                        next() é chamada
        Iterable =>>    um objeto que irá retornar um iterator quando a função iter() form chamada
"""

nome = 'Python'  # Uma string como se sabe é um iterável (iterable)
numeros = [1, 2, 3, 4, 5, 6]  # Uma lista como se sabe é um iterável (iterable)

print(f'Entendo iterator e iterable -> {nome} - Seu tipo -> {type(nome)}')
print(f'Entendo iterator e iterable -> {numeros} - Seu tipo -> {type(numeros)}')

# A seguir mostramos que a string e a lista são iteráveis não iterators ->> observe
# print(f'Entendo iterator e iterable -> {next(nome)}') # Teremos um erro -> TypeError: 'str' object is not an iterator
# print(f'Entendo iterator e iterable -> {next(numeros)}') # Teremos um erro -> TypeError: 'list' object is not an iterator

# Podemos tornar os iterables iterators ->> observe que estamos chamando a função iter() nos iteráveis. Note o retorno
it1 = iter(nome)
it2 = iter(numeros)

print(f'Entendo iterator e iterable -> {next(it1)} - Seu tipo -> {type(it1)}')  # Retorna P Seu tipo <class 'str_iterator'>
print(f'Entendo iterator e iterable -> {next(it2)} - Seu tipo -> {type(it1)}')  # Retorna 1 Seu tipo <class 'str_iterator'>

# iteragindo até o limite -> Note o erro ao tentar ir além dos limites
print(f'Entendo iterator e iterable -> {next(it1)} - {next(it2)}')
print(f'Entendo iterator e iterable -> {next(it1)} - {next(it2)}')
print(f'Entendo iterator e iterable -> {next(it1)} - {next(it2)}')
print(f'Entendo iterator e iterable -> {next(it1)} - {next(it2)}')
print(f'Entendo iterator e iterable -> {next(it1)} - {next(it2)}')
# print(f'Entendo iterator e iterable -> {next(it1)} - {next(it2)}')  # Erro ->> StopIteration

# Para finalizar, sempre que realiza uma iteração o Python estará convertendo seu iterable com a função iter()
# em um iterator e aplicando a função next() para percorrê-lo

nome = 'Dados'
for letra in nome:  # Aplica a função iter()
    print(f'Na verdade estamos imprimindo iterators -> {letra}')  # Usa next() para percorrer um a um
