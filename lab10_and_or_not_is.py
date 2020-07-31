"""
Estuturas lógicas: and (e), or (ou), not (não), is (é)

Operadores unários -> not
Operadores binários -> and, or e is

O operandor and -> retorna True se ambos os operadores/variáveis forem True
O operador or -> retorna True se ao menos um dos operadores/variáveis forem True
O operador not -> retorna o valor booleano invertido se for True retorna False se for False retorna True

O operador is -> esta integrado em muitas funções Python => confira com dir(variável) => como exercíco
confira e pratique!!!
Por exemplo variável isupper -> retorna False se variáel não estiver em maiúscula

"""

ativo = True
logado = True
if ativo and logado:
    print(f'Bem vindo usuário {ativo, logado}')
else:
    print(f'Você precisa ativar sua conta, por favor, verifique seu e-mail {ativo, logado}')

# Uso do not
print(f'Ao negar a variável logado => {logado} temos => {not logado}')

# Uso direto
if ativo:
    print(f'Bem vindo usuário! => {ativo}')
else:
    print(f'Voce precisa ativar sua conta, por favor, verifique seu e-mail => {ativo}')

# Uso do is
if ativo is False:
    print(f'Voce precisa ativar sua conta, por favor, verifique seu e-mail => {ativo}')
else:
    print(f'Bem vindo usuário! => {ativo}')

# Mostrando o operador binário is
print(f'Podemos perceber o operador binário nesta simples operação booleana <=> {ativo} é {False} => {ativo is False}')
