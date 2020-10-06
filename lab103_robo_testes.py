"""
# Motivando -> observe os teste antes de serem rafatorados -> note a repetição dos códigos

class RoboTestes(unittest.TestCase):

    def test_carregar(self):
        megaman = Robo('Mega Man', bateria=50)
        megaman.carregar()
        self.assertEqual(megaman.bateria, 100)

    def test_dizer_nome(self):
        megaman = Robo('Mega Man', bateria=50)
        self.assertEqual(megaman.dizer_nome(), 'BEEP BOOP BEEP BOOP. Eu sou MEGA MAN')
        self.assertEqual(megaman.bateria, 49, 'A bateria deveria estar em 49%')


"""

import unittest
from lab103_robo import Robo

# Refatorando utilizando setUp() e tearDown(). Note que o serUp() cria um objeto e o deixa
# disponível para todos os métodos


class RoboTestes(unittest.TestCase):

    def setUp(self):
        self.megaman = Robo('Mega Man', bateria=50)
        print(f'setUp() sendo executado ...')

    def test_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(self.megaman.dizer_nome(), 'BEEP BOOP BEEP BOOP. Eu sou MEGA MAN')
        self.assertEqual(self.megaman.bateria, 49, 'A bateria deveria estar em 49%')

    def tearDown(self):
        print(f'tearDown() sendo executado ...')


if __name__ == '__main__':
    unittest.main()
