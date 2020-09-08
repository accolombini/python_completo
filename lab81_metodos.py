"""
POO - Métodos => são funções que representam os comportamentos do objeto. Ou seja, as ações que este objeto pode
realizar no seu sistema

        Em PYTHON dividimos os métodos, em dois grupos: Métodos de instância e Métodos de Classe

            - Métodos de instância => são funções internas a uma Classe
            - O método dunder init __init__ => é um método especial chamado construtor e sua função
            é construir o objeto a partir da classe a ele associada.
                NOTA:   1- Todo elemento em PYTHON que inicia e finaliza com duplo underline é chamado de dunder
                        (Double Underline)
                        2- Os métodos/funções dunder em PYTHON são chamados de métodos MÁGICOS
                        3- Por mais que você enquanto programador possa cirar suas próprias funções utilizando dunder
                        (underline no início e underline no fim) essa prática não deve ser encorajada. PTYHTON
                        possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o comportamento
                        dessas funções mágicas existentes. ATENÇÃO não será ACUSADO ERRO ALGUM!!! CUIDADI!!!
                        4- Métodos devem ser escritos em letras minúsculas, caso tenha um nome composto, deverá
                        ser escrito em minúsuclo separado por underline
                        5- A senha gravada no banco de dados é justamente a senha criptografada ->> lembre-se
                        sempre disso
                        6- Métodos de instância acessam atributos de instância ->> uso do self

            - MÉTODOS DE CLASSE => não estão associados a nenhuma instância da classe, mas apenas a ela. Usa-se
            um decorator nestes métodos para sinalizar que se tratam de métodos de classe
                NOTA:   1- Métodos de classe não acessam atributos algum ->> uso do cls
                        2- Métodos de clsse em PYTHON são conhecidos como métodos estáticos em outras linguagens

            - MÉTODOS ESTÁTICOS => note que PYTHON além dos métodos de instância e de classe possuem os
            Métodos Estáticos ->> requer um decorador especial =>> @staticmethod
                NOTA:   1- Métodos Estáticos não têm acesso a classe e não têm acesso à instância

        EXEMPLO -> métodos de instância
        # Observe que da forma como está, conseguimos facilmente acesso a senha.
        # Para corrigir isso, vamos criptografa a senha usando um módulo de Python chamado passlib
        print(f'Teste com criptografia \n')
        nome = input('Infomre o nome: ')
        sobrenome = input('Informe o sobrenome: ')
        email = input('Informe o e-mail: ')
        senha = input('Informe a senha: ')
        confirma_senha = input('Confirme a senha: ')

        if senha == confirma_senha:
            user = Usuario(nome, sobrenome, email, senha)
        else:
            print(f'Senha não confere ...')
            exit(1)  # Código criado para finalizar o sistema quando a senha não conferir

        print(f'Retorno de cadastro correto -> {"Usuario criado com sucesso!"}')

        senha = input('Informe a senha para acesso: ')

        if user.checa_senha(senha):  # Note que user é interna ao bloco if, por isso, não é reconhecida ->> cuidado
            print(f'Acesso permitido!!')
        else:
            print(f'Acesso negado!!')

        # Vamos incorretamente fazer acesso a senha para verificar a criptografia
        print(f'Senha User Criptografada -> {user._Usuario__senha}')  # Acesso incorreto! uso didático apenas



"""
# Import do método para criptografia de senha

from passlib.hash import pbkdf2_sha256 as cryp


# Métodos de INSTÂNCIA -> note que estamos usando atributos Privados


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """
        Retorna o valor do produto com o desconto
        :param porcentagem:
        :return: Valor do produto com a porcentagem de desconto sugerida
        """
        return (self.__valor * (100 - porcentagem)) / 100

"""
class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        #    self.__senha = senha  # Sem criptografia
        #    rounds 200000 significa que estamos pedindo para fazer 200000 embaralhamentos para gerar a senha
        #    salt_size 16 significa que a senha terá um tamanho igual a 16 caracteres diferentes acrescidos
        #    quando encriptografada
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)  # Com criptografia

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        # Estamos usando um método do módulo cryo o verify para comparar a senha digitada com a senha gravada
        if cryp.verify(senha, self.__senha):
            return True
        return False

"""

