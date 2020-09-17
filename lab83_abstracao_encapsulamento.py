"""
POO - Abstração e Encapsulamento

    O grande objetivo da POO é encpsular nosso código dentro de um grupo lógico e hierárquico
    utiliando classes.

    Encapsular -> cápsula

        classe
-------------------------------
|                              |
|      atributos e métodos     |
|------------------------------|

    NOTA:   Atributos/Métodos privados em Python
            Imagine que temos uma classe chamada Pessoa, contendo um atributo privado chamado __nome
            e um método privado chamado __falar()

            Esses elementos privados -> atributos e métodos só devem/deveriam ser acessados dentro da classe.
            Mas Python não bloqueia este acesso fora da classe. Com Python acontece um fenômeno chamado
            Name Mangling, que faz uma alteração na forma de se acessar os elementos privados, conforme:

            ._Classe__elemento -> note um underline antes de classe e dois underlines antes do elemento sem o ponto

            EXEMPLO 1: acessando fora da classe o atributo nome (estando fora da classe acessando o atributo privado
            da classe)
            instancia._Pessoa__nome

            EXEMPLO 2: acessando fora da classe o método falar() (estando fora da classe acessando o método privado
            da classe)
            instancia._Pessoa__falar()

        ABSTRAÇÃO:  em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
        privados de usuário

    Exemplo 1 -> trabalhando com atributos públicos

    class Conta:

    contador = 400  # esse é um atributo de classe

    def __init__(self, titular, saldo, limite):  # Construtor da classe
        # Atributos de instâncias públicos
        self.numero = Conta.contador  # note que estamos trabalhando com atributos públicos (não se usa undeline após self)
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


# Testando a classe

conta1 = Conta('Pedro', 150.00, 1500)
# Note que o fato dos atributos serem públicos facilita muito o acesso, mas isso, nem sempre é possível ou recomendado
print(f'O número da conta -> {conta1.numero}\nSeu titular -> {conta1.titular}\nO saldo atual -> {conta1.saldo}'
      f'\nO limite da conta é -> {conta1.limite}')

# Para que fique claro o problema de se deixar público os atributos, veja o que podemos fazer facilmente

conta1.numero = 33
conta1.titular = 'Zezinho'
conta1.saldo = 999999999.00
conta1.limite = 999999999999.00

print(f'\n')
# Vamos ver o que temos ...Nada mal heim olha que festa ...
print(f'O número da conta -> {conta1.numero}\nSeu titular -> {conta1.titular}\nO saldo atual -> {conta1.saldo}'
      f'\nO limite da conta é -> {conta1.limite}')

print(f'\n')
# Podemos também imprimir diretamente como segue
# Este é um problema clássico de falta de encapsulamente, note que a segurança do sistema foi totalmente comprometida
print(f'Conta diretamente -> {conta1.__dict__}')  # dictionary for instance variables (if defined)
print(f'\n')
conta1.extrato()

        Exemplo 2 - Trabalhando com Atributos privados

        class Conta:

    contador = 400  # esse é um atributo de classe

    def __init__(self, titular, saldo, limite):  # Construtor da classe
        # Atributos de instâncias públicos
        self.__numero = Conta.contador  # Atributos privados (note o uso do undeline após self)
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Extrato -> Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor


# Testando a classe
conta1 = Conta('Pedro', 150.00, 1500)
# Note que o fato dos atributos serem públicos facilita muito o acesso, mas isso, nem sempre é possível ou recomendado
# Observe que nesse caso, estamos tentando acesso a conta externanmente, veja a mensagem de erro!
# print(f'O número da conta -> {conta1.numero}\nSeu titular -> {conta1.titular}\nO saldo atual -> {conta1.saldo}'
#      f'\nO limite da conta é -> {conta1.limite}')  # AttributeError: 'Conta' object has no attribute 'numero'

# Observe que nossa conta esta protegida ...

        # ATENÇAO -> embora aparentemente tenhamos solucionado o problema, LEMBRE-SE que a linguagem Python não bloqueia
# o acesso à essas informações --> Lembra do Name Manglin?

# Note que nesse acesso indevido o pep8 nos avisa, não faça isso, mas ...
print(f'Acesso indevido, mas possível ->> {conta1._Conta__titular}\n')

conta1._Conta__numero = 25
conta1._Conta__titular = 'Felicidade'
conta1._Conta__saldo = 999999999999.00
conta1._Conta__limite = 999999999999999999.00

conta1.extrato()
print(f'Conta atualizada -> {conta1.__dict__}')

# ATENÇÃO ->> Em Python fazer uso correto dos acessos e permissões do sistema está nas mãos do DESENVOLVEDOR!

        Exemplo 3 Atributos privados e métodos refatorados

        # Para resolver esse problema vamos refatorar nossa classe Conta tornando os atributos privados


class Conta:

    contador = 400  # esse é um atributo de classe

    def __init__(self, titular, saldo, limite):  # Construtor da classe
        # Atributos de instâncias públicos
        self.__numero = Conta.contador  # Atributos privados (note o uso do undeline após self)
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    # Após refatorar o que temos nesta classe são atributos privados e métodos públicos - observe
    def extrato(self):
        print(f'Extrato -> Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):  # Refatorando para bloquear depósitos negativos
        if valor > 0:
            self.__saldo += valor
        else:
            print(f'O valor precisa ser positivo')

    def sacar(self, valor):  # Refatorando para bloquear saques além do limite
        if valor > 0:
            if (self.__saldo + self.__limite) >= valor:
                self.__saldo -= valor
            else:
                print(f'Saldo insuficiente para o saque desejado!')
        else:
            print(f'O valor do saque precisa ser positivo > 0')


# Testando a classe
conta1 = Conta('Pedro', 150.00, 1500)
# Note que o fato dos atributos serem públicos facilita muito o acesso, mas isso, nem sempre é possível ou recomendado
# Observe que nesse caso, estamos tentando acesso a conta externanmente, veja a mensagem de erro!
# print(f'O número da conta -> {conta1.numero}\nSeu titular -> {conta1.titular}\nO saldo atual -> {conta1.saldo}'
#      f'\nO limite da conta é -> {conta1.limite}')  # AttributeError: 'Conta' object has no attribute 'numero'

# Observe que nossa conta esta protegida ...

print(f'Dados da conta -> {conta1.__dict__}')
conta1.extrato()  # Extrato -> Saldo de 150.0 do titular Pedro com limite de 1500

# Testando os métodos

conta1.depositar(-150)  # Note que estamos fazendo um depósito negativo ->> a rigor isso não é possível
conta1.depositar(150)  # Depois de refatorar o método vamos conferir novamente
conta1.extrato()  # Extrato -> Saldo de 0.0 do titular Pedro com limite de 1500
# Ou lembre-se podemos sempre usar
print(f'Usando dicionário -> {conta1.__dict__}')

# Método sacar()

conta1.sacar(200)
print(f'\nUsando dicionário depois de sacar(200) -> {conta1.__dict__}')  # {'_Conta__numero': 400, '_Conta__titular': 'Pedro', '_Conta__saldo': 100.0, '_Conta__limite': 1500}

# Mas se eu sacar mais do que tenho em limite será que posso?

# conta1.sacar(2000)
# print(f'\nUsando dicionário depois de sacar(2000)-> {conta1.__dict__}')  # {'_Conta__numero': 400, '_Conta__titular': # 'Pedro', '_Conta__saldo': -1900.0, '_Conta__limite': 1500}

# Vamos refatorar o método sacar() para melhorar um pouco isso
conta1.sacar(2000)  # Saldo insuficiente para o saque desejado!
print(f'Status da conta -> {conta1.__dict__}')

# Mas será que o sistema da forma como está nos permite fazer um saque negativo?

conta1.sacar(-200)
print(f'Status da conta depois do saque negativo -> {conta1.__dict__}')

        Exemplo 4 ->> Transferindo valores entre contas diferentes
        # Para resolver esse problema vamos refatorar nossa classe Conta tornando os atributos privados


class Conta:

    contador = 400  # esse é um atributo de classe

    def __init__(self, titular, saldo, limite):  # Construtor da classe
        # Atributos de instâncias públicos
        self.__numero = Conta.contador  # Atributos privados (note o uso do undeline após self)
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    # Após refatorar o que temos nesta classe são atributos privados e métodos públicos - observe
    def extrato(self):
        print(f'Extrato -> Conta de {self.__titular} seu saldo é {self.__saldo}  seu limite é {self.__limite}')

    def depositar(self, valor):  # Refatorando para bloquear depósitos negativos
        if valor > 0:
            self.__saldo += valor
        else:
            print(f'O valor precisa ser positivo')

    def sacar(self, valor):  # Refatorando para bloquear saques além do limite
        if valor > 0:
            if (self.__saldo + self.__limite) >= valor:
                self.__saldo -= valor
            else:
                print(f'Saldo insuficiente para o saque desejado!')
        else:
            print(f'O valor do saque precisa ser positivo > 0')


# Testando a classe com mais de uma conta

conta1 = Conta('Pedro', 150.00, 1500)
conta1.extrato()
conta2 = Conta('Julia', 300, 2000)
conta2.extrato()

# Transferindo valores entre contas ->> observe como o processo está manual:

valor = 100
conta2.sacar(valor)
conta1.depositar(valor)

conta1.extrato()
conta2.extrato()

"""

