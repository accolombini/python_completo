"""
Introdução ao módulo Unittest ->  testes unitários que são formas de testar unidades individuais de código fonte

        Unidades individuais podem ser:
            - funções
            - métodos
            - classes
            - módulos, etc

        OBS.:   - quando se fala em teste unitário, não estmaos falando especificamente da Linguagem Python.
                - estamos falando da qualidade do software, que é independente da linguagem e da plataforma
                - para criar nossos testes, criamos classes que herdam de unittest.TestCase e a partir de então
                ganhamos todos os 'assertions' presentes  no módulo.
                - para executarmos os testes, utilizamos unittest.main()
                - TestCase -> casos de teste para sua unidade aplicação
                - Para conhecer mais sobre as unittest consulte:
                https://docs.python.org/3/library/unittest.html?highlight=unittest#module-unittest
                - Consulte especificamente a tabela que discute os TestCase e os métodos assert
                - Por convenção todos os testes realizados em um test case, devem ter seu nome iniciado com test_
                - Para executar os testes com unittest -> python nome_do_modulo.py
                - Para executar os testes com unittest no modo verbose (todos os detalhes) -> python nome_do_modulo -v
                - Docstrings nos testes -> podemos acrescentar (e é recomendado) docstrings nos nossos testes.

        Conhecendo as assertions - confira na tabela

        Método                                      Checa que
        assertEqual(a, b)                           a == b
        assertNotEqual(a, b)                        a != b
        assertTrue(x)                               x é verdadeiro
        assertFalse(x)                              x é falso
        assertIs(a, b)                              a é b
        assertIsNot(a, b)                           a não é b
        assertIsIfNone(x)                           x é None
        assertIsNotNone(x)                          x não é None
        assertIn(a, b)                              a está em b
        assertNotIn(a, b)                           a não está em b
        assertIsInstance(a, b)                      a é instância de b
        assertNotIsInstance(a, b)                   a não é instância de b


"""

# Vamos praticar usando a abordagem TDD
