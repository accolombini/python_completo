"""
Forçando tipos de dados com decoradores =>  como se sabe, Python não é uma linguagem tipada
                                            imagine uma situação, onde se precise definir de forma
                                            explicita os tipos de dados, neste caso, usa-se como boa
                                            prática de programação os decorators

                        NOTA:   1- A função zip() junta duas tuplas pegando um elemento de uma e outro
                                elemento de outra.
                                    a = (1, 2, 3)
                                    b = (4, 5, 6)
                                    c = zip(a, b) =>> (1, 4), (2, 5), (3, 6)
"""


def forca_tipo(*tipos):  # Note que *tipos equivale a *args -> o nome aqui é para facilitar como apoio didático
    def decorador(funcao):  # Esta será a função decorador -> aquela que irá alterar o comportamento
        def converte(*args, **kwargs):  # Lembre-se que estes parâmetros são imutáveis. Podemos receber dif. valores
            novo_args = []  # Necessário, pois os parâmetros são imutáveis e aqui queremos manipulá-los
            for valor, tipo in zip(args, tipos):
                novo_args.append((tipo(valor)))  # Observe aqui que tipo é na verdade um cast para *tipos
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador


@forca_tipo(str, int)  # Note que estamos decorando -> str para msg e int para vezes
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(f'{msg}')


# Testando
repete_msg('Python', '5')  # Contador literal
print(f'\n')
repete_msg('Python', 3)  # Contador inteiro


@forca_tipo(float, float)  # Note que estamos decorando -> float para a e float para b
def dividir(a, b):
    print(f'{a/b}')


print(f'\n')
dividir(5, 4)
dividir('5', 20)
