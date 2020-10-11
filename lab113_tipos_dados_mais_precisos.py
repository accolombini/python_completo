"""
Novidades da versão 3.8 do Pyhton => tipos de dados mais precisos.

        NOTA:   - Conhecemos -> int, float, dict, list, set, ...
                - Os novos tipos são;
                    - Literal type
                    - Union
                    - Final
                    - Typed dictionaries
                    - Protocools

-------------------------------------------------------------------------------------
# Podemos melhor observar o problema da tipagem com o exemplo a seguir na execução do mypy:


def dobro(valor: int) -> int:
    return valor * 2


print(f'Executando a função dobro -> {dobro(8)}')  # 16
print(f'Executando a função dobro passando uma string -> {dobro("Meca")}')  # MecaMeca


Embora o tenha executado sem problemas, observe a mensagem de mypy
$ mypy lab113_tipos_dados_mais_precisos.py
lab113_tipos_dados_mais_precisos.py:16: error: Argument 1 to "dobro" has incompatible type "str"; expected "int"
Found 1 error in 1 file (checked 1 source file)


"""

# Vamos aos estudos dos novos tipos

# Tipo novo 1: Literal type

from typing import Literal, Union, Final, final, TypedDict, Protocol


# def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
#     pass


# def calcula_v1(operacao:str, num1: int, num2: int) -> None:
#    if operacao == '+':
#        print(f'{num1} + {num2} = {num1 + num2}')
#    elif operacao == '-':
#        print(f'{num1} - {num2} = {num1 - num2}')
#    else:
#        raise ValueError(f'Operação inválida {operacao!r}')  # !r irá colocar o operador entre aspas simples -> destaque

"""
Observe que nem mypy pega esse tipo de erro
$ mypy lab113_tipos_dados_mais_precisos.py
Success: no issues found in 1 source file

"""


# Resolvendo o problema usando Literal -> observe

# def calcula_v2(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
#     if operacao == '+':
#        print(f'{num1} + {num2} = {num1 + num2}')
#     elif operacao == '-':
#         print(f'{num1} - {num2} = {num1 - num2}')
#     else:
#         raise ValueError(f'Operação inválida {operacao!r}')

# calcula_v2('+', 6, 4)  # 6 + 4 = 10
# calcula_v2('-', 10, 2)  # 10 - 2 = 8
# calcula_v2('*', 2, 2)  # ValueError: Operação inválida '*'

"""
Observe que agora mypy capturou o problema
$ mypy lab113_tipos_dados_mais_precisos.py
lab113_tipos_dados_mais_precisos.py:62: error: Argument 1 to "calcula_v2" has incompatible type "Literal['*']"; expected "Union[Literal['+'], Literal['-']]"
Found 1 error in 1 file (checked 1 source file)

"""

# Trabalhando com Union -> em detrminados casos podemos ter a necessidade de retornar um tipo
# ou outro em uma função, union é uma forma elegante de tratar esta questão


# def soma(num1: int, num2: int) -> Union[str, int]:
#     resultado: int = num1 + num2
#
#     if resultado > 50:
#         return f'O valor {resultado} é muito grande. E isso é uma string!'
#     else:
#         return resultado
#
#
# print(f'Tetando soma com -> {soma(5, 25)}')  # Tetando soma com -> 30
# print(f'Tetando soma com -> {soma(25, 25)}')  # Tetando soma com -> 50
# print(f'Tetando soma com -> {soma(35, 25)}')  # Tetando soma com -> O valor 60 é muito grande. E isso é uma string!

# Trabalhando com Final -> como no JAVA pode ser utilizado para criar uma constante

# NOME: Final = 'Grandioso!'
#
# print(f'A nossa constante com o uso do Final -> {NOME}')  # A nossa constante é -> Grandioso!
#
# NOME = 'Mior do que você imagina!!'
#
# Note que para Python ambas as opções irão funcionar, mas veja quando usamos mypy
#
# print(f'A nossa constante sem o uso do Final -> {NOME}')  # A nossa constante sem o uso do Final -> Mior
# do que você imagina!!
"""
Observe o uso de mypy
$ mypy lab113_tipos_dados_mais_precisos.py
lab113_tipos_dados_mais_precisos.py:104: error: Cannot assign to final name "NOME"
Found 1 error in 1 file (checked 1 source file)

"""

# Podemos usar Final também como um decorador será preciso realizar o importe de final (note o f minúsculo)
# Note que esse final é na verdade um decorador -> acompanhe com atenção
# Quando decoramos uma classe com final -> estamos dizendo que nenhuma outra classe poderia estendê-la
# Quando decoramos um método em uma classe -> estamos dizendo que nenhum outro método poderá sobrescrevê-lo
# Pyrhon executaria esse código sem problema algum
# Já mypy pegaria o problema nas heranças de classes, mas ainda deixaria pessa o decorator
# para sobrescrever um método

# @final
# class Pessoa:
#     pass
#
#
# class Estudante(Pessoa):
#     pass
#
#     @final
#     def estudar(self):
#         print(f'Estou estudando')
#
#
# class Estagiario(Estudante):
#     pass
#
#     def estudar(self):
#         print(f'Estudando e estagiaando ...')

"""
Mas observe o que mypy diria a respeito desse código
 mypy lab113_tipos_dados_mais_precisos.py
lab113_tipos_dados_mais_precisos.py:130: error: Cannot inherit from final class "Pessoa"
lab113_tipos_dados_mais_precisos.py:138: error: Cannot inherit from final class "Pessoa"
Found 2 errors in 1 file (checked 1 source file)

"""

# Usando Typed Dictionaries -> Observe que o resultado será um dicionário com -> Chave Valor

# class CursoPython(TypedDict):
#     versao: str
#     atualizacao: int
#
#
# verde = CursoPython(versao='3.9', atualizacao=2020)
#
# print(f'Imprimindo verde -> {verde}')  # Imprimindo verde -> {'versao': '3.9', 'atualizacao': 2020}
#
# outro =CursoPython(algo='vai', coisa=True)
#
# print(f'Note que outro funciona também -> {outro}')  # Note que outro funciona também -> {'algo': 'vai', 'coisa': True}


"""
Mas mypy capturaria o erro
 mypy lab113_tipos_dados_mais_precisos.py
lab113_tipos_dados_mais_precisos.py:165: error: Extra keys ('algo', 'coisa') for TypedDict "CursoPython"
Found 1 error in 1 file (checked 1 source file)

"""

# Por fim vamos estudar os Protocols -> definem regras a serem seguidas
# Todo objeto que simular ou seguir o protocolo serão tratados com estruturas que seguem a um determinado protocolo


class Curso(Protocol):
    titulo: str


def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')


class Venda:
    titulo = '- Olá!!!'


v1 = Venda()

estudar(v1)
