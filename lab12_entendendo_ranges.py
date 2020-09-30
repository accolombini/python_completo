"""
Prisamos conhecer o loop for para usar os ranges.
Precisamos conhecer o range para trabalhar melhor com o loop for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,mas sim de maneira específica.

Formas gerais:

</> Forma 1 -> range(valor_de_parada) => valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

</> Forma 2 -> range(valor_de_inicio, valor_de_parada) => especifica um início diferente de 0, mantém o passo de
1 em 1 e valor_de_parada é não inclusive

</> Forma 3 -> range(valor_de_inicio, valor_de_parada, passo) => especifica um início diferente de 0,
especifica um passo diferente do default, ou melhor diferente de 1 em 1, valor_de_parada é não inclusive

</> Forma 4 -> range(valor_de_inicio, valor_de_parada, -passo) => especifica um início diferente de 0,
especifica um passo diferente do default, ou melhor diferente de 1 em 1, valor_de_parada é não inclusive. Usado para
fazer a inversão => range -> inverso

"""

# Forma 1
for num in range(11):
    print(f'Valor {num} ', end=' ')
print('\n')  # Apenas para saltar para a linha seguinte
# Forma 2
for num in range(5, 11):
    print(f'Valor {num} ', end=' ')
print('\n')  # Apenas para saltar para a linha seguinte
# Forma 3
for num in range(2, 11, 2):
    print(f'Valor {num} ', end=' ')
print('\n')  # Apenas para saltar para a linha seguinte
# Forma 4
for num in range(10, 3, -1):
    print(f'Valor {num} ', end=' ')
print('\n')  # Apenas para saltar para a linha seguinte
