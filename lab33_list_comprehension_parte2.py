"""
List Comprehension =>   podemos tornar essas listas ainda mais poderosas adicionando estruturas condicionais
                        às nossas List Comprehension

"""

# Ilustrando - exemplo inicial -> vamos gerar a partir de uma lista numérica uma lista com números pares e outra ímpar

numeros = [1, 2, 3, 4, 5, 6]
pares = [numero % 2 == 0 for numero in numeros]
impares = [numero % 2 != 0 for numero in numeros]
# Teste 1 -> análise booleana
print(f'Nessa introdução estamos fazendo em duas partes True (pares) -> {pares}')
print(f'Nessa introdução estamos fazendo em duas partes True (ímpares) -> {impares}')
# Agora vamos fazer num único passo e printar o resultado
print(f'Nessa introdução estamos fazendo em uma parte pares -> {[numero for numero in numeros if numero % 2 == 0]}')
print(f'Nessa introdução estamos fazendo em uma parte impares -> {[numero for numero in numeros if numero % 2 != 0]}')

# Refatorando para um código mais profissional
# Qualquer número par módulo 2 terá resultado 0 e 0 para Python é False => not False = True
# Qualquer número ímpar módulo 2 terá resultado 1 e 1 para Python é True

print(f'Nessa refatoração estamos fazendo em uma parte pares -> {[numero for numero in numeros if not numero % 2]}')
print(f'Nessa refatoração estamos fazendo em uma parte impares -> {[numero for numero in numeros if numero % 2]}')

# Exemplo 2 => não há limites para o grau de complexidade basta cuidar da sintaxe e o Python entrega o resultado
# Neste exemplo queremos multiplicar número por 2 se o módulo por 2 for 0 e dividir por 2 se o módulo for 1
print(f'Exemplo um pouco mais complexo -> {[numero * 2 if not numero % 2 else numero / 2 for numero in numeros]}')
