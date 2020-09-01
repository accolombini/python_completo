"""
Escrevendo em arquivos  =>  independentemente do que deseja fazer com arquivos, primeiro será necessário abrí-lo
                            NOTA: ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas
                            poderemos ler. Da mesma forma se abrirmos um arquivo para escrita, só poderemos
                            escrever nele. Não será possível ler esse arquivo. A diretiva para abertura de
                            um arquivo no modo de escrita é 'w'. Para escrever no arquivo, usamos a função
                            write(). Esta função (write()) recebe uma string como parâmetro. Argumentos diferentes
                            de string retornam um TypeError.

                            NOTA:   1- ao abrir um arquivo para escrita, o arquivo será criado no sistema operacional.
                                    2- abrindo um arquivo paa escrita com o módulo 'w', se o arquivo não existir será
                                    criado, caso já exista, o anterior será apagado e um novo será criado. Dessa forma
                                    todo o conteúdo existente no arquivo será perdido.
"""

# Exemplo de escrita - modo 'w' -> write (escrita) =>> Modo correto de utilização em Python
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever em arquivos em Python é muito fácil.\n')
    arquivo.write('Podemos escrer a quantidade de texto que for necessária.\n')
    arquivo.write('Está nossa última linha!!\n')

# Exemplo de escrita - modo 'w' -> write (escrita) =>> Modo não recomendado, mas que poderá encontrar, só para saber
arquivo_errado = open('mais_pode_encontrar.txt', 'w')
arquivo_errado.write('Para que conheça de tudo, inclusive o que não fazer\n')
arquivo_errado.write('Este é mais um arquivo para fixar os conceitos\n')
arquivo_errado.write('Você deve conhecer as possibilidades\n')
arquivo_errado.close()  # Lembre-se sempre de fechar o arquivo

# Exemplo ->> novo exemplo usando um iterável no bloco with ->> explorando os conhecimentos de strings
with open('python.txt', 'w') as arquivo_interessante:
    arquivo_interessante.write('Python ' * 10)

# Exemplo ->> recebendo dados do usuário e escrendo esses dados num arquivo
with open('frutas.txt', 'w') as entra_usuario:
    while True:
        fruta = input('Entre com uma fruta ou para encerra ->> digite SAIR: ')
        if fruta.upper() != 'SAIR':
            entra_usuario.write(fruta + ' ')
        else:
            break  # Estamos num loop infinito e precisamos sair deste loop
