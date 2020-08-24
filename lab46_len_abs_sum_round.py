"""
Len, Abs, Sum, Round

    Len ->> len() retorna o tamanho (ou seja, o número de itens) de um iterável
    Abs ->> abs() retorna o valor absoluto de um número inteiro ou real. E outras palavras retorna
            o número sem o sinal
    Sum ->> sum() recebe como argumento um iterável, podendo receber um valor inicial, e retorna a soma total
            dos elementos, incluindo o valor inicial. Por default o valor inicial é 0. Para alterar o valor
            inicial basta adicionar uma vírugla após o parâmetro e adicionar o valor desejado que será
            somado ao iterável passado como argumento
    Round ->> round() retorna um número arredonado para n digito de precisão após a casa decimal. Se
              a precisão não for informada usará como retorno o valor inteiro mais próximo da entrada.

"""
# Usando len()
print(f'Usando lem() com string ->> {len("Python para Ciência de Dados")}')
print(f'Usando lem() com lista ->> {len([1, 2, 3, 4, 5])}')
print(f'Usando lem() com tupla ->> {len((1, 2, 3, 4, 5))}')
print(f'Usando lem() com conjunto ->> {len({1, 2, 3, 4, 5})}')
print(f'Usando lem() com dicionário ->> {len({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})}')
print(f'Usando lem() com range ->> {len(range(0, 1000, 5))}')

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte ->> .__len__()
# As funções com essa característica recebem o nome de Dunder ->> neste caso Dunder len =>> observe

print(f'Usando Dunder len ->> {"Olá Mundo !!!".__len__()}')

# Usando abs()
print(f'Usando abs() ->> {abs(7)}')
print(f'Usando abs() ->> {abs(-7)}')
print(f'Usando abs() ->> {abs(7.35)}')
print(f'Usando abs() ->> {abs(-7.35)}')

# Usando sum()
print(f'Trabalhando com sum() usando valor default ->> {sum([1, 2, 3, 4, 5])}')
print(f'Trabalhando com sum() alterando o valor default ->> {sum([1, 2, 3, 4, 5], 15)}')
print(f'Trabalhando com sum() alterando o valor default ->> {sum([1, 2, 3, 4, 5], -15)}')
print(f'Trabalhando com sum() alterando o valor default ->> {sum([1, 2, 3, 4, 5], -25 ** 0.5)}')
print(f'Trabalhando com sum() valores reais ->> {sum([1.2, 3.45, 6.78])}')
print(f'Trabalhando com sum() valores reais tupla ->> {sum((1.2, 3.45, 6.78))}')
print(f'Trabalhando com sum() valores reais conjunto ->> {sum({1.2, 3.45, 6.78})}')
print(f'Trabalhando com sum() valores inteiros dicionário ->> {sum({"a": 1, "b": 2, "c": 3}.values())}')

# Usando round()
print(f'Explorando as possibilidades de round() ->> {round(10.2)}')
print(f'Explorando as possibilidades de round() ->> {round(10.4)}')
print(f'Explorando as possibilidades de round() ->> {round(10.5)}')
print(f'Explorando as possibilidades de round() ->> {round(10.6)}')
print(f'Explorando as possibilidades de round() ->> {round(10.8)}')
print(f'Explorando as possibilidades de round() ->> {round(10.21356789)}')
print(f'Explorando as possibilidades de round() adicionando precisão ->> {round(10.21354789, 4)}')
print(f'Explorando as possibilidades de round() adicionando precisão ->> {round(10.21355789, 4)}')
print(f'Explorando as possibilidades de round() adicionando precisão ->> {round(10.21356789, 4)}')
