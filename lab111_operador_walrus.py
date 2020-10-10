"""
Novidades da Versão 3.8 => este operador permite fazer a atribuição e retorno de valor em uma única expressão

        - formato do walrus
        - variavel := expressão

# Fariámos assim até a versão 3.7 do Python
cesta = []
fruta = input('Informe a fruta: ').lower()
while fruta != 'jaca':
    cesta.append(fruta)
    fruta = input('Informe a fruta: ').lower()

"""

# Entendendo o Walrus

nome = 'Ciencia de Dados'  # Aqui fazemos a atribuição para a variável nome
print(f'Estamos acostumado com isso em Python -> {nome}')  # Uma vez atribuído podemos imprimir seu valor


# Vamos fazer o mesmo com o Walrus -> lembra vamos atribuir e retornar o valor em um único passo
# Observe a necessiade do uso do parênteses para agurpar todo processo -> variável e valor
print(f'Facilitando a vida com Walrus -> {(nome := "Ciencia de Dados")}')

# Outros exemplos com Walrus

cesta = []
while (fruta := input('Informe a fruta: '). lower()) != 'jaca':
    cesta.append(fruta)
