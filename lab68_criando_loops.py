"""
Criando Loops =>> criando sua própria versão de loop

"""

# O que sabemos e praticamos ->> sabemos isso ...

for num in [1, 2, 3, 4, 5]:  # iter([1, 2, 3, 4, 5])
    print(f'Iterando na lista -> {num}')  # next(num)

for letra in 'Python Ciência de Dados':  # iter('Python Ciência de Dados')
    print(f'Iterando na lista -> {letra}')  # nest(letra)

# Criando um loop ->> observe como é simples criar um loop para imprimir um iterável


def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(f'Meu for -> {next(it)}')
        except StopIteration:
            break


meu_for('Python')
numeros = [1, 2, 3, 4, 5, 6, 100, 200, 300]
print(f'\n')
meu_for(numeros)
