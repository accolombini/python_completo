"""
Escrevendo Iterador Customizado => o desafio será criar um iterator parecio com o range()

        Para relembrar -> no range(0, 10) o último elemento não é contabilizado temos algo como (0, 10]
        Nosso iterator -> Contador(0, 10) o último elemento será contabilizado temos algo como (0, 10)

        NOTA:   para criar um iterator ustomizado você sempre precisará de ao menos dois métodos, são eles:
                    def __iter__(self):  será -> nosso iter()
                    return self
                    def __next__(self):   será -> nosso next()

"""

# Escrevendo um iterator customizado


class Contador:  # Note que sempre que tivermos um método dentro da classe teremos que iniciar o construtor com selt
    def __init__(self, menor, maior):  # Construtor -> cria os objetos
        self.menor = menor
        self.maior = maior

    def __iter__(self):  # Este método é necessário para converter nosso objeto para um iterator -> nosso iter()
        return self

    def __next__(self):  # Este métoo é necessário para percorrer nosso iterável -> nosso next()
        if self.menor <= self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        raise StopIteration


con = Contador(1, 5)

print(f'Imprimindo nosso iterator -> {con} - seu tipo é -> {type(con)}')  # observe o tipo <class '__main__.Contador'>

print(f'Imprimindo nosso iterator -> {next(con)}')  # Tipo <class 'int'>
print(f'Imprimindo nosso iterator -> {next(con)}')
print(f'Imprimindo nosso iterator -> {next(con)}')
print(f'Imprimindo nosso iterator -> {next(con)}')
print(f'Imprimindo nosso iterator -> {next(con)}')
# print(f'Imprimindo nosso iterator -> {next(con)}')  # Se exceder o limite teremos a mensagem ->> StopIteration

print(f' \nNosso Contador -> iterator')
for n in Contador(1, 50):
    print(f'Testando nosso iterator -> {n}')
print(f' \nUsando range()')
for n in range(1, 51):
    print(f'Testando nosso iterator -> {n}')
