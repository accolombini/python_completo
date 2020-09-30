"""
POO - O método super() ->> o método super() se refere à super classe.

    IMPORTANTE: o método super permite acesso a qualquer elemento da classe pai -> atributos/métodos
                não apenas ao construtor

"""

# Entendendo o método super()


class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} fala -> {som}')


class Gato(Animal):

    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie)  # Evite isso
        super().__init__(nome, especie)  # Esse é o formato Pythônico. Note que, ao usar super() você não uso o -> self
        # super().faz_som('auauauauauauau')  # Observe super acessando o método faz_som()
        self.__raca = raca


# Testando as classes

felix = Gato('Felix', 'Felino', 'Angorá')
felix.faz_som('miau')
