"""
POO -> Métodos Mágicos => métodos mágicos são todos os métodos que utilizam dunder.

    Conhecemos: dunder init -> __init__( )  (nosso construtor)
                dunder vem de double underline ou underscore
                dunder repr -> __repr__ -> representação do objeto
                dunder len -> __len__  -> retorna um número inteiro conforme o que foi definido pelo programador
                dunder del -> __del__ -> permite que controle a saída do método del
                dunder add -> __add__ -> permite que se crie um método para concatenar objetos de uma instância

    Exemplo:

        def __del__(self):  # Note que esse método estará sobrescrevendo o método del do sistema adicionando
        # um corportamento mais amigável
        print(f'Um objeto do tipo livro foi deletado da memória')
"""


# Exemplo conhecendo alguns dunders interessantes


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):  # este método retorna a representação __repr__ do objeto => sobrescreve na classe object
        return f'{self.titulo} escrito por {self.autor}'

    def __str__(self):  # este método retorna uma representação do objeto para o usuário final -> __str__. Faz a
        # mesma coisa que __repr__. Mas atenção se ambos estiverem presentes no seu código, será executado o __str__
        return self.titulo

    def __len__(self):  # este método retorna o número de paginas, no caso o tamanho do livro em questão -> __len__.
        # Mas atenção, é você programador que define a aplicação de __len__, por exemplo, poderia estar
        # retornando o tamanho do título
        return self.paginas

    def __add__(self, outro):  # Concatena objetos diferentes da mesma instância
        return f'{self} - {outro}'

    def __mul__(self, other):  # Permite multiplicar um objeto por outro, desde que, outro seja do tipo int
        if isinstance(other, int):
            msg = ' '  # Será um contador que permitirá concatenar um número de vezes definido por other
            for n in range(other):  # Aqui é onde estamos definindo como concatenar nosso objeto
                msg += ' ' + str(self)
            return msg
        return f'Não posso multiplicar'


livro1 = Livro('Python Rocks!', 'Leandro Medeiros', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Amaro Silva', 760)

print(f'O livro1 é -> {livro1}')  # <__main__.Livro object at 0x0000013AA461E220>
print(f'O livro2 é -> {livro2}')  # <__main__.Livro object at 0x0000013AA461E430>

print(f'O livro1 após a crição do método __repr__ -> {livro1}')  # Python Rocks! escrito por Leandro Medeiros
print(f'O livro2 após a crição do método __repr__ -> {livro2}')  # Inteligência Artificial com Python escrito
# por Amaro Silva

# del livro1

print(f'O número de páginas do livro1 é -> {len(livro1)} páginas!')  # O número de páginas do livro1 é -> 400 páginas!
print(f'O número de páginas do livro2 é -> {len(livro2)} páginas!')  # O número de páginas do livro2 é -> 760 páginas!

print(f'Concatene livro1 com livro2 -> {livro1 + livro2}')
print(f'Testando concatenar -> {livro1 * 3}')
