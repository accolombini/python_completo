"""
O bloco try/except => é utilizado para tratar erros que podem ocorrer no nosso código. Prevenindo assim que
o programa pare de funcionar e o usuário receba mensagens de erro inesperadas. Em linhas gerais o blco pode
ser expresso como: tente realizar esta ação .... se houver problema execute essa .....

    - A forma geral mais simples é:
        try:
            //execução problemática
        :except:
            //o que deve ser feito em caso de problemas

    Exemplos:
        1- Tratando erros genéricos
            a - Tente executar a função ola(), caso encontre erros, imprima a mensagem de erro!
            try:
                ola()  # Conhecemos esse erro, mas aqui vale o exemplo. NameError: name 'ola' is not defined
            except:
                print(f'Não foi possível executar o códio, houve algum problema!')

            b - Tente executar a função len(), caso encontre erros, imprima a mensagem de erro!
            try:
                len(5)  # Conhecemos esse erro, mas aqui vale o exemplo. TypeError: object of type 'int' has no                             len()
            except:
                print(f'Não foi possível executar o códio, houve algum problema!')

        2 - Tratando um erro específico
            a - Tente executar a função len(), caso encontre erros, imprima a mensagem de erro!
            try:
                ola()  # Conhecemos esse erro, mas aqui vale o exemplo. NameError: name 'ola' is not defined
            except NameError:
                print(f'Você está utilizando uma função inexistente!')

            b - Tente executar a função len(), caso encontre erros, imprima a mensagem de erro!
            try:
                len(5)  # Conhecemos esse erro, mas aqui vale o exemplo.
            except TypeError:
                print(f'Você está utilizando uma função inexistente!')

        3 - Tratando um erro espedífico de forma mais profissional

            a - Tente executar a função len(), o erro é capturado e passado para o apelido =>> err
            try:
                len(5)  # Conhecemos esse erro, mas aqui vale o exemplo.
            except TypeError as err:  # Forma Pythonica de atribuir um apelido ao erro
                print(f'A aplicação gerou o seguinte erro: {err}')

        4 - Podemos efetuar diversos tratamentos de erro de uma só vez
            try:
                len(5)  # Conhecemos esse erro, mas aqui vale o exemplo.
            except NameError as erroa:  # Forma Pythonica de atribuir um apelido ao erro
                print(f'A aplicação gerou NameError: {erroa}')
            except TypeError as errob:
                print(f'A aplicação gerou TypeError: {errob}')

        5 - Podemos efetuar diversos tratamentos de erro de uma só vez e um genérico para capturar
            erros desconhecidos

            try:
                len(5)  # Conhecemos esse erro, mas aqui vale o exemplo.
            except NameError as erroa:  # Forma Pythonica de atribuir um apelido ao erro
                print(f'A aplicação gerou NameError: {erroa}')
            except TypeError as errob:
                print(f'A aplicação gerou TypeError: {errob}')
            except:
                print(f'Deu algum tipo de erro não esperado!')

        6 - Melhorando um pouco o tratamento de erros
            dic = {'nome': 'Python'}
            def pega_valor(dicionario, chave):
                try:
                    return dicionario[chave]
                except KeyError:
                    return None
            print(f'Teste da função pega_valor -> {pega_valor(dic, "melao")}')

    OBS.:   Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é SEMPRE
            tratar os erros de forma específica.
"""
# Exemplo 7 - Refatorando adicionando mais tratamento de erros
dic = {'nome': 'Python'}


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


print(f'Teste da função pega_valor -> {pega_valor(7, 4)}')
