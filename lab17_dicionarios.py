"""
Dicionários => são coleções do tipo chave/valor -> mapeamento entre chave/valor => de forma explicita
OBS.: Em algumas linguagens de programação, os dicionários Python são conhecidos como mapas

Dicionários são representados por caves {}

OBS.: Sobre dicionários
    - Chave e valor são separados por dois pontos -> chave: valor
    - O conjunto chave/valor forma um item no dicionário -> itens são separados por vírgulas
    chave: valor, chave2: valor2, chave2: valor3 ...
    - Tanto a chave quanto o valor podem ser de qualquer tipo de dados
    - Podemos facilmente misturrar tipos de dados diferentes
    - Dicionários não são indexados no mesmo conceito que listas e tuplas => o acesso é através das chaves
    _ Podemos definir um padrão para o caso de não encontrarmos o objeto com a chave informada

NOTA: Em Python tipo None representa ausência de tipo, ou em outras palavras, sem tipo -> <class 'NoneType'>
      O tipo Nome é sempre especificado com a inicial maiúscula >>= seu retorno em Python é sempre False
      Certo -> None
      Errado -> none
      Quando utilizamos o tipo None?
        - Podemos utilizar None quando queremos criar uma variável e inicializá-la com um tipo, antes
        de atribuir-lhe o valor final, ou o valor de trabalho
        - Caso o get não encontre o objeto com a chave informada será retornado o valor None e não
        será gerado KeyError

"""
# Criação de diconários
# Forma 1 => mais comum
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(f'O dicionário paises é -> {paises} - seu tipo é -> {type(paises)}')

# Forma 2 => menos comum
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(f'O dicionário paises é -> {paises} - seu tipo é -> {type(paises)}')

# Acessando elementos em um dicionário

# Forma 1 => acessando via chave, da mesma "forma que listas/tuplas" => se usar uma chave que não exista
# no dicionário teremos um KeyError
print(f'Imprimindo países utilizando suas chaves -> {paises["br"]}')
print(f'Imprimindo países utilizando suas chaves -> {paises["eua"]}')
print(f'Imprimindo países utilizando suas chaves -> {paises["py"]}')

# Forma 2 => acessando via get -> essa é a forma recomendada => caso tente chamar algum elemento
# não existe no dicionário terá como retorno o tipo -> None
print(f'Imprimindo países utilizando get -> {paises.get("br")}')
print(f'Imprimindo países utilizando get -> {paises.get("eua")}')
print(f'Imprimindo países utilizando get -> {paises.get("py")}')
print(f'Imprimindo países utilizando get -> {paises.get("jp")} - seu tipo é -> {type(paises.get("jp"))}')

# Exemplo 1 -> None
numeros = None
print(f'Imprimindo numeros -> {numeros} - seu tipo é -> {type(numeros)}')
numeros = 1.44, 1.34, 5.67
print(f'Imprimindo numeros -> {numeros} - seu tipo é -> {type(numeros)}')

# Exemplo 2 -> None => observe que o suo do get() proporciona uma mair versatilidade ao código
russia = paises.get('ru')
if russia:
    print(f'Se encontrei Russia em paises -> {"Encontrei!!!"} - seu tipo é -> {type(russia)}')
else:
    print(f'Se não encontrei Russia em paises -> {"Não Encontrei!!!"} - seu tipo é -> {type(russia)}')

# Exemplo 3 -> None => observe que o uso do get() proporciona uma maior versatilidade ao código
# observe a seguir o uso de uma claúsula padrão
pais = paises.get('py', 'Não encontrado')
if pais:
    print(f'Se encontrei -> {pais} - em pais e seu tipo é -> {type(pais)}')
else:
    print(f'Se não encontrei -> {pais} - em paises e seu tipo é -> {type(pais)}')

# Exemplo 4 -> None => observe que o uso do get() proporciona uma maior versatilidade ao código
# observe a seguir o uso de uma claúsula padrão e note que não precisamos do if utilizado no exemplo 3
pais = paises.get('jp', 'Não encontrado')
print(f'Sem if -> {pais} - em pais e seu tipo é -> {type(pais)}')

