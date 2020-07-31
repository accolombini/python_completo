"""
Escopo de variáveis => são dois os escopos de variáveis <=> variáveis globais e variáveis locais
1- Variáveis globais => são reconhecidas, ou melhor, seu escopo compreende todo o programa
2- Variáveis locais => são reconhecidas. ou melhor, seu escopo compreende o bloco de código onde foi declarada

Para declarar variáveis em Python, basta estabelecer o nome da variável e atribuir um valor

nome_da_variavel = valor_da_variavel

OBS.: Python é uma linguagem de tipagem dinâmica, isso significa que ao declararmos uma variável, não colocmos seu tipo.
O tipo é inferido ao atribuirmos o valor à variável.

Exemplo em C:
int soma = 0;   # declara uma variável do tipo inteiro e atribui valor zero a ela

Exemplo em Java:
int soma = 0;   # declara uma variável do tipo inteiro e atribui valor zero a ela

Exemplo em Python:
soma = 0   # declara uma variável do tipo inteiro e atribui valor zero a ela

A mensagem para a variável novo quando numero é igual a 5 => NameError: name 'novo' is not defined

"""
# Exemplos de variáveis globais
numero = 100
print(f'A variável número é do tipo => {type(numero)} e seu valor é => {numero}')

# Python trabalha com reatribuição, observe no exemplo a seguir:
numero = 'abacate'
print(f'A variável número após reatribuição é do tipo => {type(numero)} e seu valor é => {numero}')

# Exemplos de variáveis locais
numero = 25
if numero > 10:
    novo = numero * 5
    print(f'O valor da variável novo declarada no interior do bloco if é => {novo}')
    print(f'A variável novo passa a existir a partir do momento que se entra no bloco if')

print(f'O valor da variável novo declarada ao passar pelo if é => {novo}')
# print(f'Alterando o valor de numero para 5, não entraremos no bloco if, neste caso a variável novo => {novo}')
