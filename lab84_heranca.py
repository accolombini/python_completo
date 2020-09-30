"""
POO - HERANÇA (Inheritance) => a ideia de herança é a de reaproveitar código e na extensão de classes.

    OBS.:   com a herança, a partir de uma classe existente, nós extendemos outra classe que passa a herdar
            atributos e métodos da classe herdada.

    PENSE:  considere um sistema bancário, podemos ter duas entidades com seus respectivos atributos -> observe

        CLIENTE:
            - nome;
            - sobrenome;
            - cpf;
            - renda;

        FUNCIONARIO:
            - nome;
            - sobrenome;
            - cpf;
            - matricula;

    NOTA:   observe que em ambas as classes vocês possuem atributos que se repetem e ao aolhar para a classe podemos
            observar que ambas possuem o método nome_completo que faz exatamente a mesma coisa. Isso não lhe parece
            um desperdício de código?

    PERGUNTA:   sempre que estiver diante de uma situação como essa você deverá fazer a seguinte pergunta.
                EXISTE ALGUMA ENTIDADE GENÉRICA O BASTANTE PARA ENCAPSULAR OS ATRIBUTOS E MÉTODOS COMUNS A TODAS
                AS ENTIDADES?

Entendendo o problema:

class Cliente:
    def __init__(self, nome, sobrenome, cpf, renda):  # Observe que estamos trabalhando com atributos privados
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    IMPORTANTE: quando uma classe herda de outra classe ela herda TODOS os atributos e métodos da classe herdada
                quando herdamos devemos utilizar o construtor da classe herdada
                Quando uma classe herda de outra classe, a classe herdada, que no nosso caso, a classe
                herdada é a classe =>> Pessoa -> que recebe as seguintes denominações:
                    - Super Classe;
                    - Classe Mãe;
                    - Classe Pai;
                    - Classe Base;
                    - Classe Genérica;

                Quando uma classe herda de outra classe, que no nosso caso, são as classes Cliente e Funcionario
                elas recebem as seguintes denominações:
                    - Sub Classe;
                    - Classe Filha;
                    - Classe Específica;

# Problema refatorado e corrigido

# Dado que temos que entendemos o problema, vamos refatorar nosso código

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):  # Observe que estamos trabalhando com atributos privados
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):  # Aqui acontece a HERANÇA estamos dizendo que Cliente é do tipo PESSOA
    # Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)  # super é o modo que fazemos acesso ao construtor da Super Classe.
        # Isso equivale a dizer que super().__init__ é na verdade a Super Classe sendo executada no
        # escopo da Classe Filha
        # Pessoa.__init__(self, nome, sobrenome, cpf)  # É outra forma de acessar a Super Classe,
        # mas seu uso não deve ser encorajado!
        self.__renda = renda


class Funcionario(Pessoa):
    # Funcionario herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Está é a foram recoendada para acessar a Super Classe
        self.__matricula = matricula


# Testando as classes

cliente1 = Cliente('Amaro', 'Batista', '123.456.789-00', 5000)
funcionario1 = Funcionario('Marinalva', 'Conceição', '987.654.321-11', 1500)

print(f'O Cliente é -> {cliente1.nome_completo()}')
print(f'O funcionario é -> {funcionario1.nome_completo()}')

# Vamos observar o dicionário de cada uma das classes
# Observe que é feita uma separação para nós, sabe-se exatamente a que classe pertence cada atributo
print(cliente1.__dict__)  # {'_Pessoa__nome': 'Amaro', '_Pessoa__sobrenome': 'Batista',
# '_Pessoa__cpf': '123.456.789-00', '_Cliente__renda': 5000}
print(funcionario1.__dict__)  # {'_Pessoa__nome': 'Marinalva', '_Pessoa__sobrenome': 'Conceição',
# '_Pessoa__cpf': '987.654.321-11', '_Funcionario__matricula': 1500}

        SOBRESCRITA DE MÉTODO:  ocorre quando reescrevemos/reimplementamos um método presente na Super Classe
                                em classes filhas.
"""

# Vamos agora tratar de um problema chamado Sobrescrita de Métodos (Overriding)


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):  # Observe que estamos trabalhando com atributos privados
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):  # Aqui acontece a HERANÇA estamos dizendo que Cliente é do tipo PESSOA
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)  # super é o modo que fazemos acesso ao construtor da Super Classe.
        # Isso equivale a dizer que super().__init__ é na verdade a Super Classe sendo executada no
        # escopo da Classe Filha
        # Pessoa.__init__(self, nome, sobrenome, cpf)  # É outra forma de acessar a Super Classe,
        # mas seu uso não deve ser encorajado!
        self.__renda = renda


class Funcionario(Pessoa):
    """ Funcionario herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Está é a foram recoendada para acessar a Super Classe
        self._Pessoa__sobrenome = nome  # Só para evitar que o PyCharm reclame, a rigor não é necessário
        self._Pessoa__nome = sobrenome  # Só para evitar que o PyCharm reclame, a rigor não é necessário
        self.__matricula = matricula

    def nome_completo(self):  # Método Overriding (Sobrescreve o método nome_completo de Pessoa)
        print(f'Acessando Pessoa dentro do método Overriding {super().nome_completo()}')
        print(f'Acessando cpf, note que Funcionário herda de Pessoa {self._Pessoa__cpf}')
        return f'{self._Pessoa__nome} {self._Pessoa__sobrenome} - Matrícula: {self.__matricula}'

# Testando as classes


cliente1 = Cliente('Amaro', 'Batista', '123.456.789-00', 5000)
funcionario1 = Funcionario('Marinalva', 'Conceição', '987.654.321-11', 1234)

print(f'Cliente: -> {cliente1.nome_completo()}')
print(f'Funcionario: -> {funcionario1.nome_completo()}')
