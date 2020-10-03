"""
Lendo arquivos CSV => Coma Separeted Values -> Valores Seprados por vírgula.

        Observações:    1- O primeiro ponto aqui é ter consciência de que podemos ter outros tipos de separadores que
                        não apenas a vírgula e ainda estamos tratando de um arquivo CSV, o importante é que exista um
                        padrão, não pode haver mistura de separadores. Os separadores mais comuns:
                             - Separador por vírgulas -> 1, 2, 3, 4, 5 => "python", "ciência de dados", "ml"
                             - Separador por ponto e virgulas -> 1; 2; 3; 4; 5 => "python"; "ciência de dados"; "ml"
                             - Separador por espaço ->  1  2  3  4  5 => "python"  "ciência de dados"  "ml"

                        2- Você pode conseguir muitos dados para testes e simulações em: http://dados.gov.br/dataset
                        3- A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV:
                            - reader -> permite que iteremos sobre as linhas do arquivo CSV como se fossem listas
                            - DictReader -> Permite que iteremos sobre as linhas do arquvio CSV como OrderedDicts

# Iniciando seus trabalhos -> como arquivos não recomendado

with open('lutadores.csv', 'r', encoding='utf8') as arquivo:  # 'r' não é necessário já é defautl para Python
    dados = arquivo.read()
    print(f'Qual o tipo de dados? -> {type(dados)}')
    dados = dados.split(',')
    print(f'Imprimindo dados \n {dados}')

arquivo.close()

# Trabalhando com CSV -> usando reader

from csv import reader

with open('lutadores.csv', encoding='utf8') as arquivo:
    leitor_csv = reader(arquivo)  # A grande sacada aqui é que reader() devolve cada linha numa lista facilitando
    # o processo de iteração e manipulação de seu arquivo. Ainda temos um problema, observe que o cabeçalho está
    # sendo impresso como um dado, mas podemos não querer isso.
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)s {linha[1]} e mede {linha[2]} centimetros')

arquivo.close()

print(f'\n')

# Vamos refatorar nosso código para não trabalhar com o cabeçalho como um dado. Lembre-se da vantagem de
# estar usando iterators, observe
# Você pode confirmar o retorno de readerf() posicionando o mause sobre ele pressionando CTRL -> note que
# o retorno é um iterator, logo, tudo o que apresndeu sobre iterators vale para este caso

with open('lutadores.csv', encoding='utf8') as arquivo:
    leitor_csv = reader(arquivo)  # A grande sacada aqui é que reader() devolve cada linha numa lista facilitando
    # o processo de iteração e manipulação de seu arquivo. Ainda temos um problema, observe que o cabeçalho está
    # sendo impresso como um dado, mas podemos não querer isso.
    next(leitor_csv)  # Simples assim, pulamos para o próximo iterável, no caso a linha seguinte ao cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)s {linha[1]} e mede {linha[2]} centimetros')

arquivo.close()

# Trabalhando com DictReader

from csv import DictReader

with open('lutadores.csv', 'r', encoding='utf8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict - Note que a chave é o cabeçalho, logo devem ser escritas exatamente
        # conforme especificado no cabeçalho do seu arquivo
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")

arquivo.close()

"""

# Trabalhando com DictReader -> com outro separador, lembre esses métodos consideram a vírgula o separador default

from csv import DictReader

with open('lutadores.csv', 'r', encoding='utf8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')  # Observe o uso do delimiter =, aqui especifique o
    # delimitador de seu arquivo, no caso estamos usando a vírgula e isso é desnecessário, mas imagine
    # que o delimitador fosse '$', ficaria no seu código da seguinte forma => delimiter='$'
    for linha in leitor_csv:
        # Cada linha é um OrderedDict - Note que a chave é o cabeçalho, logo devem ser escritas exatamente
        # conforme especificado no cabeçalho do seu arquivo
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")

arquivo.close()
