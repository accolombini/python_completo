"""
Reversed =>> a função reversed() funciona com qualquer tipo de iterável, sua função é inverter o iterável

    ATENÇÃO:    a função reversed retorna um iterável do tipo <class 'list_reverseiterator'>. Para acessá-lo
                devemos usar um cast para convertê-lo
                seu valor de retorno será um objeto <list_reverseiterator object at 0x000002333DDFC7C0>
                pode-se converter o elemento retornado para uma lista, uma tupla ou um conjunto (set), não
                se esqueça que com set{} não guardamos a ordem ...
                nós podemos iterar com reversed normalmente
                podemos também usar o reversed() para fazermos um loop for reverso

    OBS.:   não confunda com a função reverse() estudada em listas. Lembre-se que o retorno da função reverse()
            é o tipo NoneType
            outro detalhe é o fato de que a função reverse() só se aplica a listas

"""

lista = [1, 2, 3, 4, 5]
print(f'A função reverse() estudada em lista ->> {type(lista.reverse())} ->> {lista}')

# Usando reversed()

print(f'Usando reversed em lista temos ->> {type(reversed(lista))}\nSeu valor de retorno ->> {reversed(lista)}')
print(f'Usando reversed em lista temos ->> {type(reversed(lista))}\nSeu valor de retorno ->> {list(reversed(lista))}')
print(f'Usando reversed em tupla temos ->> {type(reversed(lista))}\nSeu valor de retorno ->> {tuple(reversed(lista))}')
# Atenção ->> em conjunto não definimos a ordem dos elementos
print(f'Usando reversed em conjuntos temos ->> {type(reversed(lista))}\nSeu valor de retorno ->> {set(reversed(lista))}')

# Podemos iterar sobre reversed() ->> o uso do terminador end='' ->> é para escrevermos na mesma linha
for letra in reversed('Python para Ciência de Dados'):
    print(f'{letra}', end="")
# Podemos fazer ou obeter o mesmo resultado sem o uso do comando for ->> observe o uso do .join()
print(f'')  # Só para pular uma linha
print(f'Sem o uso do for, com join =>> {"".join(list(reversed("Python para Ciência de Dados")))}')

# Faremos agora o mesmo de uma forma bem mais simples  utilizando o slice de string =>> observe
print(f'Usando slice de string =>> {"Python para Ciência de Dados"[::-1]}')

# Podemos também usar o reversed() para fazermos um loop for reverso
for n in reversed(range(0, 10)):
    print(f'Imprime reverso de range ->> {n}')

# Podemos também fazer isso usando o próprio range()
for n in range(9, -1, -1):
    print(f'Imprime reverso de range ->> {n}')
