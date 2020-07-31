"""
Tipo Booleano => temos duas constantes -> verdadeiro ou falso
No Python => True -> verdadeiro; False -> falso (note que as iniciais são em maísculas)
As operações booleanas se aplicam também a todos os operadores relacionais (< , >, ==, !=, >=, <=)

"""

ativo = True
logado = False
print(f'O valor da variável ativo é => {ativo}')
print(f'O valor da variável logado é => {logado}')

# Operações booleanas básicas
# Negação (not) -> se o valor booleano for verdadeiro o resultado será falso, se for falso será verdadeiro
print(f"A negação da variável ativo é => {not ativo}")

# Ou ou (or)
# É uma operação binária (depende de dois valores/variáveis de entrada) seu retorno será verdadeiro sempre que ao menos
# um dos valores/variáveis de entrada forem verdadeiras
print(f"O resultado do OU booleano entre logado e ativo é => {ativo or logado}")

# E ou (and)
# É uma operação binária (depende de dois valores/variáveis de entrada) seu retorno será verdadeiro se e somente se
# amabos valores/variáveis forem verdadeiros
print(f"O resultado do E booleano entre logado e ativo é => {ativo and logado}")
