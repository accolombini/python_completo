"""
Alocação de memória em Python -> este é um laboratório apenas conceitual -> Lembre-se => tupo em Python é objeto

    OBS.:   1- Python inteligentemente reutiliza valores já alocados para novos valres, economizando espaço em memória
            2- Não se esqueça que a RAM de seu computador está dividida em partes, a memória Stack e a memória Heap
            3- Seu código é alocado na memória Heap e suas variáveis alocadas na memória Heap
            4- O que acontece com dados da memória que não estão mais sendo referenciados? Estes dados estão soltos
            5- Python por baixo dos panos ele cria uma referência para cada objeto criado e passa a gerenciar
            quantos objetos apontam para a mesma referência. Quando um objeto foi utilizado e não mais faz referncia
            à variável, Python decrementa o contador de referência e quando esse for zerado ele se encarrega da
            limpeza da memória. Quando a referência de controle do núemro de objetos é zerada, o objeto recebe
            o nome de Dead Object -> neste momento entra em ação o algoritmo de Garbage Colletor para
            fazer a faxina na memória. Para Python esse algoritmo recebe o nome de Reference Counting.

    EM PALAVRAS:    - Métodos e variáveis são criadas na memória stack
                    - Os objtos e instâncias são criadas na memória heap
                    - Um novo stack é criado durante a invocação de uma função ou método
                    - Stacks são destruídas sempre que uma função ou método retorna o valor
                    - O algoritmo de Garbage Collector é um mecanismo para limpar dead objects

    -------------------------------------------------------------------------------------
    |  Ambiente de trrabalho                 |  Memória                                 |
    --------------------------------------------------------------------------------------
    | x = 10                                 | x, y --> 10                               |
    | print(type(x)) <class 'int'>           |                                           |
    | y = x                                  |                                           |
    | if(id(x) == id(y)):                    |                                           |
    |    print(f'x e y referenciam a mesma posição de memória                            |
    | x = x + 1                              | x --> 11; y --> 10                        |
    | z = 10                                 | x --> 11; y, z --> 10                     |
    | class Carro:                           | Carro                                     |
    |     pass                               |                                           |
    | car = Carro()                          | car --> Carro                             |
    --------------------------------------------------------------------------------------


"""

x = 10
print(f'O tipo de x é -> {type(x)}')  # <class 'int'>

y = x

if id(x) == id(y):  # x e y referenciam ao mesmo objeto
    print(f'x e y referenciam ao mesmo objeto')

x = x + 1
if id(x) == id(y):  # Agora x e y referenciam objetos diferentes, observe.
    print(f'x e y referenciam ao mesmo objeto após atribuição de 1 em x?')
else:
    print(f'Agora x e y referenciam objetos diferentes, observe.')

z = 10

if id(z) == id(y):  # z e y referenciam ao mesmo objeto
    print(f'z e y referenciam ao mesmo objeto')
else:
    print(f'Agora z e y referenciam objetos diferentes, observe.')


class Carro:
    pass


car = Carro()


def funcao2(x):
    x = x + 1
    print(f'O valor de x na funçao2 vale -> {x}')  # O valor de x na funçao2 vale -> 11
    return x


def funcao1(x):
    x = x * 2
    print(f'O valor de x na funçao1 vale -> {x}')  # O valor de x na funçao1 vale -> 10
    y = funcao2(x)
    print(f'O valor de y na funçao1 vale -> {y}')  # O valor de y na funçao2 vale -> 11
    return x, y


y = 5
z = funcao1(y)
