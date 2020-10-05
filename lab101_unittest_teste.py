"""
Note que o teste é um arquivo separado, pertence ao mesmo projeto, mas é um arquivo separado
"""

import unittest

# Observe que estamos importando os módulos que desejamos testar, os quais se encontram em lab101_atividades_teste_tdd

from lab101_atividades_teste_tdd import comer, dormir

# É boa prática de programação atribuir à classe de teste o mesmo nome da unidade a ser testada, no caso,
# estamos testando lab101_atividades_testes_tdd, daí o nome da classe ser AtividadesTesteTdd


class AtividadesTesteTdd(unittest.TestCase):

    def test_comer_saudavel(self):  # Observe que estamos seguindo a convenção de
        """Testando o retorno com comida saudável."""
        # nome chamando test_<nome_do_que_sta_sendo_testado>
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comer_gostosa(self):
        """Testando o retorno com comida gostosa."""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),  # Observe que aqui estamos trabalhando com argumentos nomeados
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    def test_dormir_pouco(self):
        """Testando o retorno dormindo pouco."""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas. :('
        )

    def test_dormir_muito(self):
        """Testando o retorno dormindo muito."""
        self.assertEqual(
            dormir(10),
            'Ptz! Dormi muito! Estou atrasado para o trabalho!'
        )


if __name__ == '__main__':
    unittest.main()
