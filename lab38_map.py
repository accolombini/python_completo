"""
Map ->> com map, fazemos mapeamento de valores para uma função

    - Map é uma função que recebe dois argumentos => o primeiro é uma função e o segundo um iterável
    - Sintaxe => var = map(função, iterável) => o retorno de map() um map object -> para visualizar
    seu conteúdo você deve utilizar um cast: list(), tuple(), set() ...
    IMPORTANTE: A partir do primeiro momento que o map object foi utilizado ele é zerado!!! Fique atento <$>

"""
import math

# Para este exemplo vamos trabalhar com cálculo de área de um circulo


def area(r):
    """
    Cáclulo da área de um círculo de raio r
    :param r: Recebe como parâmetro o raio do circulo
    :return: Retorna a área do círculo
    """
    return math.pi * r ** 2


print(f'Testando a função área -> {area(2)}')
print(f'Testando a função área -> {area(22.35)}')

# A função está funcionando muito bem!
# Imagine que ao invés de raio você tenha raios, muitos raios para calcular a muitas áreas
# Aqui um exemplo com pouquissímos raios
raios = [2, 5, 7.1, 0.3, 10, 44, 100]

# Um forma tranquila para resolver esse problema é a seguinte =>> Forma 1
areas = []
for r in raios:
    areas.append(area(r))

print(f'Resolvendo para uma lista de raios -> {areas}')

# Refatorando para o uso de map =>> Forma 2 ->> note o uso do cast list() para impressão
areas = map(area, raios)
print(f'Utilizando map() -> {areas}\nSeu tipo é {type(areas)}')  # Retorna um map objetct
print(f'Utilizando map() com list() -> {list(areas)}\nSeu tipo é {type(areas)}')  # usando o cast list() retorna o coteúdo de map() object

areas = map(area, raios)
print(f'Utilizando map() com tuple() -> {tuple(areas)}\nSeu tipo é {type(areas)}')  # Usando o cast tuple

areas = map(area, raios)
print(f'Utilizando map() com set() -> {set(areas)}\nSeu tipo é {type(areas)}')  # Usando o cast set
print(f'Utilizando map() com set() -> {set(areas)}\nSeu tipo é {type(areas)}')  # Observe que esse resultado será vazio
# isso ocorre porque o map objetct já fora utilizado uma vez


# O mesmo problema tratado em uma única linha

print(f'Utilizando map() -> {tuple(map(area, raios))}\nSeu tipo é {type(areas)}')  # Usando o cast tuple

# Forma 3 ->> utilizando lambda com a função map()

print(f'Usando lambda com map() -> {list(map(lambda raio: math.pi * (raio ** 2), raios))}')


# Para fixar o conceito de Map ->> temos dados iteráveis -> it; temos uma função f(x) =>> a função map(f, it)
# =>> map irá 'mapear' cada elemento do iterável à função

# Exemplo final ->> neste exemplo temos uma lista de cidades e suas temperaturas médias em graus Celsius
# Pede-se exibir a lista de cidades com a temperatura média expressa em Fahrenheit

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londres', 22)]

print(f'A variável cidades é -> {cidades}\nSeu tipo é {type(cidades)}')

# Fórmula de conversão =>> f = 9/5 * c + 32
# Usando lambda para a conversão temos
# Não use lambda assim, ok aqui estamos construindo os passos da solução
c_para_f = lambda dado: (dado[0], 9/5 * dado[1] + 32)

print(f'Mapeando cidades e convertendo a temperatura com map -> {list(map(c_para_f, cidades))}')

# Usando lambda da forma correta e profissional ->> teste de lambda foi ok
print(f'Mapeando cidades e convertendo a temperatura com map -> {list(map(lambda dado: (dado[0], 9/5 * dado[1] + 32), cidades))}')
