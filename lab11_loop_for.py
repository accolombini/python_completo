"""
Loop for -> trata-se de uma estrutura de repetição
for item in intervavel:
    execução do loop

Utilizamos loop para iteirar sobre sequências ou sobre valore iteráveis.
Exemplos de iteráveis => strings, listas, dicionários, tuplas, range

"""

nomes = 'Abacate maduro'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

# Exemplo de for -> 1 (iterando sobre strings)
for letra in nomes:
    print(f'Letras e espaços encontradas em nomes são => {letra}')

# Exemplo de for -> 2 (iterando sobre listas)
for numero in lista:
    print(f'Os números encontrados em lista são => {numero}')

# Exemplo de for -> 3 (iteirando sobre um range! Note o valor final de range é não inclusivo)
for numero in range(1, 10):  # Note que o 10 não entra nosso range irá de 1 a 9
    print(f'Os números encontrados em range são => {numero}')

# Trabalhando com enumerate -> retorna um objeto indice e valor ou índice ou valor
enum = enumerate(nomes)
print(f'Entendendo enumerate - seu tipo é uma classe => {type(enum)}')
# Podemos usar de várias formas -> alguns poucos exemplos (observe a diferença nesta construção do for)
for indice, letra in enumerate(nomes):
    print(f'Note o retorno de índice com o uso do enumerate {indice}')  # Observe que indice é na verdade o índice da
    # string nomes

for indice, letra in enumerate(nomes):
    print(f'Note o retorno de letra com o uso do enumerate {letra}')  # Observe que indice é na verdade não é utilizado

# Nota como o indice não é utilizado, a linguagem Python nos permite substituir requisitos que são serão utilizados
# pelo underline <=> _ Observe o mesmo exemplo acima repetido com o uso do _

for _, letra in enumerate(nomes):
    print(f'Note o uso de _ com for enumerate {letra}')

for indice, letra in enumerate(nomes):
    print(f'Note o uso de índice com for enumerate {indice}')
    print(f'Note o uso de letra com for enumerate {letra}')

for tudo in enumerate(nomes):
    print(f'Note agora que não estamos separando em índice valor, assim, teremos o retorno de ambos {tudo}')

for tudo in enumerate(nomes):
    print(f'Assessando apenas o índice => vale para valor também ok => {tudo[0]}')

# Exemplo de for -> 4 (definindo limite superior de execução)
qtd = int(input('Quantas vezes devo executar o loop? -> '))
for n in range (1, qtd + 1):
    print(f'Executando o for {qtd} => {n}')

# Exemplo de for -> 5 (explorando ainda mais a iteratividade com o usuário)
qtd2 = int(input('Quantas vezes devo executar o loop? -> '))
soma = 0
for n in range(1, qtd2 + 1):
    num = int(input(f'Informe o {n}/{qtd2} valor: '))
    soma = soma + num
print(f'O resultado de soma é {soma}')

# Exemplo de for -> 6 (melhorando a saída do comando for - string em uma linha)
for letra in nomes:
    print(f'{letra}', end='')
print('\n')  # Só para deixar o curso na próxima linha

# Exemplo de for -> 7 (usando Emojis => Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
# Extraido da tabela -> original: U+1F60B
# Convertendo para Python -> U0001F60B <=> basta substituir o sina de + por três zeros
for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60B' * num)
