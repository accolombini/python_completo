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

    Num segundo exemplo vamos instalar o módulo externo fpdf2 =>> pip install fpdf2. Este módulo nos permite
    converter para pdf de forma configurada e formatada para o formato .pdf. Para maiores detalhes de uso e
    configuração deste módulo consulte ->> https://pypi.org/project/fpdf2/
    Para usar este módulo externo devemos fazer o seguinte import ->> from fpdf import FPDF


"""
from fpdf import FPDF
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


# Trabalhando com o módulo fpdf

title = '20000 Leagues Under the Seas'
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=15)
pdf.cell(200, 10, txt="Ola Mundo!!!", ln=1, align="C")

# Salvando como pdf

pdf.output("Gera_PDF")
