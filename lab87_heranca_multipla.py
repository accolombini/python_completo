"""
POO - Herança Múltipla =>   enquanto JAVA, por exemplo, suporta herança de uma única classe, Python, por sua vez,
                            suporta herança proveniente de múltiplas classes. Logo, a classe filha, herdadra todos
                            os atributos e métodos de todas as classes herdadas
                            Em outras palavras, podemos dizer que herança multipla nada mais é do que a possibilidade
                            de uma classe herdar de múltiplas classes, fazendo com que a classe filha herde todos
                            os atributos e métodos de todas as classes herdadas. Detalhe, em PYTHON, não existe limite
                            para HERANÇA ...

                NOTA:   A herança múltipla pode ser feita de duas maneiras:
                        - Por Multiderivação Direta;
                        - Por Multiderivação Indireta;

                OBS.:   Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará
                        todos os atributos e métodos das super classes.
                        Importante, em heranças múltiplas, a ordem da herança altera o comportamento do objeto,
                        observe especificamente a classe Pinguim e o método cumprimentar.
                        Qualquer objeto em Python herda inicialmente de object -> não esqueça

# Entendendo heranças múltiplas. Primeiramente Multiderivação DIRETA


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass


# Entendendo heranças múltiplas. Multiderivação INDIRETA


class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerivada(Base3):
    pass

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


# Testando

baleia = Aquatico('Wally')
print(f'{baleia.nadar()}')
print(f'{baleia.cumprimentar()}')

print(f'\n')

tatu = Terrestre('Xim')
print(f'{tatu.andar()}')
print(f'{tatu.cumprimentar()}')

print(f'\n')

tux = Pinguim('Tux')
print(f'{tux.andar()}')
print(f'{tux.nadar()}')
print(f'{tux.cumprimentar()}')  # A execução aqui é uma questão de Method Resolution Order - MRO Foi executado
# neste caso Eu sou Tux da terra!. Este resultado ocorre quando a classe Pinguim(Terrestre, Aquatico). Observe
# o resultado quando inverto a classe Pinguim(Aquatico, Terrestre) temos como resultado -> Eu sou Tux do mar!

print(f'\n')

# Podemos por algum motivo querer saber se o Objeto sob análise é uma instância de ...

print(f'Tux é uma instância de Pinguim? {isinstance(tux, Pinguim)}')  # True
print(f'Tux é uma instância de Aquatico? {isinstance(tux, Aquatico)}')  # True
print(f'Tux é uma instância de Terrestre? {isinstance(tux, Terrestre)}')  # True
print(f'Tux é uma instância de Animal? {isinstance(tux, Animal)}')  # True
print(f'Tux é uma instância de Object? {isinstance(tux, object)}')  # True
