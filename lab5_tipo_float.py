"""
Tipo float, decimal => casas decimais
Obs.: o separador de casas decimais na programação é o ponto (.) e não a vírgula (,)
Todas as operações realizadas com inteiros são possíveis com float

"""

# Errado do ponto de vista do float mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))  # Será do tipo tupla

# Certo do ponto de vista float
valor = 1.44
print(valor)
print(type(valor))  # Será do tipo float

# É possível considerando uma tupla
valor1, valor2 = 1, 44
print(f"valor 1 será {valor1}")
print(f"valor 2 será {valor2}")

# Podemos converter um float para um int
# Obs.: Ao converter valores float para interiros, nós podemos perder precisão
res = int(valor)
print(f'O valor inteiro de valor é dado por res {res}')
print(f'O tipo de res é {type(res)}')

# Podemos trabalhar tranquilamente com números complexos => sendo todas as operações de complexos aceitas
x = 5 + 4j
print(f'O tipo de x é {type(x)}')

# Podemos converter de inteiro para float
num = 1_000_000
print(f'O tipo de num é {type(num)}')
print(f'Podemos converter para float usando o cast {type(float(num))} {float(num)}')
