"""
Decoradores (Decorators) => 1- são funções -> envolvem outras funções e arpimoram seus comportamentos
                            2- também são exemplos de Higher Order Functions
                            3- decorators possuem uma sintaxe própria, usando "@" (Syntact Sugar / Açúcar Sintático)
                            4- na sintaxe do decorator não se esqueça de que não precisa dos parênteses da função
                            exemplo -> @seja_educado_mesmo -> note que não usamos o parênteses.
                            5- Não confunda Decorator (@seja_educado_mesmo) com
                            Decorator Funciton (ef seja_educado_mesmo(funcao):

    -------------------------------------------
    |            Function Decorator            |
    -------------------------------------------

    --------------------------------------------
    ||-----------------------------------------||
    ||            Função decorada              ||
    ||-----------------------------------------||
    -------------------------------------------

"""

# Decoradores como funções (essa Sintaxe não é recomendada), mas você poderá se deparar com ela em algum momento
# Este tipo de sintaxe não emprega o "@", ou seja, não possue o açúcar sintático

# Note neste exemplo que quando a função ->> seja_educado() for executada, seu retorno será sua
# função interna ->> sendo e não a execução da função
# Note que neste exemplo a função seja_educado() é um decorador da função que é passada como argumento, no caso
# é um decorador para a função saudacao()


def seja_educado(funcao):  # Essa é a função Decorator
    def sendo():
        print(f'Foi um prazer conhecer você')
        funcao()
        print(f'Tenha um ótimo dia!')
    return sendo  # É aqui que chamamos a função interna sendo()


def saudacao():
    print(f'Seja bem vindo ao curso Python para Ciência de Dados')

# Testando a função ->> Teste 1


teste1 = seja_educado(saudacao)
teste1()


# Testando a função ->> Teste 2


def raiva():
    print(f'EU TE ODEIO')


raiva_educada = seja_educado(raiva)
raiva_educada()

# Decorators com o Syntax Sugar (Áçúcar Sintático) =>> uso correto da sintaxe
print(f'\n')


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        funcao()
        print(f'Foi um prazer conhecer você!!')
        print(f'Tenha um excelente dia!!')
    return sendo_mesmo


@seja_educado_mesmo  # Está é a forma correta para Decorar uma função -> neste caso a função apresentando será decorada pela função seja_educado_mesmo
def apresentando():  # Esta é a função que desejo decorar
    print(f'Eu sou o Júlio')


# Testando ->> note que agora não precisamos criar uma variável, basta executar a função a ser decorada

apresentando()

# Outro teste
print(f'\n')


@seja_educado_mesmo
def cafe():
    print(f'Preciso de um café')


cafe()
