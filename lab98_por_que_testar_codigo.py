"""
Por que testar código => testamos para avaliar se o código funciona da forma que esperamos.

        - Estamos aqui falando de testes automatizados!
        - Quando criamos um sistema na verdade criamos mais de um
        - Testes acabam por ser um tema polêmico, pois nem todo desenvolvedor gosta de realizar testes
        - automatizados, pois estes exigem um grande carga de programação.

        Exemplo:
        ----------------------------------------------------------
        |              Uma Aplicação web envolve:                |
        ----------------------------------------------------------
        |  1-                    frontend                        |
        ----------------------------------------------------------
        |  2-                    backend                         |
        ----------------------------------------------------------
        |  3- testes automatizados para frontend e para backend  |
        ----------------------------------------------------------

        Testamos nosso código para:
            1- Reduzir bugs (problemas) no código existente
            2- Testes garantem que novos recursos da sua aplicação não quebren (alterem) recursos antigos
            3- Testes garantem que bugs (problemas) que foram corrigidos anteriormente continuem corrigidos
            4- Testes garantem que a refatoraçãl que costumamos fazer não tragam novos bugs (rpoblemas)

        A vertente de testes mais usada hoje é o TDD - Test Driven Development (Desenvolvimento Guiado por Testes)
            O interessante no TDD é que primeiramente você escreve seu teste, só aí você escreve seu código
            Com TDD você emprega os seguintes estágios:
                - Você escreve seu código primeiro
                - Então você escreve o código mínimo o suficiente para fazer o teste passar
                (ou seja, executar com sucesso)
                - Então refatora o código para realizar a funcionalidade e testa novamente
                - Uma vez que o teste passe, o recurso é considerado completo

            Estes estágios de desenvolvimento do TDD são quase que como um mantra que os desenvolvedores seguem,
            são conhecidos como:
                1- Red -> vai falhar
                2- Green -> código mínimo para passar
                3- Refactor -> ajustes no código para tratar de todas as funcionalidades do sistema

"""
# Alguns conceitos relevantes -> vamos praticando


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando!!!')


# Até aqui testamos nosso código dessa forma -> avaliamos os métodos e atributos simulando o uso do sistema

felix = Gato('Felix')
felix.miar()
print(f'O objeto felix chama-se -> {felix.nome}')
