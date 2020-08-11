"""
Modulo Collections -> Deque => podemos dizer que o Deque é uma lsta de alta performance

Para maiores informações: https://docs.python.org/3/library/collections.html
Especificamente vá para: https://docs.python.org/3/library/collections.html#collections.deque

"""
# Para trabalhar com Deque precisamos fazer um import

from collections import deque

# Criando Deques

deq = deque('Python')
print(f'Conhecendo nosso primeiro deque -> {deq} - seu tipo é -> {type(deq)}')

# Adicionando elementos no Deque -> uso direto do append (adiciona no final)
deq.append('jujuba')
print(f'Adicionando ao deq com append -> {deq} - seu tipo é -> {type(deq)}')

# Adicionando elementos no Deque -> uso direto do appendleft (adiciona no início)
deq.appendleft('The best')
print(f'Adicionando ao deq com appendleft -> {deq} - seu tipo é -> {type(deq)}')

# Removendo elementos do Deq -> usando o método pop() remove e retorna o último elemento
print(f'Removendo com pop() observe o valor de reotorno -> {deq.pop()}')
print(f'Removendo o último elemento do deq com pop() -> {deq} - seu tipo é -> {type(deq)}')

# Removendo elementos do Deq -> usando o método popleft() remove e retorna o primeiro elemento
print(f'Removendo com popleft() observe o valor de reotorno -> {deq.popleft()}')
print(f'Removendo o último elemento do deq com popleft() -> {deq} - seu tipo é -> {type(deq)}')
