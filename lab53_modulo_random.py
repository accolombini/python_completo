"""
Módulo Random =>    em Python módulos nada mais sao do que outros arquivos Python. Módulo Random
                    adiona uma série de funcionalidades para facilitar o trabalho com números
                    pseudo-aleatórios -> (significa que pode haver repetição). Para conhecer mais
                    do módulo Random utilize (dir(random)), na console Python. Para conhecer mais
                    sobre uma função especíica do módulo basta (help(<nome_da_função>)). Como exemplo
                    help(random.random) -> random() method of random.Random instance
                    random() -> x in the interval [0, 1).

    OBS.:   Existem duas formas de utilizar um módulo ou uma função:
            - Forma 1 ->    import random (desta forma todo o módulo é importado) => assim, todas as funções, atributos,
                            classes e propriedades que estiverem presentes dentro do módulo ficarão disponíveis
                            (ficarão em memória) =>> não recomendado. O ideal é conhecer quais as funções que precisa
                            do módulo e fazer o import apenas das funções desejadas (Forma 2).
                            ATENÇÃO: O uso da forma 1 NÃO é recomendado
            - Forma 2 ->    importa uma função específica do módulo. Por exemplo, from random import random. É o mesmo
                            que dizer, do módulo random, importe a função randon(). Neste caso, você não deverá
                            fazer referência ao módulo ao usar a função. Exemplo, print(f'{random()}). Note que no
                            importe você não usa random() e sim o nome da função apenas random. Mas você deverá
                            fazer uso dos parêntes ao usar a função random().
                            ATENÇÃO: O uso da forma 2 É recomendado

    NOTA:   Para utilizar a função random() do pacote random, nós devemos chamá-la através do nome do pacote e o nome
            da função separados por ponto (.). Exemplo: random.random()
            Nunca confunda o pacote random com a função randon(). Pode soar estranho, mas a função randon() é apenas
            uma função dentro do módulo random.
"""
# Forma 1 -> Importando todo o módulo
# import random

# print(f'Testando a função random() -> {random.random()} - seu tipo é -> {type(random.random())}')

# Forma 2 -> Importando uma função específica do módulo
# from random import random

# print(f'Testando a função random() -> {random()} - seu tipo é -> {type(random())}')
# for i in range(10):
#    print(f'Testando random() -> {round(random(), 2) - seu tipo é -> {type(random())}')

# Podemos desejar gerar números pseudo-aleatórios com valores que estejam fora do intervalo de random() [0, 1)
# A função uniform() -> permite a geração de números pseudo-aleatórios entre o intervalo definido.

# from random import uniform

# for i in range(10):
#    print(f'Testando uniform() -> {round(uniform(3, 7), 2)} - seu tipo é -> {type(uniform(3, 7))}')  # Neste caso o 7 será exclusive ->> nunca gerado


# Até aqui geramos números pseudo-aleatórios em ponto flutuante, mas imagine o caso em que queira gerar números
# pseudo-aletórios inteiros em função da necessidade de sua aplicação. Para isso, devemos utilizar a função
# presente no módulo random chamada randint(). A função randint() gera números pseudo-aleatórios dentro do intervalo
# pré estabelecido.

# from random import randint

# Nosso desafio será gerar apostas para a mega-sena. Não se esqueça que pseudo-aleatório poderá haver repetição
# print(f'Gerando para a Mega_Sena ->> [1, 61)')
# for i in range(6):  # Range 0, 1, 2, 3, 4, 5
#    print(f'{randint(1, 61)}', end=', ')  # Note o limite superior igual a 61, isso porque ele não entra no cálculo


# A próxima função interessante do módulo random é a função choice(). A função choice() ->> mostra um valor aleatório
# presente em um iterável

# from random import choice
# Vamos emular o jogo Tesoura, Papel e Pedra usando choice()

# jogadas = ['pedra', 'papel', 'tesoura']  # Nosso iterável

# print(f'Nesta jogada escolho -> {choice(jogadas)}')
# print(f'Basta ser um iterável e poderei escolher -> {choice("Python^para^Ciência^de^Dados")}')

# A próxima função interessante do módulo random é a função shuffle(). A função shuffle() ->> embaralha os dados

from random import shuffle

# Imagine um jogo de cartas onde em algum momento precisamos embarlhar as cartas
cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
print(f'Sem embaralhar temos     -> {cartas}')
shuffle(cartas)
print(f'Embaralhando com shuffle -> {cartas}')
print(f'Distribuindo uma carta para o jogador -> {cartas[3]}')
print(f'Retirando a última carta do baralho para distribuir -> {cartas.pop()}')
