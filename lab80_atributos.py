"""
POO ->  Atributos representam as caracteristicas do objeto. Ou seja, pelos atributos nos conseguimos representar
        computacionalmente os estados de um objeto.

        Os Atributos em Python podem ser:
            - Atributos de instâncias
            - Atributos de classe
            - Atributos dinâmicos

        1- Atributos de instância: são atributos declarados dentro do método construtor.


    OBS.:   1- Método construtor -> é um método especial utilizado para a construção do objeto
            Em JAVA, uma classe lâmpada, inclusive seus atribuots ficaria mais ou menos assim:
                public class lampada(){
                    private int voltagem;
                    private String cor;
                    private Booleam ligada = false;

                    public lampada(int voltagem, String cor){
                        this.voltagem = voltagem;
                        this.cor = cor;
                    }

                    public int getVoltagem(){
                        return this.voltagem
                    }

                }
            2- Em PYTHON, uma classe lâmpada, inclusive seus atributos ficaria assim:
                class lampada:
                    def __init__(self, voltagem, cor):  # método construtor
                        self.__voltagem = voltagem  # Atributo de instância
                        self.__cor = cor  # Atributo de instância
                        self.__logada = False  # Atributo de instância
            3- Em PYTHON private do JAVA equivale a .__

    NOTA:   1- Se o atributo é "privado" só temps acesso a ele dentro da classe no qual foi definido!
            2- O que é o self? Simples self é na linguagem PYTHON um objeto que executa o método. Pense no self como
            um auto serviço, assim como você se serve em um restaurante self service.
            3- Podemos dizer que self por convenção da linguagem PYTHON é sempre o primeiro parâmetro de um método.
            4- Atributos podem ser públicos ou privados. Privados - são acessados apenas internamente à classe onde
            foi criado. Publicos - são acessados internamente e externamente à classe onde foi criado.
            5- Em PRYTHON ficou estabelecido que todo atributo de uma classe é PÚBLICO ou seja, pode ser acessado em
            todo projeto. Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja,
            que deve ser acessado/utilizado somente dentro da própria classe onde está declarado, utiliza-se
            __ duplo underscore no início de seu nome. Isso é conhecido também como Name Mangling.
                IMPORTANTE =>> isso é apenas uma convenção, ou seja, a linguagem PYTHON não vai impedir que façamos
                acesso aos atributos sinalizados como privados fora da classe.
            6- Atributo de INSTÂNCIA -> significa que ao criarmos instâncias (OBJETOS DA CLASSE) de uma classe,
            todas as instâncias terão esses ATRIBUTOS e ainda assim, serão diferentes.
            7- Atributo de CLASSE -> são os atributos que terão seus próprios valores de acordo com a instância
            criada, ou seja, cada instância terá seus próprios valores. São atributos declarados diretamente na
            classe, ou seja, fora do construtor. Geralmente já inicializamos um valor, e este valor é compartilhado
            entre todas as instâncias da classe. Ou seja, ao invés de cada instância da classe ter seus próprios
            valores como é o caso dos atributos de instância, com os atributos de classe todas as instâncias
            terão o mesmo valor para esse atributo.
                NOTA:   1- Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe
                        2- Em linguagens como JAVA, os atributos conhecidos como atributos de classe que em PYTHON
                        são chamados de atributos estáticos
            8- Atributos DINÂMICOS -> nada mais é do que um atributo de INSTÂNCIA que pode ser criado em tempo de
            execução.
                NOTA:   1- O atributo DINÂMICO será exclusivo da INSTÂNCIA que o criou
                        2- Embora bem trânquilo e possível em PYTHON seu uso não é COMUM

EXEMPLO Uma classe PYTHON explorando recursos avançados de POO

# Criando a classe lâmpada em PYTHON


class Lampada:

    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

# Vamos agora criar métodos para facilitar a utilização
    @property
    def voltagem(self):
        return self.__voltagem

    @property
    def cor(self):
        return self.__cor

    @property
    def ligada(self):
        return self.__ligada


"""


# Simplificando o início vamos refatorar para algo mais básico. Classes com atribuots de Intância Público


class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Exemplo ->> para executar o método __init__ (construtor da classe) basta usarmos o próprio nome da classe
# num processo de atribuição/criação de um objeto na verdade.
ps4 = Produto('playstation', 'ps4',
              2500.00)  # Produto() aqui é o construtor da classe Produto, na verdade é o método __init__ sendo executado


# Atributos de Instância -> Públicos e Atributos Privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email  # Note que este atributo foi declarado como PÚBLICO
        self.__senha = senha  # Note o __ antes do nome, siginificando que estamos com atributo PRIVADO

    def mostra_senha(self):
        return self.__senha

    def mostra_email(self):
        return self.email


# IMPORTANTE =>> isso é apenas uma convenção, ou seja, a linguagem PYTHON não vai impedir que façamos
# acesso aos atributos sinalizados como privados fora da classe.


