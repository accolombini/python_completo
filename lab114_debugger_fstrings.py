"""
Debugger mais simples com o uso de fstrings -> podemos facilmente debugar valores,
            bastando adicionar o sinal de igual
            Nota:   - basta usar a variável com um sinal de = -> print(f'{variavel=}")
                    - Você poderá usar esse recurso para testar seu código com muito mais recurso e propriedade

"""

# Debugger mais simples com fstrings

# def multiplicar(num1: float, num2: float) -> float:
#     return num1 * num2
#
# resultado: float = multiplicar(4.2345, 6.7890)
#
# print(f'O valor de resultado é -> {round(resultado, 2)}')
#
# print(f'O resultado diretamente pode ser obtido -> {multiplicar(9, 4):.4f}')
#
# # Observe que como estamos manipulando a variável media em um único print()
# print(f'Observe o uso do walrus -> {(media := 8 / 2)} é a metdade de -> {media * 2}')

variavel: str = 'Python para Ciência de Dados'

print(f"variavel='{variavel}'")  # Forma antiga

print(f'{variavel =}')  # A partir do Python 3.8

print(f'{variavel.upper()[::-1] =}')
