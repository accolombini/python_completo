"""
Leitura de Arquivos =>  para ler o conteúdo de um arquivo em Python, utilizamos a função integrada open() ->>
                        literalmente significa abrir

                        open() =>> na sua forma mais simple de utilização passamos apenas um parâmetro de entrada
                        que neste caso é o nome do arquivo a ser lido que é o caminho para encontrar o arquivo.
                        Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos.

                        Para conhecer todos os parâmetros suportados pela função open() e potencializar ainda mais
                        seu uso, recomendamos a leitura de ->> https://docs.python.org/3/library/functions.html#open

                        OBS.:   Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir
                                ou então teremos o erro FileNotFoundError
                                Para ler um arquivo após sua abertura precisamos usar a função read(). Fique atento
                                pois ao terminar a leitura o cursor (Python usa o conceito de cursor) para caminhar
                                por um arquivo, assim, o cursor será posicionado após o final do arquivo, isso
                                significa que, se tentar um segunda leitura terá como retorno - vazio
                                Podemos dizer que a função read() lê todo o conteúdo do arquivo.

"""
# Exemplo de utilização

arquivo = open('texto.txt')
# Impressão do arquivo ->> <_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
# Typo de dados do arquivo ->> <class '_io.TextIOWrapper'>
print(f'Imprimindo o arquivo -> não seu conteúdo ->> {arquivo}\nSeu tipo é ->> {type(arquivo)}')
# Vamos agora conhecer o retorno da função read(). Observe que tudo o que aprendeu de string se aplica aqui!
ret = arquivo.read()
print(f'Entendendo o retorno da função read() -> {type(ret)}')  # Seu tipo é <class 'str'>
print(f'Explorando string', ret.split('\n'))  # Retorna uma lista de strings
# A seguir vamos ler o conteúdo do arquivo
print(f'Lendo o conteúdo do arquivo -> {arquivo.read()}')
# A seguir vamos demonstrar o que acontece quando tentamos ler o arquivo pela segunda vez
print(f'Lendo o conteúdo do arquivo pela segunda vez -> {arquivo.read()}')
