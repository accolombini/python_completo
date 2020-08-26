"""
Debugando com PDB => Python Debugguer

    OBS.:   Usar print() para debugar código é uma prática ruim!
            Existem formas profissionais de se fazer esse "debug", utilizando o debugger
            Em Python, podemos fazer isso em diferentes IDEs, como o PyCharm ou utilizando
            o PDB ->> Python Debugger

    Exemplo:
        1- Utilizando print() para debugar o código =>> PRÁTICA RUIM!!!
            def dividir(a, b):
                print(f'Conferindo os valores a = {a}, b = {b}')
                try:
                    return int(a) / int(b)
                except (NameError, ValueError, ZeroDivisionError) as err:
                    return f'Ocorreu um erro! {err}'
            a = 'b'
            print(f'{dividir(a, 9)}')

        2- Debugando com o PyCharm
            def dividir(a, b):
                try:
                    return int(a) / int(b)
                except (NameError, ValueError, ZeroDivisionError) as err:
                    return f'Ocorreu um erro! {err}'
            print(f'{dividir(6, 0)}')

        3- Debugando com PDB -> Exemplo 1 => PDB
            import pdb
            nome = 'Felicity'
            sobrenome = 'Jones'
            pdb.set_trace()  # Equivale ao break point
            nome_completo = nome + ' ' + sobrenome
            curso = 'Python para Ciência de Dados'
            final = nome_completo + ' faz o curso ' + curso
            print(f'Imprimindo o resultado final -> {final}')

        4- Exemplo 2 => PDB -> chamdo o import na linha de set_trace()
            Por que utilizar este formato?
            O debug é utilizado durante o desenvolvimento. Acostumamos realizar todos os imports de bibliotecas
            no início do arquivo. Por isso, ao invés de colocamos o import do PDB no início do arquivo, o fazemos
            somente no ponto onde faremos o debugger, a ao finalizarmos fazemos a remoção do códio de debug.

            nome = 'Felicity'
            sobrenome = 'Jones'
            import pdb; pdb.set_trace()  # Quando usamos dois comandos Python na mesma linha separamos com (;)
            nome_completo = nome + ' ' + sobrenome
            curso = 'Python para Ciência de Dados'
            final = nome_completo + ' faz o curso ' + curso
            print(f'Imprimindo o resultado final -> {final}')

        5- Exemplo 3 => PDB -> a partir da versão 3.7 do Python, não precisamos mais importar a biblioteca pdb
            pois, os comandos de debug foram incorporados como função built-in (integrada) chamada breakpoint()
            nome = 'Felicity'
            sobrenome = 'Jones'
            breakpoint()  # Usando breakpoint()
            nome_completo = nome + ' ' + sobrenome
            curso = 'Python para Ciência de Dados'
            final = nome_completo + ' faz o curso ' + curso
            print(f'Imprimindo o resultado final -> {final}')

    OBS.: Cuidado com conflitos entre nomes de variáveis e os comandos do PDB


"""

# Debugando com o PDB => Python Debugger
# Para utilizar o Python Debugger, precisamos importar a biblioteca pdb e então utilizar
# a função set_trace()
# Comandos básicos do PDB:
# l -> listar onde estamos no código
# n -> próxima linha
# p -> imprime variável
# c -> continua a execução - finaliza o debugging


# Exemplo 4 => PDB -> cuidados com variáveis com mesmo nome dos comandos do PDB


def soma(l, n, p, c):  # Observe que os parâmetros são exatamente os mesmos nomes dos comandos do PDB
    breakpoint()
    return l + n + p + c


print(f'Imprimindo soma -> {soma(1, 3, 5, 7)}')
# Como os nomes das variáveis são os mesmos dos comandos do PDB, deveos utilizar o comando p para imprimir
# as variáveis. Ou seja: p <nome_da_variável>
# DICA ->> nunca coloque nomes em variáveis que não sejam representativos, busque por nomes que tenham significado
