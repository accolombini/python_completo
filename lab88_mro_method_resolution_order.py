"""
POO =>> MRO Method Resolution Order -> Resolução de Ordem de Métodos, é a ordem de execução dos métodos
        (quem será executado primeiro). Esse fato é muito importante quando se trabalha com heranças múltiplas.
        Trata-se justamente da forma como o Python estrura o uso dos métodos conforme as classes são herdadas.

        Em Python, podemos conferir a ordem de execução dos métodos (MRO) de três formas diferentes:
            - Via propriedade da classe __mro__
            - Via método mro()
            - Via help

"""

# Exemplo real


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou -> {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Aquatico, Terrestre):  # Herança múltipla ->> Atenção a ordem é importante
    # Atenção da forma como está quando o Pinguim cumprimentar, como será seu cumprimento?
    def __init__(self, nome):
        super().__init__(nome)


# Testando ->> Lembra do que ocorreu na classe Pinguim quando invertermos a ordem de herança?

tux = Pinguim('Tux')
print(f'{tux.cumprimentar()}')  # A execução aqui é uma questão de Method Resolution Order - MRO Foi executado
# neste caso Eu sou Tux da terra!. Este resultado ocorre quando a classe Pinguim(Terrestre, Aquatico). Observe
# o resultado quando inverto a classe Pinguim(Aquatico, Terrestre) temos como resultado -> Eu sou Tux do mar!


# Observe o uso dos três métodos para visualizar a sequência de operações mro

"""
Pinguim.__mro__
(<class 'lab88_mro_method_resolution_order.Pinguim'>, <class 'lab88_mro_method_resolution_order.Aquatico'>, <class 'lab88_mro_method_resolution_order.Terrestre'>, <class 'lab88_mro_method_resolution_order.Animal'>, <class 'object'>)
Pinguim.mro()
[<class 'lab88_mro_method_resolution_order.Pinguim'>, <class 'lab88_mro_method_resolution_order.Aquatico'>, <class 'lab88_mro_method_resolution_order.Terrestre'>, <class 'lab88_mro_method_resolution_order.Animal'>, <class 'object'>]
help(Pinguim)
Help on class Pinguim in module lab88_mro_method_resolution_order:
class Pinguim(Aquatico, Terrestre)
 |  Pinguim(nome)
 |  
 |  Method resolution order:
 |      Pinguim
 |      Aquatico
 |      Terrestre
 |      Animal
 |      builtins.object
 |  
 |  Methods defined here:
"""
