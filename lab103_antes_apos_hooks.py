"""
Unittest -> antes e após hooks =>> hooks são os testes em si, em outras palavras, a execução dos testes

            - Quando falamos antes e após o hooks, na verdade estamos dizendo que devemos realizar algo
            antes e após os testes (hooks)

            - Para realizar estas ações, o Unittest possui dois métodos para isso, são eles:
            - setUp() -> é executado antes de cada método de teste. É útil para criarmos instâncias de objetos
            e outros dados
            - tearDown() -> é executado ao final de cada método de teste. É útil para excluir dados ou fechar
            conexões com banco de dados

"""
import unittest


class ModuloTest(unittest.TestCare):

    def setUp(self):
        # Configurações do setUp()
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar após o teste
        pass

    def test_segundo(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar após o teste
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass
