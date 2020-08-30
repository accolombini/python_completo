"""
Módulos Externos => são módulos que não são instalados previamente com a linguagem Python
                    Para instalar um módulo: pip install <nome_modulo>

    Utilizamos o gerenciador de pacotes Python chamado Pip ->> Python Installer Package
    Você pode conhecer todos os pacotes oficiais no site =>> https://pypi.org

    Para conhecer todos os comandos pip, basta digitar pip no terminal: terminal>pip
                                                                                    Usage:
                                                                                      pip <command> [options]
    Como exemplo vamos instalar o módulo externo Colorama: pip install colorama. O módulo externo
    colorama é utilizado para a impressão de textos coloridos no terminal.
    Para usar colorama é necessário fazer o import de init =>> from colorama inport init e executar a função init()

"""
from colorama import init, Fore, Style, Back
init()

# Exemplos do módulo Colorama
print(f'Teste colorama ->> {Fore.MAGENTA + "Python para Ciência de Dados"}')
print(f'Teste colorama ->> {Fore.RED + "Python para Ciência de Dados"}')
print(f'Teste colorama ->> {Fore.BLUE + "Python para Ciência de Dados"}')
print(f'O que fica após o uso do Fore ->> {"Olá Python"}')  # Note que é preciso resetar as cores
print(f'Teste colorama ->> {Style.RESET_ALL + "Python para Ciência de Dados"}')
print(f'O que fica após o uso do Style.RESET_ALL ->> {"Olá Python"}')  # Voltamos ao normal
print(f'Teste colorama ->> {Back.LIGHTBLACK_EX + "Python para Ciência de Dados"}')
print(f'O que fica após o uso do Back ->> {"Olá Python"}')  # Note que é preciso resetar para que o fundo retorne
print(f'Teste colorama ->> {Style.RESET_ALL + "Python para Ciência de Dados"}')
print(f'O que fica após o uso do Style.RESET_ALL ->> {"Olá Python"}')  # Voltamos ao normal