# Para resolver o problema vamos precisar refatorar mais uma vez a classe


class Conta:

    contador = 400  # esse é um atributo de classe

    def __init__(self, titular, saldo, limite):  # Construtor da classe
        # Atributos de instâncias públicos
        self.__numero = Conta.contador  # Atributos privados (note o uso do undeline após self)
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    # Após refatorar o que temos nesta classe são atributos privados e métodos públicos - observe
    def extrato(self):
        print(f'Extrato -> Conta de {self.__titular} seu saldo é {self.__saldo}  seu limite é {self.__limite}')

    def depositar(self, valor):  # Refatorando para bloquear depósitos negativos
        if valor > 0:
            self.__saldo += valor
        else:
            print(f'O valor precisa ser positivo')

    def sacar(self, valor):  # Refatorando para bloquear saques além do limite
        if valor > 0:
            if (self.__saldo + self.__limite) >= valor:
                self.__saldo -= valor
            else:
                print(f'Saldo insuficiente para o saque desejado!')
        else:
            print(f'O valor do saque precisa ser positivo > 0')

    def transferir(self, valor, conta_destino):
        # 1 passo Remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10  # Taxa de transferência paga por quem realizou a transferência

        # 2 adicionar o valor na conta de destino
        conta_destino.__saldo += valor


# Testando a classe com mais de uma conta

conta1 = Conta('Pedro', 150.00, 1500)
conta1.extrato()
conta2 = Conta('Julia', 300, 2000)
conta2.extrato()

# Transferindo valores entre contas ->> observe como o processo está manual:

conta2.transferir(100, conta1)
conta1.extrato()
conta2.extrato()
