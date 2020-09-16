"""
POO - Objetos =>    objetos são instâncias da classe. Ou seja, após o mapeamento do objeto do mundo real
                    para sua representação computacional, devemos poder criar quantos objetos forem necessários.
                    Podemos pensar nos objetos/instâncias de uma classe como variáveis do tipo definido na classe.

            NOTA:   Sempre que um objeto/intância for criada deve-se passar todos os parâmetros requeridos pelo
                    construtor da classe, caso contrário terá um erro do tipo: TypeError:
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente -> {self.__nome} diz oi')


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__Limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O Cliente é -> {self.__cliente._Cliente__nome}')  # Atenção em Cliente use um underline (atributo privado)
        print(f'O cpf do cliente é -> {self.__cliente._Cliente__cpf}')


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):

        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


# Instâncias/objetos
lamp1 = Lampada('branca', 110, 60)
print(f'O tipo de lamp1 é -> {type(lamp1)}\nA lâmpada lamp1 está ligada? {lamp1.checa_lampada()}')
# O tipo de lamp1 é -> <class '__main__.Lampada'>
# A lâmpada lamp1 está ligada? False
lamp1.ligar_desligar()
print(f'A lâmpada lamp1 está ligada? {lamp1.checa_lampada()}')  # A lâmpada lamp1 está ligada? True
# cc1 = ContaCorrente(5000, 20000)
# print(f'O tipo de cc1 é -> {type(cc1)}')  # O tipo de cc1 é -> <class '__main__.ContaCorrente'>
# user1 = Usuario('Silva', 'Hernani', 'silviah@gmail.com', '123456')
# print(f'O tipo de user1 é -> {type(user1)}')  # O tipo de user1 é -> <class '__main__.Usuario'>

# Simulando um erro por falta de parâmetros na definição do objeto
# lamp2 = Lampada()  # TypeError: __init__() missing 3 required positional arguments: 'cor', 'voltagem', and 'luminosidade'

cli1 = Cliente('Marcos Vale', '123.456.789-99')
cc = ContaCorrente(5000, 10000, cli1)  # Importante -> cli1 é um objeto da classe logo ele tema acesso aos
# atributos e métodos da classe
print(f'O tipo de cli1 é ->> {type(cli1)}')  # O tipo de cli1 é ->> <class '__main__.Cliente'>
cc.mostra_cliente()
# O Cliente é -> Marcos Vale
# O cpf do cliente é -> 123.456.789-99
# Fazendo acesso de forma errada só para fins didáticos
cc._ContaCorrente__cliente.diz()  # O cliente -> Marcos Vale diz oi
