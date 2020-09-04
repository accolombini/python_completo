"""
Generators => Teste de Velocidade com Expressões Geradoras
"""
# Fazendo o import do módulo time -> requisito para análise temporal
import time

# Generators (Geradores)


def nums():
    for num in range(1, 10):
        yield num


# Imprimindo da forma fácil com cast -> tuple()
print(f'Testando o generator -> {tuple(nums())}')
gel = nums()
print(f'Testando o generator -> {gel}')  # Retorna um objeto -> <generator object nums at 0x000001631C0163C0>
print(f'Testando o generator -> {next(gel)}')  # Imprime o primeiro elemento do Generator -> 1


# Generator Expression

gel2 = (num for num in range(1, 10))

print(f'Quem é nosso gel2 {gel2}')  # Observe que é um objeto tipo -> <generator object <genexpr> at 0x000001E879C8AA50>
print(f'Podemos caminhar nele com next() da mesma forma -> {next(gel2)}')  # Imprime o primeiro elemento -> 1

# Realizando o teste de velocidade -> precisaremos realizar o import do módulo time

gen_inicio = time.time()
print(f'Valor final da soma Expression -> {sum(num for num in range(100000000))}')  # 100 milhões
gen_tempo = time.time() - gen_inicio

# Usando list Comprehension -> para comparar com Generator Expression

list_inicio = time.time()
print(f'Valor final de soma Comprehension -> {sum([num for num in range(100000000)])}')  # 100 milhões
list_tempo = time.time() - list_inicio

print(f'Generaor expression levou o seguinte tempo -> {gen_tempo}')  # levou o seguinte tempo -> 6.353104829788208
print(f'List Comprehension levou o seguinte tempo -> {list_tempo}')  # levou o seguinte tempo -> 7.936882019042969
