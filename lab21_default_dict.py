"""
Módulo Collections - Default Dict => Dicionários

Para maiores referências: https://docs.python.org/3/library/collections.html#collections.defaultdict

Ao criarmos um dicionário utilizando o Default Dict, nós informamos um valor default,
podemos utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será criada
e o valor defaut será attribuído a ela

NOTA: Funções lambda são funções sem nove, que podem ou não receber parâmetros de entrada e retornam valores

"""
# Para usar um default dict precisamos fazer um import
from collections import defaultdict


# Recordando rapidamente dicionários
dicionario = {'curso': 'Python para Ciência de Dados'}
print(f'Imprimindo o dicionário diretamente -> {dicionario}')
print(f'Imprimindo a partir da chave -> {dicionario["curso"]}')
# Teremos um KeyError: 'abobora'
# print(f'O que acontece quando tentamos imprimir a partir de uma chave não existente -> {dicionario["abobora"]}')

# Trabalhando com default dict()
dicionario = defaultdict(lambda: 0)

print(f'Testando o dicionário sem qualquer valor atribuído \n-> {dicionario} \n- seu tipo é -> {type(dicionario)}')
dicionario['curso'] = 'Python para Ciência de Dados'
print(f'Testando o dicionário com valor atribuído \n-> {dicionario} \n- seu tipo é -> {type(dicionario)}')
# Observe que no teste a seguir não será gerado erro KeyError: 'abobora' e sim retornado o valor defaut <=> 0
print(f'testando agora com uma chave inexistente => {dicionario["abobora"]}')
# Veja que interessante => nesta impressão o valor 0 foi atribído ao dicionário com a chave abobora
print(f'Testando o dicionário com valor atribuído \n-> {dicionario} \n- seu tipo é -> {type(dicionario)}')

# Observe que interessante o exemplo a seguir:
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(f'Imprimindo d -> {d} - seu tipo é -> {type(d)}')
print(f'Imprimindo usando sorted -> {sorted(d.items())}')
# Observe que ao buscarmos por uma chave inexistente nenhum erro será retornado e um [] -> será retornado
# isso ocorre, pois nenhum valor defout foi definido
print(f'testando agora com uma chave inexistente => {d["magenta"]}')
# Veja que interessante => nesta impressão o valor [] foi atribído ao dicionário com a chave magenta
print(f'Testando o dicionário com valor atribuído \n-> {d} \n- seu tipo é -> {type(d)}')
