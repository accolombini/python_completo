"""
Decorators com diferentes assinaturas => decorators functions com diferentes parâmetros de entrada

        NOTA:   1- Para resolver problemas com argumentos ->> usamos um padrão de projeto chamado
                Decorator Pattern
                2- A assinatura de uma funçõ é representada pelo seu retorno, nome e parâmetro de entrada
                3- Vale lembrar que podemos utilizar parâmetros nomeados e não nos preocuparmos com a ordem
                dos parâmetros
                4- Podemos ter Decorators com argumentos ->> confira

"""

# Relembrando


def gritar(funcao):  # Decorator function
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):  # Função que será decorada
    return f'Olá eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'


# Testando
print(f'{saudacao("Américo")}')

# print(f'{ordenar("Picanha", "Batata Frita")}')  # Teste sem o decorator -> Olá, eu gostaria de Picanha, acompanhado de Batata Frita, por favor.
# print(f'{ordenar("Picanha", "Batata Frita")}')  # Teste com o decorator -> TypeError: aumentar() takes 1 positional argument but 2 were given


# Refatorando com a Decorator Pattern
def gritar(funcao):  # Decorator function
    def aumentar(*args, **kwargs):  # Decorator Pattern
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):  # Função que será decorada
    return f'Olá eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'


print(f'{ordenar("Picanha", "Batata Frita")}')  # Resolvido -> OLÁ, EU GOSTARIA DE PICANHA, ACOMPANHADO DE BATATA FRITA, POR FAVOR.


@gritar
def lol():
    return f'lol'


print(f'Sem parâmetro -> {lol()}')


# Usando parâmetros nomeados
print(f'usando parâmetros nomeados -> {ordenar(acompanhamento="Batata Frita", principal="Picanha")}')


# Decorator com argumentos


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    return args


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


# Testando ->> validando argumentos

print(f'Teste de soma -> {soma_dez(10, 20)}')  # Observe -> Teste de soma -> Valor incorreto! Primeiro argumento precisa ser 10

print(f'{comida_favorita("pizza", "ravioli")}')