user = Acesso('user@gmail.com', '123456')  # user é um objeto da classe Acesso
# Através do objeto criado, podemos ter acesso aos atributos e métodos da classe
print(f'testando acesso a atributos públicos -> {user.email}')
# print(f'testando acesso a atributos privado -> {user.__senha}')  # Teremos um erro ->> AttributeError: 'Acesso' object has no attribute '__senha'
# Mas, isso é apenas um aviso!!! Vamos explorar um pouco mais usando o dir()
print(f'{dir(user)}')
print(f'testando acesso a atributos privado -> {user._Acesso__senha}')  # Note que com dir() temos a dica de como
# resolver o problema 'objeto._Classe__atributo'. Enfim, temos acesso, mas não devemos usar este tipo de acesso.
# Isso que foi feito é o que recebe o nome de Name Mangling =>> _Classe__atributo

print(f'Acessando de forma correta um atributo privado -> {user.mostra_senha()}')
print(f'Acessando um atributo público através de um método -> {user.mostra_email()}')

# O que significa atributos de Instância?
# Significa, que ao criarmos instâncias/objetos de uma classe, todas as instâncias terão estes atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')
print(f'\n')
print(f'Acessando um atributo público através de um método -> {user1.mostra_email()}')
print(f'Acessando de forma correta um atributo privado -> {user1.mostra_senha()}')
print(f'Acessando um atributo público através de um método -> {user2.mostra_email()}')
print(f'Acessando de forma correta um atributo privado -> {user2.mostra_senha()}')
print(f'\n')


# Atributos de Classe ->> refatorando a classe Produto


class Produto:
    # Atributo de classe
    imposto = 1.05  # Atributo de Classe -> 0.05% de imposto
    contador = 0  # Atributo de Classe -> contador = 0

    # A lógica desse construtor faz com que sempre ao criar um objeto acrescente-se um ao seu contador

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1  # Atributo de INSTANCIA -> id
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto
        Produto.contador = self.id  # Cada objeto criado terá seu id acrescido de um -> oberve como se faz acesso
        # a um atributo de CLASSE


p1 = Produto('PlayStation 4', 'Video Game', 2500)
p2 = Produto('Xbox S', 'Video Game', 4500)

# Embora p1 e p2 sejam objetos diferentes, obseve quando pedimos para imprimir o imposto ->> acesso INCORRETO
print(f'Verificando imposto de p1 -> {p1.imposto}')  # p1 -> 1.05
print(f'Verificando imposto de p2 -> {p2.imposto}')  # p2 -> 1.05
print(f'\n')
# Observe agora quando tentamos acessar os valores de p1 e p2 -> Observe que o imposto já foi incorporado
print(f'Verificando valor de p1 -> {p1.valor}')  # p1 -> 2625.0
print(f'Verificando valor de p2 -> {p2.valor}')  # p2 -> 4725.0
print(f'\n')
# Observe que não precisamos criar uma instância para termos acesso a um ATRIBUTO DE CLASSE ->> acesso CORRETO
print(f'Verificando acesso ao atributo de classe -> {Produto.imposto}')  # Imposto = 1.05
print(f'\n')
# Vamos agora acessar o contador do objeto
print(f'Verificando contador p1 -> {p1.id}')  # p1 -> 1
print(f'Verificando contador p2 -> {p2.id}')  # p2 -> 2

# Vamos trabalhar com ATIBUTOS DINÂMICOS
print(f'\n')
p3 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo DINÂMICO em tempo de execução
p3.peso = '5kg'  # Note que na CLASSE Produto não existe o ATRIBUTO peso
print(f'Quem é p3? nome -> {p3.nome}, descrição -> {p3.descricao}, valor -> {p3.valor}, peso -> {p3.peso}')
# Para conferir a criação em tempo real do atributo, vamos conferir com o produto p1
# print(f'Quem é p1? nome -> {p1.nome}, descrição -> {p1.descricao}, valor -> {p1.valor}, peso -> {p1.peso}')
# Temos a mensagem de erro: AttributeError: 'Produto' object has no attribute 'peso'

# Deletando ATRIBUTOS -> observe o uso de __dict__ que devolve os atributos de instância, mas não os de classe
print(f'\n')
print(f'Dict de p1 -> {p1.__dict__}')
print(f'Dict de p3 -> {p3.__dict__}')
# Para conhecer todos os atributos da classe use
print(f'Dict para a classe Produtos -> {Produto.__dict__}')

# Deletando o atributo peso
del p3.peso
# Conferindo
print(f'\n')
print(f'Dict de p1 -> {p1.__dict__}')
print(f'Dict de p3 -> {p3.__dict__}')
# Deletando um atributo estático de forma dinâmico
del p3. valor
print(f'\n')
print(f'Dict de p3 -> {p3.__dict__}')
