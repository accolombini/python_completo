"""
Seek e Cursors =>   a função seek() é utilizada para movimentar o cursor dentro do arquivo.
                    a função seek() recebe um argumento posicionando o cursor no ponto de início de leitura
                    desejado


            NOTA:   Pode ser interessante percorrer o arquivo - linha a linha, neste caso a função read()
                    não se aplica.
                    Para resolver esse problema utilizamos a função readln()

"""
# Trablhando com seek()
arquivo = open('texto.txt')
print(f'Imprimindo o arquivo texto.txt ->> Observe a seguir: \n{arquivo.read()}')
# Já sabemos, caso tente imprimir novamente o mesmo texto terá como retorno texto em branco
print(f'Imprimindo o arquivo texto.txt pela segunda vez ->> Observe a seguir: \n{arquivo.read()}')


# Para resolver esse problema, vamos agora verificar como movimentar o cursor pelo arquivo utilizando a função seek()

arquivo.seek(0)  # Retorna a posição inicial do arquivo
print(f'Imprimindo o arquivo texto.txt pela segunda vez com seek() ->> Observe a seguir: \n{arquivo.read()}')
arquivo.seek(13)  # Posiciona o cursor na poição 13
print(f'Imprimindo o arquivo texto.txt pela segunda vez com seek() ->> Observe a seguir: \n{arquivo.read()}')


# Trabalhando com a função readln() ->> precisamos reposicionar o cursor na posição zero ->> apenas para
# fins didáticos

arquivo.seek(0)
print(f'Imprimindo o arquivo texto.txt usando a função readln() ->> Observe a seguir: \n{arquivo.readline()}')
# Para imprimir as demais linhas do arquivo será necessário:
print(f'Imprimindo o arquivo texto.txt usando a função readln() ->> Observe a seguir: \n{arquivo.readline()}')
print(f'Imprimindo o arquivo texto.txt usando a função readln() ->> Observe a seguir: \n{arquivo.readline()}')
print(f'Imprimindo o arquivo texto.txt usando a função readln() ->> Observe a seguir: \n{arquivo.readline()}')

# Sempre ao conhecer uma nova função é interessante observar o tipo de retorno ou se há ou não retorno
arquivo.seek(0)
ret_readln = arquivo.readline()
print(f'Conhecendo o retorno de readln ->> {type(ret_readln)}')  # Observe que a classe é <class 'str'>

# Novamente, tudo o que aprendemos para string se aplica aqui
print(f'Explorando a classe string ->> {ret_readln.split()}')  # Converte a string em uma lista de string
