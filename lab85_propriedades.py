"""
POO => Propriedades - Properties

    NOTA:   Em lingugens de programação como o JAVA, ao declararmos atributos privados nas classes, costumamos criar
            métodos públicos para manipulação desses atributos. Esses métodos são conhecidos por getters e setters, onde
            os getters retornam o valor do atributo e os setters alteram o valor do mesmo.
            É importante avaliar a importância do setters, pois seu uso implica em alterar os atributos, o que nem
            sempre é interessante, portanto, use apenas em casos que realmente seu uso se torne necessário.


Exemplo inicial -> gerando a necessidade

class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador +=1

    def extrato(self):
        return f'Saldo de {self.__saldo} do/a Cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def trasferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

# Para os testes iniciais


conta1 = Conta('Manoela', 3000, 5000)
conta2 = Conta('Jussara', 2000, 4000)

print(f'O extrato de conta1 -> {conta1.extrato()}')
print(f'O extrato de conta2 -> {conta2.extrato()}')

# Nunca faça isso acessar elementos privados da Classe externamente -> só para fins didáticos

soma = conta1._Conta__saldo + conta2._Conta__saldo
print(f'A soma do saldo das contas registradas é -> {soma}')


Exemplo -> Forma JAVA

# A melhor forma para resolver esse problema é criando métodos chamados getters e setters
# Vamos refatorar nossa classe usando get e set, acompanhe
# Isto é o forma JAVA de resolver o problema e não a forma Pythônica


class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador +=1

    def extrato(self):
        return f'Saldo de {self.__saldo} do/a Cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def trasferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    # Criação dos métodos Get e Set
    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


# Para os testes iniciais


conta1 = Conta('Manoela', 3000, 5000)
conta2 = Conta('Jussara', 2000, 4000)

print(f'O extrato de conta1 -> {conta1.extrato()}')
print(f'O extrato de conta2 -> {conta2.extrato()}')

# Nunca faça isso acessar elementos privados da Classe externamente -> só para fins didáticos

soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma do saldo das contas registradas é -> {soma}')

# Vamos testar o uso do set alterando o limite de conta1

print(f'O limite atual de conta1 -> {conta1.get_limite()}')

conta1.set_limite(10000)

print(f'O limite atual de conta1 -> {conta1.get_limite()}')

"""


# Refatorando nossas classes utilizando o conceito de Propriedades =>> Método Pythônico


class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador +=1

        # Vamos agora criar as propriedades, para isso usaremos um decorator @properties

    # O decorator @property equivale de forma melhorada ao get do JAVA
    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    # O decorator @limite.setter equivale de forma melhorada ao set do JAVA => Note que você o usa no decorator
    # o mesmo nome do atributo => no caso deste exemplo, limite
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    # Métodos privados

    def extrato(self):
        return f'Saldo de {self.__saldo} do/a Cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def trasferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    # Um outro uso interessante de propriedades é quando criamos um método que não reporta a um atributo específico.
    # No caso observe que não existe um atributo valor total, mas podemos criar um metodo que retorne o valor
    # total -> saldo + limite de cada conta

    @property
    def valor_total(self):
        return self.__saldo + self.__limite

# Para os testes iniciais


conta1 = Conta('Manoela', 3000, 5000)
conta2 = Conta('Jussara', 2000, 4000)

print(f'O extrato de conta1 -> {conta1.extrato()}')
print(f'O extrato de conta2 -> {conta2.extrato()}')

# Usando propriedades @decorator

soma = conta1.saldo + conta2.saldo  # Observe que o uso da propriedade nos permite acesso sem o uso de parênteses
print(f'A soma do saldo das contas registradas é -> {soma}')

# Usando propriedades @nome_atributo_setter

print(f'Daddos da conta1 -> {conta1.__dict__}')

# Alterando o limite

conta1.limite = 10000  # Observe que estamos usando a propriedade e não o método e esta propriedade
# funcionará como um setter
print(f'O novo saldo de conta1 é -> {conta1.limite}')

# Consultando saldo total de cada conta usando @property
print(f'Valor total de conta1 -> {conta1.valor_total}')  # Observe o poder do uso do @property
print(f'Valor total de conta2 -> {conta2.valor_total}')
