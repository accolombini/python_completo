"""
Try / Except / Else / Finally => trando erros de forma profissional
    O Else é executado se não houver um erro (não for capturado por except). Podemos ter um else para cada
    except definido no seu código.
    O Finally será executado se não houver erro -> passou no try e executou o else e o finally, em outras
    palavras é executado quando não há erros no código.

    Exemplos:
        1- Tratando a entrada de dados para blindá-la com try e except
        num = 0
        try:
            num = int(input('Informe um número:  '))
        except ValueError or TypeError:
            print(f'Entrada de dados incorreta -> Digite um número!')
        if num != 0:
            print(f'Você digitou {num}')

        2 - Tratando a entrada de dados para blindá-la com try e except e else
        try:
            num = int(input('Informe um número:  '))
        except ValueError or TypeError:
            print(f'Entrada de dados incorreta -> Digite um número!')
        else:  # Só entra em else se não for capturada por except
            print(f'Você digitou {num}')

        3- Tratando a entrada de dados para blindá-la com try, except, else e finally
        try:
            num = int(input('Informe um número:  '))
        except ValueError or TypeError:
            print(f'Entrada de dados incorreta -> Digite um número!')
        else:  # Só entra em else se não for capturada por except
            print(f'Você digitou {num}')
        finally:
            print(f'O finally será sempre executado!!!')

        4- Exemplo mais complexo =>> ERRADO
        def dividir(a, b):
            return a / b
        num1 = int(input(f'Informe o primeiro número - numerador: '))
        try:
            num2 = int(input(f'Informe o segundo número - denominador: '))
        except ValueError:
            print(f'O valor precisa ser numérico')
        try:
            print(f'Dividindo num1 por num2 -> {dividir(num1, num2)}')
        except NameError:
            print(f'O valor digitado não está correto!!!')

        5- Exemplo mais complexo =>> CORRETO
            def dividir(a, b):
                try:
                    return int(a) / int(b)
                except ValueError:
                    return f'Dados de entrada incorretos!'
                except ZeroDivisionError:
                    return f'Dados de entrada incorretos divisão por zero reveja seu denominador!'
            num1 = input('Informe o primeiro número -> numerador: ')
            num2 = input('Informe o segundo número -> denominador: ')
            print(f'{dividir(num1, num2)}')

        6- Exemplo mais complexo refatorado =>> GENÉRICO
            def dividir(a, b):
                try:
                    return int(a) / int(b)
                except:
                    return f'Ocorreu um erro!'
            num1 = input('Informe o primeiro número -> numerador: ')
            num2 = input('Informe o segundo número -> denominador: ')
            print(f'{dividir(num1, num2)}')

        7- Exemplo mais complexo =>> SEMI-GENÉRICO
        def dividir(a, b):
            try:
                return int(a) / int(b)
            except (ValueError, ZeroDivisionError):
                return f'Ocorreu um erro!'
        num1 = input('Informe o primeiro número -> numerador: ')
        num2 = input('Informe o segundo número -> denominador: ')
        print(f'{dividir(num1, num2)}')

        8-  Exemplo mais complexo refatorado =>> SEMI-GENÉRICO
            Neste exemplo além da tupla utilizamos o atributo as err para capturar o erro

            def dividir(a, b):
                try:
                    return int(a) / int(b)
                except (ValueError, ZeroDivisionError) as err:
                    return f'Ocorreu um erro! {err}'
            num1 = input('Informe o primeiro número -> numerador: ')
            num2 = input('Informe o segundo número -> denominador: ')
            print(f'{dividir(num1, num2)}')

    Dica de quando e onde tratar código:
        1- Toda entrada deve ser tratada sem exceção
        2- O bloco finally será sempre executado independete se houve ou não exceção
        3- O finally, geralmente, é utilizado para fechar ou desalocar recursos, por exemplo,
        quando se cria uma conexão com um banco de dados, ou também para fechar um arquivo que
        foi aberto para leitura ou escrita


    ATENÇÃO:    Uma entrada de dados indevida pode DESTRUIR SEU SISTEMA - Trate TODAS
                Sempre que possível procure tratar os erros nas funções e não em cada entrada de dados que
                venham a chamar sua função.
                Você é responsável por seu código, entre tate-o para que não existam erros que possam
                incomodar o usuário!!!

"""
# Exemplo mais complexo refatorado =>> SEMI-GENÉRICO
# Neste exemplo além da tupla utilizamos o atributo as err para capturar o erro


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro! {err}'


num1 = input('Informe o primeiro número -> numerador: ')
num2 = input('Informe o segundo número -> denominador: ')

print(f'{dividir(num1, num2)}')
