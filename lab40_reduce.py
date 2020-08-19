"""
Reduce =>>  a partir do Python versão 3 e superiores a função reduce() não é mais uma funçao integrada (built-in)
            Agora temos que importar e utilizar esta função a partir do módulo 'functools'

            Guido van Rossum (criador do Python) diz =>> utilize a função reduce() se você realmente precisa dela.
            Em todo caso, 99% das vezes um loop for é mais legível que reduce()

            Para entender o reduce()

                - Imagine que você tenha uma coleção de dados:
                - dados = [a1, a2, a3, ..., an]
                - E você tem uma função que recebe dois argumentos:
                - def funcao(x, y):
                      return x * y

                - Assim com map() e filter(), a função reduce() recebe dois argumentos: a função e o iterável
                - reduce(funcao, iteravel)

                - A função reduce(), funciona da seguinte forma:
                    - Passo 1: res1 = f(a1, a2)  =>> aplica a funçao nos dois primeiros elementos da coleção e guarda
                    o resultado
                    - Passo 2: res2 = f(res1, a3) =>> aplica a função passando o resultado do passo1 mais o terceiro
                    elemnto e guarda o res
                    - ...
                    - Isso se repete até o final

            CONCLUSÃO: em cada passo reduce() aplica a função passando como primeiro argumento o resultado da aplicação
            anterior. No final reduce() irá retornar o resultado final

    OBS.: Lembre-se para usar o reduce() nós precisamos de uma função que recebe dois argumentos (que tenha dois
    parâmetros)

"""
# Primeiro importamos functools para utilizar reduce()

from functools import reduce

# Exemplo -> utilizar reduce() para multiplicar todos os números de uma lista ->> no caso dados[]

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Uso não recomendado
multi = lambda x, y: x * y
res = reduce(multi, dados)

print(f'Utilizando reduce() ->> {res}')

# Refatorando nosso código forma correta ->> testes ok

print(f'Trabalhando com reduce() ->> {reduce(lambda x, y: x * y, dados)}')

# Refazendo utilizando o loop for

res = 1
for n in dados:
    res = res * n

print(f'O resultado do desafio utilizando for é ->> {res}')
