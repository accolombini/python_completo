"""
Definindo Funções => funções são pequenos blocos de código que realizam tarefas bem definidas.
    - Pode ou não receber entrada de dados e retornar uma saída de dados
    - São muito úteis para executar procedimentos similares por repetidas vezes


OBS.:   Caso sua função (escrita por você) realize várias tarefas dentro dela =>> recomenda-se
        fortemente que faça uma verificação para que a função seja simplificada ao máximo,
        podendo inclusive se tornar mais de uma função com escopo reduzido e muito bem
        definido (muito importante para se trabalhar com grandes sistemas)

Ao longo deste lab já utilizamos várias funções como:
    - print()
    - len()
    - max()
    - min()
    - count()
    - e muitas outras ...

Podemos observar a função print() mais de perto -> print(help(print) no corpo do código ou
help(print) no Python Console -> >>> help(print)

Mas como podemos definir uma função em Python?
    def nome_da_funcao(parametros_de_entrada):
        bloco_da_função

Onde:
    nome_da_funcao ->> SEMPRE, com letras minúsculas, e se for nome composto, separado por undeline (Snake Case):
    parametros_de_entrada ->> são OPCIONAIS, onde tendo mais de um, separa-se por vírgula, e havendo,
    ainda podem ser opcionas ou obrigatórios
    bloco_da_funcao ->> também chamado de corpo da função ou implementação da função, é onde o processamento
    da função acontece. É neste bloco, que PODE TER OU NÃO retorna da função para o sistema

OBS.: note que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que estamos
definindo uma funçao. Também abrimos o bloco_da_funcao com os DOIS PONTOS (:) =>> que na linguagem Python é
utilizado para definr blocos

UMA DICA:   recorrente em programação profissional ->> DRY -> Don't Repeat Yourself =>> Não repita você mesmo
            Não repita seu código

"""

# Exemplo de utilização de funções
cores = ['verde', 'amarelo', 'azul', 'branco']
# Primeiro utilizando fuções integradas da linguagem Python que são também chamadas de (Built-in)
# A função print(), por exemplo
print(f'Imprimindo a lista cores -> {cores} \nSeu tipo é -> {type(cores)}')

curso = 'Python para Ciência de Dados'
print(f'Imprimindo a string curso -> {curso} \nSeu tipo é -> {type(curso)}')

# Usando a função append() -> note o tipo de ação que ela executa e compare com a função print()
cores.append('roxo')
print(f'Imprimindo a lista cores (após append()) -> {cores} \nSeu tipo é -> {type(cores)}')

# Note que a varável precisa ter o atributo append() para que essa função possa ser utilizada, note a seguir um erro
# curso.append('Outro curso') -> Teremos uma AttributeError, pois a função string não possui o atributo append()

# Há funções que não recebem, ou não precisam de parâmetros de entrada -> veja a função clear() a seguir
cores.clear()
print(f'Imprimindo a lista cores após clear() -> {cores} \nSeu tipo é -> {type(cores)}')

# Definindo uma função
# Exemplo 1


def diz_oi():
    print(f'Esta função é simpatica responde sempre -> {"Oi"}')


"""
OBS.: 
    1- Note que, dentro de uma função podemos utilizar outras funções
    2- Observe que essa função execute somente uma tarefa, ou seja, a única coisa que ela faz é dizer Oi
    3- Esta é uma função que não recebe parâmetro algum de entrada
    4- Esta é uma função que não retorna nada para o sistema que a chama -> não existe o comando ->> return

"""
# Para executar precisamoschamar a função ->> no caso seu nome. Note que é preciso o uso dos parenteses () para
# que a função exute suas ações -> teste eliminando o parenteses () e observe o que acontece
# Formas erradas de chamar uma função: diz_oi | diz_oi ()
# Forma correta de chamar uma função: diz_oi()
diz_oi()

# Exemplo 2:


def cantar_parabens():
    print('Parabens a você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva ...')


cantar_parabens()

# Ou num for teremos
for n in range(5):
    cantar_parabens()

# Em Python, podemos CRIAR VARIÁVEIS do TIPO DE UMA FUNÇÃO e executar esta função através da variável
# Na atribuição da função não se utiliza o parêntes

canta = cantar_parabens  # Observe que NÃO usamos o parêntes da função nesta atribuição ok

print(f'-----------------------------------Separando ações-------------------------------')
canta()
