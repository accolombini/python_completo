"""
Módulo Collections - Counter
Collections => High performance Container Datetypes

Counter -> recebe um iterável como parâmentro e cria um objeto do tipo Collections Counter que é
parecido com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor
a quantidade de ocorrências desse elemento.

Para saber mais => https://docs.python.org/3/library/collections.html#collections.Counter
Ou ainda utilize help(Counter)

"""
# Realizando o import de Counter

from collections import Counter


# Podemos usar qualquer iterável, neste exemplo estamos usando uma lista, mas todos são válidos

# Exemplo 1
lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 2, 2, 5, 5, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34, 100]

# Utilizando o Counter
res = Counter(lista)
print(f'Podemos ver o efeito do Counter imprimindo \n- res -> {res} \n- e seu tipo é -> {type(res)}')
# Veja que para cada elemento da lista, o Counter criou uma chave a partir dos valores da lista e gerou um valor
# a partir da quantidade de vezes que o elemento se repete na lista
# res -> Counter({5: 6, 2: 5, 3: 5, 4: 4, 1: 3, 45: 2, 66: 2, 43: 1, 34: 1, 100: 1})
# e seu tipo é -> <class 'collections.Counter'>

# Exemplo 2
print(f'Usando Counter com uma String observe o resultado \n-> {Counter("Python para Ciência de Dados")}')

# Exemplo 3
texto = """
Uma corrida armamentista naval entre Argentina, Brasil e Chile — países mais poderosos e ricos da América do Sul — começou no início do século XX, quando o governo brasileiro comprou três dreadnoughts, formidáveis embarcações couraçadas cujas capacidades ultrapassavam em muito a dos navios mais antigos das marinhas do resto do mundo.

Em 1904, a Marinha do Brasil ficou muito atrás de suas rivais argentina e chilena em qualidade e tonelagem total; poucos navios haviam sido encomendados desde a queda da monarquia brasileira em 1889, enquanto Argentina e Chile haviam acabado de concluir uma corrida armamentista naval de quinze anos que encheu suas marinhas com modernos navios de guerra."""

palavras = texto.split()
print(f'Conhecendo palavras após split() -> {palavras}')
res2 = Counter(palavras)
print(f'Podemos ver o efeito do Counter imprimindo \n- res2 -> {res2} \n- e seu tipo é -> {type(res2)}')

# Fica muito fácil encontrar as as top 3 mais recorrentes no nosso texto, veja como a seguir
print(f'As top 3 do nosso texto é -> {res2.most_common(3)}')

# Exemplo 4 => Observe o potencial de Counter
c = Counter(a=4, b=2, c=0, d=-2)
print(f'Podemos ver o efeito do Counter imprimindo \n- c -> {c} \n- e seu tipo é -> {type(c)}')
d = Counter(a=1, b=2, c=3, d=4)
print(f'Podemos ver o efeito do Counter imprimindo \n- d -> {d} \n- e seu tipo é -> {type(d)}')
c.subtract(d)
print(f'Podemos ver o efeito do Counter após subtração imprimindo \n- c -> {c} \n- e seu tipo é -> {type(c)}')
