"""
Bloco with =>   é utilizado para criar um contexto de trabalho onde os recursos utilizados são
                fechados após o bloco with. O uso do bloco with é a forma correta de se trabalhar
                com arquivos em Python
                Passos para se trabalhar com arquivos:
                1- Abrimos o arquivo
                1- Manipulamos o arquivo
                3- Fechamos o arquivo

                NOTA: ao sair do contexto with o arquivo já estará fechado, pois o mesmo só estará disponível
                dentro do contexto ao qual foi criado
                FORMA GERAL DO BLOCO WITH:
                    with open('nome_arquivo') as apelido_arquivo:
                        realize ações, por exemplo:
                        print(f'Imprima os dados do arquilo -> {apelido_arquivo.read())

"""
# O uso do bloco with ->> neste exemplo o arquivo será aberto para impriessão de sua primeira linha
with open('texto.txt') as arquivo:
    print(f'Testando o bloco with ->> {arquivo.readline()}')  # Imprime a primeira linha do arquivo
# A seguir vamos provar que o bloco with fechou o arquivo. observe o erro =>> ValueError: I/O operation on closed file.
# print(f'Só para demonstra que o arquivo foi fechado ou ele não existe mais fora do contexto ->> {arquivo.read()}')
# Vamos confirmar se o arquivo esta realmente fechado ->> retorno deverá ser booleano
print(f'Conferindo se o arquivo foi fechado ->> {arquivo.closed}')  # Retorno -> True
