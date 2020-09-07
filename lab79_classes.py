"""
POO -> Classes ->> nada mais são do que modelos dos objetos do mundo real sendo representados computacionalmente

        NOTAS:  1- Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas
                da casa/empresa. Existe o tipo lâmpada em Python???
                2- Não existe, mas podemos criar uma classe lâmpadas ->> com isso poderemos modelar um
                objeto do mundo real para o ambiente computacional
                3- Classes podem conter:
                    - Atributos -> representam as características do objeto. Ou seja, pelos atributos
                    conseguimos representar computacionalmente os estrados de um objeto. No caso da lâmpada
                    possivelmente iriámos querer saber se a lâmpada é 110 ou 220 volts, se ela é branca,
                    vermelha ou outra cor, qual é a sua luminosidade, etc.
                    - Métodos -> são funções que representam os comportamentos do objeto. Ou seja, as ações que
                    este objeto pode realizar no seu sistema. No caso da lâmpada, por exemplo, um comportamento
                    comum que muito provavelmente iríamos querer representar no nosso sistema é o de ligar e
                    desligar a memsa (automatizando o processo liga/desliga).
                4- Em Python, para definir uma classe utilizamos a palavra reservada class.
                5- Utilizamos a palavra "pass" em Python quando temos um bloco de código que ainda não está
                implementado.
                6- Quando inicializamos nossas classes em Python utilizamos por convenção o nome com inicial
                em maiúsculo. Se o nome for composto, utiliza-se as iniciais de ambas as palavras em maiúsculo
                todas juntas (CamelCase).
                7- Em computação não utilizamos: acentuação, caracteres especiais, espaços ou similares
                para nomes de classes, atributos, métodos, arquivos, diretórios ...
                8- Quando estamos planejando um software e definimos quais classes teremos que ter no sistema,
                chamamos estes objetos que serão mapeados para classes como entidade.
"""

# A classe Lâmpada, classe ContaCorrente, classe Produto e classe Usuario


class Lampada:
    pass


class ContaCorrente:
    pass


class Produto:
    pass


class Usuario:
    pass


lamp = Lampada()
print(f'Observe que acabamos de criar o tipo lâmpada -> {type(lamp)}')  # Tipo -> <class '__main__.Lampada'>


# Note que temos usado classes com certa frequência, veja o exemplo a seguir

valor = int('42')  # Note que int é um cast para uma string '42'
print(f'Vamos observar mais de perto -> {help(int)}')  # Dentre outras informações encontramos -> class int(object)