# Exemplo 5 -> não há busca por valor => Podemos verificar se determinada chave se encontra em um dicionário
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(f'Não busca por valor Usando a chave br -> {"br" in paises}')
print(f'Não busca por valor Usando o valor Estados Unidos -> {"Estados Unidos" in paises}')
print(f'Não busca por valor Usando uma chave desconhecida pt -> {"pt" in paises}')

# Observe uma forma de capturar mensagem de erro => na verdade evitar uma mensagem de erro
if 'pt' in paises:
    Portugal = paises['pt']

# Podemos utilizar qualquer tipo de dados (int, float, string, boolean), inclusive listas, tupla, dicionário =>
# como chave de um dicionário
# Exemplo => neste caso estamos utilizando uma tupla como chave de um dicionário -> observe que está é uma
# opção interessante, pois como já sabemos, as tuplas são imutáveis
localidades = {
    (35.6894, 139.692): 'Escritório em Tókio',
    (-2.92887, -44.9357): 'Escritório de Nova York',
    (-23.5489, -46.6388): 'Escritório de São Paulo'
}
print(f'Imprimindo localidade -> {localidades} - e seu tipo é -> {type(localidades)}')

# Adicionar elementos em um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(f'Imprimindo receita -> {receita} - e seu tipo é -> {type(receita)}')

# Exemplo 1 -> adicionando um novo item ao dicionário receita
receita['abr'] = 350
print(f'Imprimindo receita após adição de abr -> {receita} - e seu tipo é -> {type(receita)}')

# Exemplo 2 -> fazendo uso do método update
novo_dado = {'mai': 500}
print(f'Quem é novo_dado -> {novo_dado} - e seu tipo é -> {type(novo_dado)}')
receita.update(novo_dado)
print(f'Imprimindo receita após adição de novo_dado -> {receita} - e seu tipo é -> {type(receita)}')

# Atualizando dados em um diconário
# Forma 1
receita['mai'] = 550
print(f'Imprimindo receita após adição atualizar valor -> {receita} - e seu tipo é -> {type(receita)}')

# Forma 2
receita.update({'mai': 600})
print(f'Imprimindo receita após adição atualizar valor -> {receita} - e seu tipo é -> {type(receita)}')

# CONCLUSÃO 1: a forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma
# CONCLUSÃO 2: em dicionários não podemos ter chaves repetidas

# Como remover dados de um dicionário
# Forma 1 -> utilizando o método pop() => mais comum de ser utilizada
ret = receita.pop('mai')  # É preciso sempre fornecer a chave
print(f'O valor de retorno de pop("mai") está na variável ret e seu valor é -> {ret}')
print(f'Imprimindo receita após o uso do método pop("mai") -> {receita} - e seu tipo é -> {type(receita)}')
# OBS 1: na forma 1 sempre precisamos informar a chave, e caso não encontre o elemento, será retornado um KeyError
# OBS 2: ao removermos um objeto, seu valor é sempre retornado

# Forma 2 -> uso do comando del
del receita['fev']
print(f'Imprimindo receita após o uso do comando del ["fev"] -> {receita} - e seu tipo é -> {type(receita)}')

# Se a chave não existir será gerado um KeyError
# OBS.: neste caso não há retorno de valor -> o valor excluído não é retornado

# USO DO DICIONÁRIO
# Imagine hipoteticamente que você tem um comércio eletrônico, onde temos um carrinho de compras na
# qual adicionamos produtos para pagar ao final da compra

"""
Carrinho de compras:
    Produto 1:
        nome;
        quantidade;
        preço;
    Produto 2:
        nome;
        quantidade;
        preço;
"""
# 1 - Podemos representar essa proposta como uma Lista? Sim podemos
carrinho = []
produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(f'Nosso carrinho de compras com o uso de listas é -> {carrinho} - e seu tipo é -> {type(carrinho)}')
# OBS.: neste caso, nosso carrinho é uma lista de listas, assim, teríamos que saber qual é o índice de cada produto

