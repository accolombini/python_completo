"""
Funções com parâmetro padrão -> Default Parameters

    - São funções onde a passagem de parâmetros seja opcional
    - Em funções Python, os parâmetros com valores default (padrão) DEVEM semrpe estar ao final da declaração
    - Se não respeitar essa proposição terá como retorno -> SyntaxError: non-default argument follows default argument

Por quê utilizar parâmetros com valor default
    - Nos permite ser mais flexíveis nas funções
    - Evite erros com parâmetros incorretos
    - Nos permite trabalhar com exemplos mais legíveis

Quais tipos de dados podemos utilizar como valores default para parâmetros?
    - Qualquer tipo de dado:
    - Numeros
    - Strings
    - Floats
    - Booleans
    - Listas
    - Tuplas
    - Dicionários
    - Funções
    - etc...

Escopo => A ideia é evitar problemas e confusões -> então fique atento
    - Variáveis globais -> visivel em todo escopo do programa
    - Variáveis locasi -> visivel no escopo no qual foi definida (interna)
    - Importante a variável LOCAL se sobrepõem à variável GLOBAL

ATENÇÃO => cuidado com variáveis GLOBAIS se puder evitá-las EVITE!!!
        => podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de
        => escopo de variável

"""

# Exemplo -> analise a função print() => observe que a passagem de parâmetro é opcional

print(f'Python para Ciência de Dados')
print()  # Sem parâmetro -> apenas imprime uma linha em branco
print(f'Note que houve um pular de linha entre as duas mensagens')


# Exemplo -> analise a função quadrado() => observe que a passagem de parâmetro é obrigatória


def quadrado(num):
    return num ** 2


print(f'A função quadrado com um parâmetro -> {quadrado(6)}')


# print(f'A função quadrado sem um parâmetro -> {quadrado()}')  # TypeError: quadrado() missing 1 required positional argument: 'num'

# Exemplo -> analise a função exponencial() => observe que a passagem de parâmetro é obrigatória


def exponencial(numero, potencia):
    return numero ** potencia


print(f'A função exponencial com seus parâmetros -> {exponencial(6, 2)}')
print(f'A função exponencial com seus parâmetros -> {exponencial(30, 20)}')


# Exemplo -> analise a função exponencial() => observe que agora queremos que a homissão da potência indique que
# o número deve ser elevado ao quadrado <=> note que a homissão do parâmetro não incorre em erro

# Vamos então refatorar a função exponencial para atender a essa demanda


def exponencial(numero, potencia=2):  # Observe que estamos definindo potencia = 2 como padrão
    return numero ** potencia


print(f'A função exponencial com um de seus parâmetros -> {exponencial(6)}')
print(f'A função exponencial com seus parâmetros -> {exponencial(30, 20)}')


# OBS:
# Se o usuário passar apenas um argumento, este será atribuído ao parâmetro numero, e será calculado o quadrado deste
# numero. Caso o usuário passe dois argumentos, o primeiro será atribuído ao parâmetro numero e o segundo ao
# parâmetro potencia. Então a função calculará o numero elevado a esta potencia

# A pergunta agora é: Podemos tornar todos os parâmetros opcionais => Observe sua resposta -> use com sabedoria,
# busque por soluções que sejam de fato interessantes. Mas vale aqui o aprendizado


def exponencial(numero=5, potencia=2):  # Observe que estamos tornando os dois parâmetros padrões
    return numero ** potencia


print(f'A função exponencial com um de seus parâmetros -> {exponencial(6)}')
print(f'A função exponencial com seus parâmetros -> {exponencial(30, 20)}')
print(f'A função exponencial sem seus parâmetros -> {exponencial()}')


# Cudiado -> parâmetros default devem ser declarados no final das declarações da função


# def teste_erro(num=2, potencia):  SyntaxError: non-default argument follows default argument
#     return num ** potencia


# print(f'A função teste_erro com seus parâmetros -> {teste_erro(6)}')

# Refatorando a função teste_erro() para teste_acerto()


def teste_acerto(potencia, num=2):
    return num ** potencia


print(f'A função teste_acerto com seus parâmetros -> {teste_acerto(6)}')


