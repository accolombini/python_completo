"""
Teste de memória com Generators => uso mais eficiente dos recusos de memória

        - Sequência de Fibonacci ->> 1, 1, 2, 3, 5, 8, 13, 21, ...


        Teste 1 -> verificando a função
        print(f'Sequência de Fibonacci de 5 termos -> {fib_lista(5)}')

        Teste 2 -> aplicando iterações na função que foi definida utilizando listas
        print(f'Inicio do teste for')
        for n in fib_lista(100):
            print(f'Sequência de Fibonacci de 100 termos -> {n}')

        NOTA:   Para visualizar os efeitos deste testes recomenda-se utilizar algum software do seu SO para monitorar
                consumo de memória. Poderá ser interessante aumentar o número de iterações para que seja visível nos
                testes.

        """
# Função Fibonacci
# Teste 1 ->> função usando listas


def fib_lista(max_term):
    nums = []
    a, b = 0, 1
    while len(nums) < max_term:
        nums.append(b)
        a, b = b, a + b
    return nums


# Função Fibonacci
# Teste 2 ->> usando geradores


def fib_gen(max_term):
    a, b, contador = 0, 1, 0
    while contador < max_term:
        a, b = b, a + b
        yield a
        contador += 1


# Teste 1 -> verificando a função fib_gen()
print(f'Sequência de Fibonacci de 5 termos -> {list(fib_gen(5))}')  # Função ok -> [1, 1, 2, 3, 5]

# Teste 2 -> aplicando iterações na função que foi definida utilizando generators
print(f'Inicio do teste for')
for n in fib_gen(100):
    print(f'Sequência de Fibonacci de 100 termos com Generators -> {n}')
