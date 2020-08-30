"""
Criamos essa cópia de lab27_funcoes_com_parametros para podermos alterar dentro do escopo do laboratório 58
Observe como estamos usando Dunder para profissionalizar nosso módulo Python

Funções com Parâmetros -> funções que recebem parâmetros como dados de entrada <=> se o parâmtro não for
informado teremos um erro -> TypeError mais tarde veremos que podemos definir valores
default como parâmetros de entrada

    _ As funções podem receber n - parâmetros de entrada. Ou seja, podemos receber como entrada
    em uma função quantos parâmetros forem necessários. Eles são separados por vírgulas.
    - Se informarmos um número errado de parâmetro ou argumentos, teremos um TypeError
    _ NOTA: Parâmetros são variáveis declaradas na definição da função
            Argumentos são dados passados durante a execução de uma função
            A ordem dos parâmetros importa
            Argumentos nomeados -> são chamados de Keyword Argumentos =>> neste caso a ordem não será importante

    São funções que recebem dados para serem processados dentro da mesma

    Pensando em um programa qualquer =>> geralmente encontramos:
        - entrada -> processamento -> saída

    Pensando em uma função, já sabemos que temos funções que:
        - Não possuem entrada
        - Não possuem saída
        - Possuem entrada mas não possuem saída
        - Não possuem entrada mas possuem saída
        - Possuem entrada e saída

# Refatorando uma função -> quadrado_de_7() => para a função quadrado()

x = 5555


def quadrado(numero):
    return numero ** 2


quadrado(x)
print(f'A função quadrado para o valor -> {x} - retorna o valor -> {quadrado(x)}')

# Refatorando uma função -> cantar_parabens() -> atribuindo um parâmetro a ela


def cantar_parabens(aniversariante):
    print(f'Parabens a você')
    print(f'Nesta data querida')
    print(f'Muitas felicidades')
    print(f'Muitos anos de vida')
    print(f'Viva o/a {aniversariante}!!!')


cantar_parabens('Hugo')

# cantar_parabens()  #  TypeError: cantar_parabens() missing 1 required positional argument: 'aniversariante

# Exemplos de funções com mais de um parâmetro


def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(f'Teste da função soma -> {soma(7, 34)}')
print(f'Teste da função multiplica -> {multiplica(7, 3)}')
print(f'Teste da função outra -> {outra(7, 4, "De mais!!!")}')

# print(f'Função soma com erro num argumentos -> {soma(7)}')
# TypeError: soma() missing 1 required positional argument: 'b'

# Qulidade de código -> nomeando parâmetros


def nome_completo(string1, string2):
    return f'Seu nome completo é {string1} {string2}'


print(f'Chamando a função nome_completo -> {nome_completo("Vinicius", "Braga")}')


# Refatorando aplicando melhores práticas de programação


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(f'Chamando a função nome_completo -> {nome_completo("Vinicius", "Braga")}')

# A ordem dos parâmetros importa -> exemplo ->> acompanhe

nome = 'Felicity'
sobrenome = 'Jones'

print(f'Chamando a função nome_completo ordem correta -> {nome_completo(nome, sobrenome)}')
print(f'Chamando a função nome_completo ordem inversa -> {nome_completo(sobrenome, nome)}')


# Argumentos nomeados (Keyword Arguments)
# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem

print(f'Usando Keyword na função nome_completo() -> {nome_completo(nome="Marcos", sobrenome="Uriel")}')
print(f'Usando Keyword na função nome_completo() -> {nome_completo(sobrenome="Uriel", nome="Marcos")}')
print(f'Chamando a função nome_completo ordem inversa -> {nome_completo(sobrenome=sobrenome, nome=nome)}')

"""

# Note que a inversão na passagem dos argumentos não alterou a ordem correta


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total  # Uso correto do return


# No teste a seguir estamos avaliando se o módulo está sendo executado localmente ou se ele foi importado
# No caso queremos que ao ser importado apenas a função soma_impares() seja executada

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f'Testando a função soma_impares com a lista -> {soma_impares(lista)}')

    # Erro comum na utilizaço do return
    def soma_impares(numeros):
        total = 0
        for num in numeros:
            if num % 2 != 0:
                total += num
            return total  # Erro no uso do return
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f'Testando a função soma_impares com a lista -> {soma_impares(lista)} -> {type(lista)}')
    tupla = 1, 2, 3, 4, 5, 6, 7, 8, 9
    print(f'Testando a função soma_impares com a tupla -> {soma_impares(tupla)} -> {type(tupla)}')
else:  # Não é usual ->> aqui esta sendo usado apenas como apoio didático
    print(f'Se entramos aqui significa que o módulo lab58b_funcoes_com_parametros foi importado')
