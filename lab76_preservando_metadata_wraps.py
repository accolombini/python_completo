"""
Preservando metadados com wraps =>  metadados são dados intrinsecos em arquivos
                                    wraps são funções que envolvem elementos com diversas finalidades

                    NOTA:   Para resolver o problema de documentação decorrente do uso de decorators
                            será necessário realizar o import =>> from functools import wraps
                            Wraps -> como poderá ser observado é na verdade um decorator próprio da linguagem
                            Python
                            Recomenda-se fortemente no uso de programação profissional.

# Problema para entendimento


def ver_log(funcao):
    def logar(*args, **kwargs):
       #
        Eu sou uma função chamada logar e estou dentro da função ver_log
        :param args:
        :param kwargs:
        :return: é a função (funcao(*args, **kwargs)
        #
        print(f'Você está chamando a função {funcao.__name__}')  # Retorna o nome da função
        print(f'Aqui a documentação: {funcao.__doc__}')  # Retorna a documentação da função
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    #
    Função soma dois números
    :param a: deve ser um númeri inteiro ou ponto flutuante
    :param b: deve ser um númeri inteiro ou ponto flutuante
    :return: a + b
    #
    return a + b


print(f'Teste de metadados -> {soma(7, 9)}')

# Vamos aos possíveisproblemas ->> observe que ao esperar os resultados para soma() tenho os resultados de logar()
# Isso ocorre porque os metadados da função soma() estão sendo alterados pelo ->> decorator. CUIDADO!!
print(f'Conferindo os resultados -> {soma.__name__}')  # Veja o retorno de nome -> logar
print(f'Conferindo os resultados {soma.__doc__}')  # o retorno de doc -> logar


"""
# Para resolver o problema precisamos importar wraps

from functools import wraps


# Resolvendo o problema ->> fazendo uso de wraps


def ver_log(funcao):
    @wraps(funcao)  # Basta isso para resolver o problema apresentado anteriormente
    def logar(*args, **kwargs):
        """
        Eu sou uma função chamada logar e estou dentro da função ver_log
        :param args:
        :param kwargs:
        :return: é a função (funcao(*args, **kwargs)
        """
        print(f'Você está chamando a função {funcao.__name__}')  # Retorna o nome da função
        print(f'Aqui a documentação: {funcao.__doc__}')  # Retorna a documentação da função
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """
    Função soma dois números
    :param a: deve ser um númeri inteiro ou ponto flutuante
    :param b: deve ser um númeri inteiro ou ponto flutuante
    :return: a + b
    """
    return a + b


# print(f'Teste de metadados -> {soma(7, 9)}')

# Vamos aos possíveisproblemas ->> observe que ao esperar os resultados para soma() tenho os resultados de logar()
# Isso ocorre porque os metadados da função soma() estão sendo alterados pelo ->> decorator. CUIDADO!!
print(f'Conferindo os resultados -> {soma.__name__}')  # Veja o retorno de nome -> logar
print(f'Conferindo os resultados {soma.__doc__}')  # o retorno de doc -> logar
