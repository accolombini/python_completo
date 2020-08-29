"""
Módulos Customizados => como módulos Python nada mais são do que arquivos Python, então todos os arquivos criados
neste curso e os que venham a criar são também módulos Python prontos para serem utilizados

Como exemplo vamos chamar o lab27_funcoes_com_parametros para teste =>> OBSERVE

from lab27_funcoes_com_parametros import soma_impares

Os resultados estranhos são decorrentes do módulo Python lab27 que não deveria ter uma série de execuções e
Exemplos de utilizaçao. Deveria ter apenas e tão somente a definição das funções, ok ->> vale aqui o exemplo
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(f'Chamando a função soma_impares() de lab27_funcoes_com_parametros -> {soma_impares(lista)}')

O erro a seguir é decorrente do fato de estarmos importando a soma_impares -> vamos corrigir esse problema
alerando o import, observe no próximo exemplo.
print(f'Chamando a outros elementos de lab27_funcoes_com_parametros -> {tupla}')  # NameError: name 'tupla' is
not defined

Neste exemplo teremos acesso a tudo o que está definido em lab27_funcoes_com_parametros

import lab27_funcoes_com_parametros as lab27

Os resultados estranhos são decorrentes do módulo Python lab27 que não deveria ter uma série de execuções e
Exemplos de utilizaçao.
print(f'Acessando a tupla -> observe ->> {lab27.tupla}')
print(f'Chamando a função soma_impares() de lab27_funcoes_com_parametros -> {lab27.soma_impares(lab27.lista)}')

"""
# Vamos agora trabalhar com lab38_map

from lab38_map import cidades, c_para_f

print(f'Trabalhando com lab38_map ->> {list(map(c_para_f, cidades))}')
