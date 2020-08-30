
def funcao1():
    return f'Python para Ciência de Dados -> lab58c_testando_dunder1.py'


if __name__ == '__main__':
    funcao1()
    print(f'lab58c_testando_dunder1.py -> está sendo executado diretamente e a variável __name__ vale ->> {__name__}')
else:  # Novamente uso pedagógico
    print(f'lab58c_testando_dunder1.py foi importado e a variável __name__ vale ->> {__name__}')
