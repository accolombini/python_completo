"""
Sistemas de arquivos manipulação => usar Python para criar arquivos, diretórios, deletar, etc.

    ATENÇÃO:    1- no ambiente LINUX - recomenda-se o uso de os.mknod() para criar arquivos. Este método não
                funciona no WINDOWS
                2- tome cuidado com os comando de deleçao. Ao deletar um arquivo ou diretório, eles
                não vão para a lixeira, eles somem.
                3- Este é um módulo muito extenso, para maiores informações consulte:
                https://docs.python.org/3/library/os.html
    OBS.:       1- se não tivermos permissão para criarmos arquivo ou diretório, teremos um PermissionError
                2- se estiver no windows e o arquivo que for deletar estiver em uso, terá um erro
                3- pode ser que tenha problemas ao trabalhar com arquivos temporários se estiver utilizando
                uma máquina Windows. Isso por conta do Windows trabalhar de forma diferente seu sistema de arquivos
                temporários

"""
# Importando os
import os
# Importanto tempfile
import tempfile
# Importando a biblioteca send2trash
from send2trash import send2trash

# Descobrindo se um arquivo ou diretório existe ->> usando paths relatvos
print(
    f'Verificando a existência de um arquivo -> {os.path.exists("arquivo.txt")}\nSeu tipo é ->>{type(os.path.exists("arquivo.txt"))}')  # False - Seu tipo é <class 'bool'>
print(f'Verificando a existência de um arquivo -> {os.path.exists("frutas.txt")}')  # True

# Descobrindo se existe um diretório ->> usando paths relatvos
print(f'Verificando a existência de um diretório -> {os.path.exists("geek")}')  # True
print(f'Verificando a existência de um diretório -> {os.path.exists("python")}')  # False
print(f'Verificando a existência de um diretório -> {os.path.exists("geek/python")}')  # True

#  Descobrindo se existe um diretório ->> usando paths absolutos

print(f'Verificando a existência de um diretório -> {os.path.exists("d:/python_completo/geek/python")}')  # False
print(f'Verificando a existência de um diretório -> {os.path.exists("d:/JetBrains")}')  # True
print(
    f'Verificando a existência de um diretório -> {os.path.exists("d:/JetBrains/PyCharm Community Edition 2019.3.3")}')  # True

# Criando arquivos ->> forma antiga e não profissional ->> mas no windows é o que temos

# Forma 1 ->> com a diretiva 'w'
open('arquivo_teste1.txt', 'w').close()  # Cria e já fecha o arquivo

# Forma 2 ->> com a diretiva 'a'
open('arquivo_teste2.txt', 'w').close()  # Cria e já fecha o arquivo

# Forma 3 ->> usando with
with open('arquivo_teste3.txt', 'w') as arquivo:
    pass  # Recurso para dizer que não faremos nada neste bloco

# Criando diretórios únicos ->> segundo as melhores práticas de programação =>> uso de os.makedirs() ou os.mkdir()

# os.makedirs('arquivo_teste4.txt')  # Caso tente criar um arquivo que já exista terá uma mensagem de erro -> FileExistsError:
os.makedirs('d:/users/Angelo/arquivo_teste5.txt',
            exist_ok=True)  # Caso tente criar um arquivo que já exista terá uma mensagem de erro -> FileExistsError:. Ao adionar o parâmetro exist_ok=True não teremos mais a mensagem de erro

# os.mkdir('arquivo_teste5.txt')  # Caso já exista teremos -> FileExistsError:
# os.mkdir('d:/users/Angelo/arquivo_teste6.txt')  # # Caso já exista teremos -> FileExistsError:

# Criando diretórios aninhados ->> segundo as melhores práticas de programação =>> uso de os.makedirs() ou os.mkdir()
# Observe que não conseguimos com esse recurso criarmos todos os diretórios de uma única vez.
# os.mkdir('temp')
# os.mkdir('temp/teste')
# os.mkdir('temp/teste/outro')

# Criando diretórios ->> segundo as melhores práticas de programação =>> uso de os.makedirs()
# Caso exista dará FileExistsError

# os.makedirs('temp/teste/outro')  # cria toda estrutura anterior em uma única linha

# Podemos contornar a mensagem de erro, simplesmente adicionando um parâmetro, neste caso, se existir
# a estrutura de arquivos não teremos a mensagem de erro, observe.

# os.makedirs('temp/teste/outro', exist_ok=True)  # cria toda estrutura anterior em uma única linha

# Renomeando arquivos e diretórios usando -> os.rename()

# os.rename('temp', 'template')  # Observe que é renomeado e toda estrutura é mantida, como deveria ser.
# Caso tente renomera para um nome já existene terá um erro do tipo ->> FileExistsError
# Caso o diretório que esteja tentando renomear não estiver vazio teremos um ->> OSError

