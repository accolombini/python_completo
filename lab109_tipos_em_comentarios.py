"""
Trabalhando com tipos nos comentários -> uma outra forma para tipificar seu código Python

    - # type: (tipoa, tipob, ...) -> tipo retorno => é a forma para você definir tipos em comentários
    - Importante você deve optar por uma das formas de Type Hinting, ou tipando peo comentário, ou tipando diretamente no
    código
    - Embora possível, o uso de annotations é mais interessante e deve ser encorajado
"""

# Exemplos de tipos nos comentários

import math


def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio


print(f'A cincunferência é -> {circunferencia(8)}')

"""
Obsrve o retorno de mypy:
$ mypy lab109_tipos_em_comentarios.py
Success: no issues found in 1 source file

"""

# print(f'A circunferência com erro no argumento -> {circunferencia("melancia")}')

"""
Observe o novo retorno de mypy num cenário de erro:
$ mypy lab109_tipos_em_comentarios.py
lab109_tipos_em_comentarios.py:25: error: Argument 1 to "circunferencia" has incompatible type "str"; expected "float"
Found 1 error in 1 file (checked 1 source file)

"""

# Exemplo com múltiplos argumentos


def cabecalho(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'


"""
Observe o retorno de mypy:
$ mypy lab109_tipos_em_comentarios.py
Success: no issues found in 1 source file

"""

# Forçando um erro -> observe

# cabecalho(texto=55, alinhamento='maca')

"""
Observe o retorno de mypy:
$ mypy lab109_tipos_em_comentarios.py
lab109_tipos_em_comentarios.py:58: error: Argument "texto" to "cabecalho" has incompatible type "int"; expected "str"
lab109_tipos_em_comentarios.py:58: error: Argument "alinhamento" to "cabecalho" has incompatible type "str"; expected "bool"
Found 2 errors in 1 file (checked 1 source file)

"""
# Uma forma não muito usual de usar Type Hinting em comentários


def cabecalho1(
        texto,  # type: str
        alinhamento=True  # type: bool
):  # type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'


"""
Observe o retorno de mypy
$ mypy lab109_tipos_em_comentarios.py
Success: no issues found in 1 source file

"""

# Podemos também, mas não deve ser recomendado

nome = 'Abóbora Madura'  # type: str

"""
Observe o retorno de mypy
$ mypy lab109_tipos_em_comentarios.py
Success: no issues found in 1 source file

"""
