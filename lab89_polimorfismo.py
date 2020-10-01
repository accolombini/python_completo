"""
POO - Polimorfismo =>>  Poli -> significa muitas =>> Morfis -> Formas - em outras palavras podemos dizer que
                        polimorfismo siginifica muitas formas ->> mais fácil mostrar do que falar, acompanhe!

        NOTA:   Quando reimplementamos um método presente na classe pai numa classe filha, estmos realizando
                uma sobrescrita de método (Overriding).
                O OVERRIDING é na verdade, a melhor representação daquilo que recebe o nome de Polimorfismo em POO.
                Note que nos exemplos o método falar permite que ao ser sobrescrito você crie variações da classe Pai
"""


# Entendendo Polimorfismo


class Animal(object):  # Não é necessário o objetct estou usando aqui para reforçar o conhecimento
    # de que toda classe por padrão gera de -> object
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):  # Só lembrando com raise você lança uma excessão. Neste caso, estamos lançando uma mensagem!
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self):
        print(f'{self.__nome} está comendo ...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala auauauau!')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miauuuu!')


class Rato(Animal):  # Você irá receber uma notificação de sua IDE de que precisa implementar os métodos abstratatos,
    # no caso o método falar

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala Olá Minie!')


# Testes -> vamos avaliar se conseguimos implementar os objetos

felix = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()  # NotImplementedError: A classe filha precisa implementar este método
