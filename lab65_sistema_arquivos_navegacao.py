"""
Sistema de Arquivos e Navegação =>  para fazer uso de manipulação de arquivos do SO, precisamos importar
                                    e fazer uso do módulo os.
                                    os ->> Operating System -> Sistema Operacional

                                    ATENÇÃO:    Se estiver utilizando uma máquina Windows, terá que alterar a forma de
                                                verificação de diretório:
                                                WIN seria: D:\\OneDrive\\CURSOS\\UNIVERSIDADE\\LINGUAGENS
                                                MUDE para: D:/OneDrive/CURSOS/UNIVERSIDADE/LINGUAGENS
                                                POSIX    : /OneDrive/CURSOS/UNIVERSIDADE/LINGUAGENS
                                    NOTA:       Observe que no Windows usa-se barras duplas, isso porque a barra '\'
                                                é utilizada como caractere de scape oque nos obriga a duplicar as barras
                                                '\\' -> fique atento!!
"""
# Fazendo o import do módulo os
import os
import platform  # necessário caso queira mais detalhes do SO se estiver no Windows 10

# Imagine que nosso desafio é descobrir qual o diretório corrente -> getcwd() => pega o current work directory
# Seu tipo de retorno será <class 'bytes'> e seu retorno será o path (caminho) absoluto
print(f'Estamos trabalhando no diretório ->> {os.getcwdb()}\nSeu tipo é ->> {type(os.getcwdb())}')

# Agora se quisermos alterar o diretório usamos -> chdir() => permite que altere entre os diretórios de trabalho
# Seu tipo de retorno será <class 'NoneType'>. Poderá subir na hieraquia até atingir o diretório Raiz
os.chdir('..')  # Com este comando estaremos subindo um nível na hierarquiva de diretórios
print(f'Estamos trabalhando no diretório ->> {os.getcwdb()}\nSeu tipo é ->> {type(os.getcwdb())}')
print(f'O tipo de chdir() será ->> {type(os.chdir(".."))}')  # Com este comando estaremos subindo um nível na hierarquiva de diretórios
print(f'Estamos trabalhando no diretório ->> {os.getcwdb()}\nSeu tipo é ->> {type(os.getcwdb())}')

# Podemos verificar se um caminho é absoluto ou relativo usando ->> os.path.isabs() => Seu retorno será True ou False
# print(f'Será absoluto ou relativo/ ->> {os.path.isabs("D:/OneDrive/CURSOS/UNIVERSIDADE/LINGUAGENS")}')  # True
# print(f'Será absoluto ou relativo/ ->> {os.path.isabs("D:OneDrive/CURSOS/UNIVERSIDADE/LINGUAGENS")}')  # False

# Podemos identificar qual o sistema operacional local utilizando o módulo os ->> observe
print(f'Qual o sistema operacional corrente? ->> {os.name}')  # O retorno será 'posix' para Linux e MAC e 'nt' para Win
print(f'O tipo de retorno será ->> {type(os.name)}')  # Teremos uma string como retorno <class 'str'>

# Caso queira mais informação a respeito do sistema operacional corrente use ->> os.uname()
print(f'Detalhes do sistema operacional corrente ->> {platform.platform()}')  # Windows-10-10.0.19041-SP0
print(f'O tipo de retorno será ->> {type(platform.platform())}')  # Teremos uma string como retorno <class 'str'>

# Imagine uma situação na qual você deseja acrescentar um diretório ao caminho (path). Você está em path e deseja
# acrescentar um diretório a seu caminho use ->> os.path.join(). NOTA, mais de um salto acrescente víruglas e os
# os passos para percorrer sua árvore de arquivos
# NOTA: os.path.join() ->> recebe dois parâmetros, sendo o primeiro o diretório atual em seguinda acrescente quantos
# forems os passos para compor seu caminho - path
print(f'Para exemplificar vamos ver onde estamos -> {os.getcwdb()}')
print(f"Testando o uso de join diretamente -> {os.path.join(str(os.getcwdb()), 'SO_PARA_TESTE')}")
res = os.path.join(str(os.getcwdb()), 'SO_PARA_TESTE')
print(f'Olhando para o resultado de join pelo uso de uma variável->> {res}')

# Imagine agora que queremos listar o conteúdo de um diretório com o listdir()
print(f'Listando o conteúdo de um diretório ->> {os.listdir}')  # Seu valor de retorno será <built-in function listdir>
print(f'Listando o conteúdo de um diretório ->> {os.listdir()}')  # Retorna o conetúdo do diretório corrente
# Como o retorno é uma lista, podemos utilizar tudo o que foi aprendido em listas para manipular o resultado
print(f'Listando a dimensão do diretório ->> {len(os.listdir())} - arquivos/diretórios')
print(f'Listando o número de arquivos/diretórios do Disco D ->> {len(os.listdir("D://"))} - arquivos/diretórios')

# Podemos listas os arquivos e diretórios com mais detalhes com scandir()
# NOTA: sempre que trabalhar com scandir() será necessário fechar o processo da mesma forma que num arquivo

scanner = os.scandir()
arquivos = list(scanner)
# Importante, novamente temos como retorno uma lista e poderemos usar tudo que sabemos ->> <class 'list'>
print(f'Lendo um elemento da lista dir name -> {dir(arquivos[0].name)}')  # Nome do arquivo
print(f'Conhecendo nossa variável arquivos -> {arquivos}\nSeu tipo é -> {type(arquivos)}')
print(f'Lendo um elemento da lista inode -> {arquivos[0].inode()}')  # Retorna o número do inode (nó do diretório)
print(f'Lendo um elemento da lista name -> {arquivos[0].name}')  # Nome do arquivo
print(f'Lendo um elemento da lista stat -> {arquivos[0].stat()}')  # Valor de retorno são valores estatísticos, por exemplo o size do arquivo -> st_size=192205
print(f'Lendo um elemento da lista path -> {arquivos[0].path}')  # Caminho do diretório/arquivo

# Precisamos fechar scanner
scanner.close()
