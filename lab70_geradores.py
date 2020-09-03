"""
Geradores => Generators são na verdade Iterators (Iteradores)

            OBS.:   1- O contrário não é verdadeiro, ou seja, nem todo iterator é um generator.
                    2- Uma Generator Function não é um Generator. Ela gera um generator!

            NOTA:   1- Generators podem ser criados com funções geradoras:
                    2- Funções geradoras utilizam a palavra reservada -> yield
                    3- Generators podem ser criados com Expressões Geradoras

            Diferenças entre Funções e Generator Functions (Funções Geradoras)

            -------------------------------------------------------------------------------------------
            |Funções                                     | Generator Functions                        |
            -------------------------------------------------------------------------------------------
            | utilizam return                            | utilizam yield                             |
            -------------------------------------------------------------------------------------------
            | retorna uma vez                            | podem utilizar yield múltiplas vezes       |
            -------------------------------------------------------------------------------------------
            | quando executada retornam um valor         | quando executada, retorna um generator     |
            -------------------------------------------------------------------------------------------

"""

# Exemplo de Função Geradora (Generator Function) -> Note que o yield funciona como um return, mas ele não finaliza a função


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador  # Retorna o valor e fica agualdando o next()
        contador += 1


gen = conta_ate(5)

# Neste primeiro print vamos usar um cast (list), no caso o list para imprimir todos de uma vez
print(f'Testando nossa função geradora -> {list(conta_ate(5))}\nSeu tipo é -> {type(gen)}')  # <class 'generator'>
print(f'Testando nossa função geradora -> {gen}')  # Retorno -> <generator object conta_ate at 0x000001BFA45AADD0>
# Como se observa o retorno de gen é um generator object -> vamos agora usar o next()
print(f'Testando nossa função geradora -> {next(gen)}')


# Neste exemplo vamos iterar usando for
print(f'\n')
gen2 = conta_ate(10)
for num in gen2:
    print(f'Contando até 10 -> {num}')

# Neste exemplo vamos demonstrar o efeito do yield na function generator
print(f'\n')
gen3 = conta_ate(8)
print(f'Contando até 8 -> {next(gen3)}')  # Executa o generator e aguarda o próximo next()
print(f'Observe que já imprimimos algo com next()')
for num in gen3:  # Fornece os próximos next() para o generator
    print(f'Contando até 8 -> {num}')
