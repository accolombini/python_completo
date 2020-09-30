"""
Loop while -> A sua forma geral é bem simples
while expressão_booleana:
    ||execução do loop

O bloco while será repetido enquanto a expressão booleana for verdadeira
Expressão Booleana é toda expressão onde o resultado é verdadeiro ou falso
Exemplo:
num = 5
num < 5

Obs.: Em um loop while é importante que o programador assuma o controle do critério de parada para não causar
loop infinito -> Claro o loop infinito pode ser um requisito para seu código ok! Até mesmo neste caso o
programador deve estar no controle

Nota: em Python não existe o do while presentes em linguagens como C e JAVA

"""
# Forma 1
numero = 1
while numero <= 10:
    print(f'O valor de número é -> {numero}')
    numero += 1

# Forma 2
resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou Hugo?').lower()