# 2 - Podemos usar uma Tupla para esse projeto? Sim -> podemos usar qualquer coleção para esse projeto
produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)
carrinho = (produto1, produto2)
print(f'Nosso carrinho de compras com o uso de Tuplas é -> {carrinho} - e seu tipo é -> {type(carrinho)}')
# OBS.: neste caso, nosso carrinho é uma tupla de tuplas, assim, teríamos que saber qual é o índice de cada produto

# 3 - Podemos usar um Didionário para esse produto? Sim e observe a performance
carrinho = []  # NOTA: é importante que carrinho seja uma lista => acompanhe
produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}
carrinho.append(produto1)
carrinho.append(produto2)
print(f'Nosso carrinho de compras com o uso de Dicionários é -> {carrinho} - e seu tipo é -> {type(carrinho)}')
# OBS.: neste caso, nosso carrinho é uma lista de dicionários,
# assim, temos como saber qual é o índice de cada produto
# NOTA: desta forma podemos adicionar ou remover produtos, alterar quantidade, etc e ainda em cada produto
# temos a certeza sobre cada uma das informações que compreendem o produto comprado

# Métodos próprios para se trabalhar com dicionários -> dir({})
d = dict(a=1, b=2, c=3)
print(f'Nosso novo Dicionários para testes é -> {d} - e seu tipo é -> {type(d)}')

# Limpar o dicionário - zerar dados => uso do método clear()
d.clear()
print(f'Apagando o novo Dicionários com o método clear() -> {d} - e seu tipo é -> {type(d)}')

# Copiando um dicionário para outro
d = dict(a=1, b=2, c=3)

# Forma 1 => Deep Copy
novo = d.copy()
print(f'Nosso novo Dicionários para testes é -> {d} - e seu tipo é -> {type(d)}')
print(f'Copiando o dicionário d para o dicionário novo com o método copy() -> {novo} - e seu tipo é -> {type(novo)}')

# Alterando o dicionário novo e avaliando o impacto no dicionário d

novo['d'] = 4
print(f'Avaliando o dicionário d após alterar o dicionário novo -> {d} - e seu tipo é -> {type(d)}')
print(f'Nosso novo foi acrescido de "d" -> {novo} - e seu tipo é -> {type(novo)}')

# Forma 2 => Shallow Copy -> neste caso uma alteração em um altera-se também o outro

novo = d
print(f'Nosso novo Dicionários para testes é -> {d} - e seu tipo é -> {type(d)}')
print(f'Copiando o dicionário d para o dicionário novo por atribuição -> {novo} - e seu tipo é -> {type(novo)}')

# Alterando o dicionário novo e avaliando o impacto no dicionário d

novo['d'] = 4
print(f'Avaliando o dicionário d após alterar o dicionário novo -> {d} - e seu tipo é -> {type(d)}')
print(f'Nosso novo foi acrescido de "d" -> {novo} - e seu tipo é -> {type(novo)}')

# Forma não usual de criar dicionários usando o método fromkeys() -> passando chave/valor
outro = {}.fromkeys('a', 'b')  # Neste caso => a é a chave e b é o valor
print(f'Novo dicionário criado de forma não convencional outro -> {outro} - e seu tipo é -> {type(outro)}')

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(f'Novo dicionário criado de forma não convencional usuario -> {usuario} - e seu tipo é -> {type(usuario)}')

# OBS.: o método fromkeys recebe dois parâmetros: um iterável e um valor
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chaveo valor informado

veja = {}.fromkeys('teste', 'valor')  # Note que teste é um iterável para fromkeys e será desmembrado como a seguir
# onde cada letra da string será tratada com um iterável e note que o último 'e' não foi convertido, isso ocorre
# porque nos dicionários em Python não podem haver repetições de chaves
print(f'Novo dicionário criado de forma não convencional veja -> {veja} - e seu tipo é -> {type(veja)}')

vejanovo = {}.fromkeys(range(1, 11), 'novo')
print(f'Novo dicionário criado de forma não convencional vejanovo -> {vejanovo} - e seu tipo é -> {type(vejanovo)}')