# Renomeando arquivos e diretórios usando -> os.rename()

# os.rename('temp/teste/outro/teste_rename.txt', 'temp/teste/outro/mais_um.txt')  # Observe que você deverá passar
# o caminho completo para renomear seu arquivo, caso não faça terá erro, assim também, caso o arquivo não seja
# encontrado termos uma menagem ->> FileNotFoundError:
# Renomeando em qualquer ponto da hierarquia de diretórios
# os.rename('temp/teste', 'temp/template')  # Se não existir terá um ->> FileNotFoundError:

# Removendo um arquivo -> os.remove()

# os.remove('para_deletar.txt')  # Caso o arquivo não exista teremos um erro ->> FileNotFoundError:

# Caso tente utilizar -> os.remove() para remover um diretório terá um erro ->> IsADirectoryError

# os.remove('template')  # Caso o arquivo não exista teremos um erro ->> FileNotFoundError ou PermissionError

# Para remover diretórios vazios ->> use os.rmdir()
# Se a pasta não estiver vazia você terá um -> OSError
# Se o diretório não existir termos um -> FileNotFoundError

# os.rmdir('template')

# Removendo uma árvore de diretórios -> remove o que está dentro do diretório deixando-o zerado
# Se não encontrar o arquivo teremos -> FileNotFoundError
# for arquivo in os.scandir('D:/OneDrive/CURSOS/UNIVERSIDAE/LINGUAGENS/PYTHON/teste'):
#    if arquivo.is_file():
#        os.remove(arquivo.path)

# Podemos remover uma árvore de diretórios. Os diretóros devem estar vazios use ->> os.removedirs()
# Se ao longo da árvore de diretórios for encontrado algum diretório não vazio, o processo de remoção para
# os.removedirs('teste/outro/mais_um')  # Caso tente remover uma árvore de diretórios que não exist -> FileNotFoundError

# ATENÇÃO: ao remover arquivos e diretórios com Python, eles somem, mas podemos querer enviar esses arquivos para
# a lixeira e poder recuperá-los caso algo dê errado.
# Precisaremos instalar um pacote de terceiros para esse fim -> pip install Send2Trash
# No Linux, pode ser que precise antes instalar -> sudo apt-get install lsb-core

# Vamos aos testes - criamos dois arquivos um deverá ser excluído permanentemente o outro enviado para a lixeira
# os.remove('para_lixeira.txt')  # Não vai para a lixeira. É deletado imediatamente
# Se o arquivo não existir teremos -> FileNotFoundError
# send2trash('para_lixeira2.txt')  # Vai para a lixeira. Poderá ser restaurado
# Se o arquivo não existir teremos -> OSError

# Enviando um diretório inteiro para a lixeira
# send2trash('temp')  # É possível enviar e restauraros arquivos/diretórios

# Podemos também trabalhar com arquivos e diretórios temporários. Precisaremos de mais um import -> import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em -> {tmp}')
    with open(os.path.join(tmp, 'arqivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Olá mundo!! Cheguei!!!\n')
        arquivo.write('Observe que tudo o que foi aprendido se aplica aqui\n')
#    input()  # Apenas para segurar o sistema. Necessário para fins didáticos de visualização
# Fora dos blocos with os arquivos deixam de existir -> são fechados e por serem temporários não os visualizamos
# Observe o retorno => C:\Users\accol\AppData\Local\Temp\tmp2f1un5jq ->> Note os nomes atribuídos pelo sistema
# Confira e está tudo ok
# NOTA: ao pressionar <enter> saimos do input e os arquivivos e diretórios temporários serão eliminados


# Neste exemplo vamos trabalhar apenas com arquivo temporário. Note que devemos utilizar o cast 'b' de binary
# Pois só conseguimos escrever em binário neste tipo de arquivo, acompanhe.
# ATENÇÃO: ao trabalhar no windows com binário -> tenha muito cuidado com acentos e caracteres especiais - EVITE-OS

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Ola mundo!!!\n')  # Note o não uso de acentos
    tmp.write(b'Estamos de volta!!!\n')
    tmp.seek(0)  # Controlando o cursor para impressão
    print(f'Imprimindo nosso arquivo temp -> {tmp.read()}')

# Neste exemplo faremos quase a mesma coisa sem o uso do bloco with ->> observe

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Ola mundo!!!\n')
print(f'Imprimindo o arquivo -> {arquivo.name}')  # Arquivo criado em ->> C:\Users\accol\AppData\Local\Temp\tmpzr0epvem
# input()  # Só para manter o arquivo temporário para visualização
# Não se esqueça de fechar o arquivo
arquivo.close()
