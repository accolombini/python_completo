"""
Orientação a Objetos => conceitos Python é uma linhguagem multiparadgmas, aceitando os paradmas, estruturados,
                        orientado a objetos e o paradgma funcional
                        paradgma de programação é a forma/metodologia utilizada para pensar/desenvolver sistemas

                        Nosso foco é no paradgma orientado a objetos:
                            1- Neste paradma, busca-se formas para mapear objetos do mundo real para
                            modelos computacionais
                            2- A ideia é representar facilmente estes objetos por meio de usas características
                            e comportamentos
                            3- Para facilitar o processo, pense no seu problema e de como mapeá-lo e como
                            dar início à sua codificação. Principais componentes de POO
                                1- A Classe -> representa o modelo do objeto do mundo real sendo representado
                                computacionalmente
                                2- Atributos -> quando falamos em atributos estamos na verdade falando de
                                características do objeto. Uma classe pode ter nenhum ou vários atributos
                                3- Métodos -> quando falamos em métodos estamos falando de comportamento dos
                                objetos, em outras palavras, quais as ações que este objeto executa ou pode
                                executar. Entenda métodos como sendo funções, as mesmas funções estudadas até
                                aqui, quando definidas na classe recebem o nome de métodos
                                4- Construtor -> também é um método, mas se trata de um método especial -> trata-se
                                do método encarregado pela criação dos objetos a partir da nossa classe. O contrutor
                                possui o mesmo nome da classe (construtor padrão)
                                5- O Objeto -> todo elemento criado com base na nossa classe recebem o nome de
                                objeto ou instância

                    NOTA:   1- Quando criamos uma classe, estamos criando nossos próprios tipos de dados

"""
# Exemplos de tipos em Python

numero = 10  # Diz que número é tipo inteiro
print(f'Verificando tipos -> {numero} - seu tipo -> {type(numero)}')
num = 10.1   # Diz que num é do tipo inteiro
print(f'Verificando tipos -> {num} - seu tipo -> {type(num)}')
nome = 'Jabuticaba'  # Diz que nome é do tipo string
print(f'Verificando tipos -> {nome} - seu tipo -> {type(nome)}')

# Exemplos de tipos que podemos definir


class Produto:  # Diz que Produto é um tipo definido por essa classe
    pass


ps4 = Produto()  # Note que Produto() é o construtor da classe Produto. ps4 é um objeto dessa classe
# ps4 não tem valor, observe seu endereço de memória -> <__main__.Produto object at 0x00000214B88DD220>
print(f'Verificando tipos -> {ps4} - seu tipo -> {type(ps4)}')  # Seu tipo -> <class '__main__.Produto'>
