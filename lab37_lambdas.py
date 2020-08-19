"""
Utilizando Lambdas ->> conhecidas por expressões lambdas =>> são na verdade, funções sem nome (anônimas)
    - Estrutura de uma função lambda => lambda par1, par2, ...: <expressão de retorno de lambda>
    - NOTA: Se passarmos mais argumentos do que parâmetros esperados =>> teremos TypeError
    - OBS.: Lambdas são muitos usada para filtrar e ordenar dados =>> importante essa dica

    Função em Python tem a sintaxe abaixo:
        def soma(a, b):
            :return a + b

"""


# Exemplo de uma função em Python ->> revisão


def funcao(x):
    return 3 * x + 100


print(f'Revisando o uso de função Python -> {funcao(25)}')

# Exemplo de expressão lambda ->> resolvendo o mesmo problema de funcao(). Note a necessidade de uma atribuição
# isso é necessário porque lambda é uma palavra reservada
# ATENÇÃO => a forma de uso de lambda abaixo não é considerada a forma correta de seu uso, embora os resultados
# serão exatamente os obtidos através da função func()


calc = lambda x: 3 * x + 100

print(f'Usando lambda para solucionar o problema de funcao -> {calc(25)}')

# Podemos ter expressões lambdas com múltiplas entradas => a função do método strip() é remover
# possíveis espaços em branco deixados na digitação dos dados de entrada ->> Só retira espaços de início
# e fim de uma string - o método title() capitaliza a string


nome_completo = lambda nome, sorenome: nome.strip().title() + ' ' + sorenome.strip().title()


print(f'Usando lambda com multiplas entradas -> {nome_completo("josé", "maria")}')


# Em funções Python podemos ter nenhuma ou várias entradas. Em lambdas também!!!

nenhuma = lambda: 'Python para Ciência de Dados'
uma = lambda x: 3 * x + 100
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 30 / (1 / x + 1 / y + 1 / z)

print(f'Usando lambda -> {nenhuma()}')
print(f'Usando lambda -> {uma(100)}')
print(f'Usando lambda -> {duas(5, 7)}')
print(f'Usando lambda -> {tres(3, 6, 9)}')

# Outro exemplo de lambda ->> lista de autores =>> referência Amazon books

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(f'Imprimindo a lista de autores -> {autores}\nSeu tipo é -> {type(autores)}')

# O desafio desse exemplo é ordenar essa lista pelo sobrenome -> observe que na lista há nome e sobrenome, nome, nome
# do meio e sobrenome, abreviaturas, etc

# Utilizando o método sort() com lambda. Note que neste caso sim estamos utilizando a expressão lambda corretamente,
# ou memlhor dizendo, profissionalmente
# Note que o método split() separa o nome em uma lista separando cada parte do nome por " " e [-1] garante que você
# peqgue exatamente o último sobrenome e o método lower() deixa tudo minúsculo para fazer a ordenação, neste caso
# a lista esta corretamente digitada e seu uso é opcional, mas pense que uma lista extensa poderá haver erros de
# digitação e sue código deverá estar apto a corrigi-los

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(f'Imprimindo a lista de autores ordenada -> {autores}\nSeu tipo é -> {type(autores)}')

# Exemplo de lambda em expressões ->> no caso função quadrática do tipo =>> f(x) = a * x ** 2 + b * x + c
# Definindo a função quadrática
# Observe como essa construção é interessante =>> a função geradora_funcao_quadratica() recebe três argumentos
# e retorna lambda =>> lambda por sua vez recebe um parâmtro x e retorna a expressão quadrática


def geradora_funcao_quadratica(a, b, c):
    """
    Retorna a função f(x) = a * x ** 2 + b * x + c
    :param a: Parâmeto que multiplica x ** 2
    :param b: Parâmeto que multiplica x
    :param c: Parâmeto independente
    :return: retorna o resultado da fórmula de Bascara
    """
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, -3, -15)
print(f'Testando a função geradora_funcao_quadratica -> {teste(2)}')
print(f'Testando a função geradora_funcao_quadratica -> {teste(20)}')


# Vamos agora eliminar a variável teste e ir direto para o print() =>> observe

print(f'Testando a função geradora_funcao_quadratica sem o uso de uma variável -> {geradora_funcao_quadratica(3, 0, 1)(2)}')