# Outros exemplos


def soma(num1=1, num2=20):
    return num1 + num2


print(f'Brincando com soma passando dois argumentos -> {soma(2, 200)}')
print(f'Brincando com soma passando um argumento -> {soma(200)}')  # Note que o argumento será atribuído a num1
print(f'Brincando com soma não passando argumentos -> {soma()}')


# Trabalhando um exemplo com maior grau de complexidade


def mostra_informacao(nome='nerd', instrutor=False):
    if nome == 'nerd' and instrutor:
        return 'Bem vindo instrutor nerd'
    elif nome == 'nerd':
        return 'Eu pensei que com esse nome você fosse o instrutor, desculpe!'
    return f'Ola {nome}'


print(f'Chamando mostra_informação sem argumento algum -> {mostra_informacao()}')
print(f'Chamando mostra_informação com um argumento -> {mostra_informacao(instrutor=True)}')
print(f'Chamando mostra_informação com um argumento -> {mostra_informacao(True)}')  # Cuidado aqui -> fique atento
print(f'Chamando mostra_informação com um argumento -> {mostra_informacao("Zorro")}')
print(f'Chamando mostra_informação com um argumento -> {mostra_informacao(nome="Marcos")}')


# Exemplo passando função como parâmetros


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(f'Chamando a função mat -> {mat(2, 3)}')
print(f'Chamando a função mat -> {mat(2, 2, subtracao)}')


# Entendendo melhor o conceito de Escpo na prática -> observe a variável instrutor global

instrutor = 'nerd'  # instrutor é uma variável global


def diz_oi():
    return f'Oi {instrutor}'


print(f'Testando uma variável global chamando a função diz_oi -> {diz_oi()}!!')


# Entendendo melhor o conceito de Escpo na prática -> observe a variável instrutor agora definida também de forma
# LOCAL interna à função -> note qual das variáveis será impressa ao chamar a função diz_oi()
# Importante a variável LOCAL se sobrepõem à variável GLOBAL


def diz_oi():
    instrutor = 'Julia'  # Observe que o PEP 8 já nos avisa do problema, mas aqui estamos estudando.
    return f'Oi {instrutor}'


print(f'Testando uma variável local chamando a função diz_oi -> {diz_oi()}!!')

# Atenção no uso da variáveis Locais e Globais =>> acompanhe o problema ->> NameError


def diz_oi():
    prof = 'Mariana'  # Observe que prof é uma variável local à função, portanto, não é vista externamente!
    return f'Olá {prof}!!!'


print(f'Testando uma variável local chamando a função diz_oi -> {diz_oi()}!!')
# print(f'Testando uma variável local externamente a função -> {prof}!!')  # NameError: name 'prof' is not defined


# Variáveis Globais =>> cuidado se puder evite-as -> Fique atento o Paycharm já te avisa, mas nem sempre estamos
# no PayCharm

total = 0  # Variável Global ->> note que a função não reconhecerá a inicialização de total GLOBAL


# def incrementa():  # UnboundLocalError: local variable 'total' referenced before assignment
#    total += 1  # Note que para a função a variável total não foi inicializada para processamento
#    return total


# print(f'Problemas com variáveis globais -> {incrementa()}')

# Refatornado o código e corrigindo o problema =>> precisaremos dizer que a variável na função é GLOBAL >>= observe


def incrementa():
    global total  # Aqui avisamos que queremos utilizar a variável global
    total += 1
    return total


print(f'Problemas com variáveis globais observe como resolver -> {incrementa()}')

# Exemplo de funções declaradas dentro de funções => observe o escopo das variáveis


def fora():
    contador = 0

    def dentro():  # dentro() é uma função interno a fora() -> Esta no escopo da função fora()
        nonlocal contador  # nonlocal => a variável não é local e nem global ela é da funçào mais externa -> fora()
        contador = contador + 1
        return contador
    return dentro()  # Note que o retorno da função fora() é uma chamada para a função dentro()


print(f'Teste de funções dentro de funções -> {fora()}')
# print(f'Teste de funções dentro de funções atenção ao escopo -> {dentro()}')  #NameError: name 'dentro' is not defined
