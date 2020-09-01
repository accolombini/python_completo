"""
Modos de Abertura de Arquivos => define a forma de operação do arquivo, para saber mais consulte
        https://docs.python.org/3/library/functions.html#open. Algumas opções estão descritas abaixo:

        r => abre o arquivo para leitura é a forma padão
        w => abre o arquivo para escrita - cria um novo arquivo ou sobrescreve um arquivo já existente
        x => abre o arquivo para escrita - falha se o arquivo já existir. Se existir recebera uma mensagem de
        erro -> FileExistsError: [Errno 17] File exists
        a => abre o arquivo para escrita adicionando o conteúdo ao final do arquivo, caso exista, caso não, um novo
        arquivo será criado para escrita. ATENÇÃO escreverá SEMPRE NO FINAL, não aceita o uso de seek() para controlar
        o cursor.
        + => abre para o módulo de atualização, deve ser utilizado sempre com outra diretiva, por exemplo,
        r+ (aceita o uso do seek() para posicionar o cursor; w+ (sobrescreve não aceita seek())
        -> a+ (adiciona no final ->> não se controla o cursor não aceita seek())

"""
# Exemplo do uso do modo de abertura x -> observe a construção usando try except
try:
    with open('univeridades.txt', 'x') as arquivo:
        arquivo.write('Universidades Brasileiras.\n')
        arquivo.write('Universidade Federal de Itajubá.\n')
        arquivo.write('Universidade de São Paulo.\n')
except FileExistsError:
    print(f'O arquivo já existe e não poderá ser sobrescrito!!!')

# Exemplo do uso do modo de abertura a

with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite ->> sair para encerrar: ')
        if fruta.upper() != 'SAIR':
            arquivo.write(fruta + ' ')
        else:
            break


# Exemplo do uso do modo de abertura + e trabalhando com a diretiva r para controlar o cursor

with open('fruta.txt', 'r+') as arquivo:
    print(f'Conteúdo por linha do arquivo ->> {arquivo.readline()}')
    arquivo.seek(44)
    print(f'Conteúdo por linha do arquivo ->> {arquivo.readline()}')
    arquivo.seek(0)
    print(f'Conteúdo por linha do arquivo ->> {arquivo.readline()}')
    arquivo.seek(44)
    arquivo.write('Substituindo essa linha por nova linha - linha 2')  # irá sobrescrever, mas o resultado não é interessante
    arquivo.write('\n')