p1 = Produto('PlayStation 4', 'Video Game', 2500)

# Vamos ver o valor do produto quando atribuímos 20% de desconto
print(f'O valor de p1 com desconto de 20% é -> {p1.desconto(20)}')
# Observe que desconto é um método de instância, assim, não o acessamos através da classe -> confira
# print(f'Tentando acesso a um método de instância através da classe -> {Produto.desconto(20)}')
# A mensagem de erro será TypeError: desconto() missing 1 required positional argument: 'porcentagem'
# Podemos resolver esse problema passando para desconto o objeto -> observe p1 é o próprio objeto (self)
print(f'Tentando acesso a um método de instância através de um objeto da classe -> {Produto.desconto(p1, 20)}')

print(f'\n')
# user1 = Usuario('Americo', 'Francisco', 'americo@gmail.com', '1234')
# user2 = Usuario('Ferdinando', 'Silva', 'ferdinando@gmail.com', '4321')

# Acessando o método nome_completo
# print(f'Nome completo de user1 -> {user1.nome_completo()}')
# print(f'Nome completo de user2 -> {user2.nome_completo()}')
# Note que podemos entender user1 ou user2 como sendo self -> observe
# print(f'Usando user1 como self -> {Usuario.nome_completo(user1)}')

# Agora vamos acessar de forma errada um atributo de classe -> lembra não devemos fazer isso
# print(f'Senha User1: {user1._Usuario__senha}')
# print(f'Senha User2: {user2._Usuario__senha}')

# Vamos agora trabalhar com MÉTODOS DE CLASSE

# Para bem entender Métodos de Classe, vamos refatorar a classe Usuario


class Usuario:

    contador = 0  # Atributo de classe

    @classmethod    # Decorator para Método de Classe
    def conta_usuarios(cls):  # cls -> é a própria Classe no caso equivale a Usuario
        print(f'Quem é cls -> {cls}')  # Confirmamos que cls é a própria classe -> <class '__main__.Usuario'>
        print(f'Temos -> {cls.contador} usuário(s) no sistema')

    @classmethod
    def ver(cls):
        print(f'Não acessa nenhum atributo -> por isso foi redefinido como método de classe')

    @staticmethod
    def definicao():
        return 'ABCXTAL'

    def __init__(self, nome, sobrenome, email, senha):  # Construtor
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        #    self.__senha = senha  # Sem criptografia
        #    rounds 200000 significa que estamos pedindo para fazer 200000 embaralhamentos para gerar a senha
        #    salt_size 16 significa que a senha terá um tamanho igual a 16 caracteres diferentes acrescidos
        #    quando encriptografada
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)  # Com criptografia
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario}')

    def nome_completo(self):  # Método público
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):  # Método público
        # Estamos usando um método do módulo cryo o verify para comparar a senha digitada com a senha gravada
        if cryp.verify(senha, self.__senha):
            return True
        return False

    @property  # Decorator para Método Privado
    def __gera_usuario(self):  # Método privado
        return self.__email.split('@')[0]


# Testando métodos de classe
print(f'Testando Métodos de Classe\n')
user = Usuario('Maria', 'Silva', 'msilva@gmail.com', '123456')
Usuario.conta_usuarios()  # Forma correta de acesso -> forma correta classe ->> acessa método de classe
user.conta_usuarios()  # Forma incorreta, mas possível ->> evite

print(f'Teste do método privado! \n')
user = Usuario('Francisco', 'Martinho', 'francisco@gmail.com', '123456')
# print(f'Gerando um erro ao tentar acesso a um método privado -> {user.__gera_usuario()}')
# A mensagem de erro -> AttributeError: 'Usuario' object has no attribute '__gera_usuario'
print(f'Acessando de forma incorreta Name Mangling -> {user._Usuario__gera_usuario}')
print(f'Método Estático -> {Usuario.contador}')
print(f'Método Estático -> {Usuario.definicao()}')
user2 = Usuario('Amalia', 'Junqueira', 'amalia@gmail.com', '123456')
print(f'Usuário número 2 -> {user2.contador}')
print(f'Usuário número 2 -> {user2.definicao()}')
