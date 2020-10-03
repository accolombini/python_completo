# -*- coding:utf8 -*-  # Necessário para sistema operacional Windows
"""
Escrevendo em arquivos CSV =>   a lógica para escrever em arquivos CSV é a mesma utilizada na leitura, logo,
                                podemos fazer a seguinte analogia:

                                - reader() leitor <=> writer() escritor
                                - writerow() => escreve uma linha

# Primeira forma -> writer() => gera um objeto para que possamos escrever em um arquivo CSV. Utilizamos
# o método writerow() para escrever cada linha. Ester método recebe uma lista (iterável)

from csv import writer


with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = ' '
    escritor_csv.writerow(['Titulo', 'Genero', 'Duracao'])
    while filme.lower() != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme.lower() != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (minutos): ')
            escritor_csv.writerow([filme, genero, duracao])
            print('Filme Adicionado!')

arquivo.close()


# Como segundo exemplo vamos trabahar com DictWriter => Permite uma melhor gestão sobre o cabeçalho

from csv import DictWriter

with open('filmes.csv', 'w', encoding='utf8') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Entre com o título do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero do filme: ')
            duracao = input('Informe a duracao do filme em minutos: ')
            escritor_csv.writerow({'Título': filme, 'Gênero': genero, 'Duração': duracao})

arquivo.close()

"""

# Como segundo exemplo vamos trabahar com DictWriter => Permite uma melhor gestão sobre o cabeçalho
# As chaves do seu dicionário devem reproduzir com fidelidade o cabeçalho do seu projeto -> lembre-se disso
# Atenção, como estamos usando a diretiva 'w' na abertura do arquivo, sempre que o arquivo
# for aberto, será reescrito seu conteúdo!

from csv import DictWriter

with open('filmes.csv', 'w', encoding='utf8') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)  # Note que fieldnames é um argumento do tipo *args
    # que nos permite passar um coneiner contendo o cabeçalho todo
    escritor_csv.writeheader()  # Observe que temos um método específico para escrever nosso cabeçalho
    filme = ' '
    while filme.lower() != 'sair':
        filme = input('Entre com o título do filme: ')
        if filme.lower() != 'sair':
            genero = input('Informe o gênero do filme: ')
            duracao = input('Informe a duracao do filme em minutos: ')
            escritor_csv.writerow({'Título': filme, 'Gênero': genero, 'Duração': duracao})
            print(f'Filme adiconado com sucesso!!!')

arquivo.close()
