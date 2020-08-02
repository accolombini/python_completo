"""
Saindo de loops com break
Funciona da mesma forma que nas linguagens C ou Java
Utilizamos o break para sair de loops de forma definida pelo projeto

"""

# Exemplo 1

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(f'Ainda no loop? {numero}')
print(f'Saiu do loop e numero é -> {numero}')

# Exemplo 2

while True:
    comando = input('Digite fim para sair: ').lower()
    if comando == 'fim':
        break
print(f'Saiu finalmente você digitou -> {comando}')
