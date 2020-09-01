"""
StringIO => para ler ou escrever dados em arquivos do sistema operacional o software precisa
            ter permissão.
            - Permissão de leitura ->> para ler um arquivo
            - Permissao de escrita ->> para escrever em um arquivo

            StringIO => utilizado para ler e criar arquivos na memória ->> não será gravado no disco. Requer
            import do módulo StringIO
"""
# Fazendo o import do módulo StringIO
from io import StringIO

mensagem = 'Esta é apenas uma string normal'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para que possamos depois inserir
# alguma informação nele. Para isso basta:
# Este arquivo estará disponível para leitura e escrita com a possibilidade de controlar o cursor com seek()
arquivo = StringIO(mensagem)  # Equivale a ->> arquivo = open('arquivo.txt', 'r', 'w')

# Agora que o arquivo foi criado podemos manipluar o arquivo como já aprendido nas aulas anteriores
# Arquivo criado e aberto podemos trabalhar
print(f'Imprimindo nosso arquivo da memória -> {arquivo.read()}')
# Vamos escrever no arquivo
arquivo.write('\nEsta é a nova string feita especialmente para teste de inclusão \n')
# Vamos posicionar o cursor para uma nova leitura
arquivo.seek(0)
# Vamos conferir o resultado de nossa nova inserção no arquivo
print(f'Imprimindo com novo conteúdo -> {arquivo.read()}')
