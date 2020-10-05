"""
Assertions -> Afirmações, checagens ou questionamentos

    Em Python utilizamos a palavra reservada 'assert' para realizar afirmações simples utilizadas nos testes
    Utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não.
    Se a expressão for verdadeira, retorna None e caso seja, falsa levanta um erro do tipo AssrtionError.


    OBS.:   - nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizada
            - a palavra reservada 'assert' pode ser utilizada em qualquer função ou código nosso ... não precisa
            ser exclusivamente nos testes

    ALERTA: - cuidado ao utilizar 'assert' => se um programa Python for executado com o parâmetro -O,
            nenhum assertion será validado. Ou seja, todas as suas validações já eram.
"""

# Praticndo o uso do assert -> lembra que ele pode ser utilizado em qualquer parte do seu código


def soma_numeros_positivos(a, b):

    assert a > 0 and b > 0, 'Ambos os números precisam ser positivos'
    return a + b


# ret = soma_numeros_positivos(-2, 4)  # AssertionError: Ambos números precisam ser positivos
# print(f'Testando a funçao soma_numeros_positivos() -> {ret}')

ret = soma_numeros_positivos(2, 4)  # 6
print(f'Testando a funçao soma_numeros_positivos() -> {ret}')


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'


comida = input('Informe a comida: ')  # AssertionError: A comida precisa ser fast food -> para pedidos fora da lista
print(f'{comer_fast_food(comida)}')
