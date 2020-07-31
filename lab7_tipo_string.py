"""
Tipo string => em Python um dado/variável colocado entre '', "", aspas duplas triplas \""" \""" e aspas
simles triplas ''' ''' =>> são consideradas strings

Obs.: para representar as aspas triplas foi preciso utilizar o caracter de scape \""" -> caso contrário teriamos um
conflito com as \""" triplas utilizadas no comentário

"""

nome = 'Hoje é o dia do abacate'
print(f'Imprime uma strign => {nome}')
print(f'Imprime o tipo da variável strign => {type(nome)}')
# Incorreto
# frase = 'Avocado's day
# Correto
frase = "Avocado's day"  # Note que a necessidade do uso de uma aspas simples impede o uso das aspas simples neste caso
print(f'A frase do dia de hoje é => {frase}')
# Imagina que queria dar um enter numa frase -> observe
frase2 = 'Dia do abacate \n 31 de julho de 2020'
print(f'Conferindo o enter numa frase => {frase2}')
# Todos os recursos de string estão disponíveis em dir(string)
print(f'Usando um recurso de string disponível na linguagem Python => {frase.upper()}')
print(f'Usando outro recurso de string disponível na linguagem Python => {frase.title()}')
# Um recurso muito útil para se trabalhar com string é o uso do split() ->> que converte uma string numa lista, observe
# que cada palavra da string original foi convertida para um elemento do tipo string de uma lista
print(f'Convertendo uma string em uma lista usando split() => {frase.split()}')
# Conferindo o tipo de frase ao usar o método split()
print(f'O tipo da frase após o uso do split() é => {type(frase.split())}')
print(f'O tipo de frase não foi alterado observe => {type(frase)}')
frase3 = frase.split()
print(f'O tipo de frase3 é => {type(frase3)}')
print(f'Testando o uso de listas observe que apenas a primeira string será impressa => {frase3[0:1]}')
frase4 = 'O dia de hoje é considerado o dia do abacate'
# Na verdade o Python trata uma string como se fosse uma lista separando letras e espaços -> observe o último valor
# no caso 8 do exemplo abaixo não entra na lista, ok -> será impresso de 0 <-> 7
# As operações a seguir são chamadas de SLICE de string
print(f'Observe como o Python trata uma string => {frase4[0:8]}')
# Observe que embora a frase tenha 44 caracteres [0:43] assinalamos até 44 justamente porque o último elemento não
# entra na impressão
print(f'Escrevendo o resto da string => {frase4[9:44]}')
# Podemos facilmente inverter uma string observe a construção a seguir:
# [::-1] =>> esta nos dizendo -> comece do primeiro elemento, vá até o último elemento e inverta (-1)
print(f'Imprimido nossa frase inversmanete => {frase4[::-1]}')
# Outro recurso interessante que temos no uso de string é a facilidade para substituir =>> usando replace
print(f'Explorando o uso do replace na string => {frase4.replace("hoje é", "ontem foi")}')
print(f'Explorando mais um pouco o uso do replace => {frase4.replace("o", "u")}')
