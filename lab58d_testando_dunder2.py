import lab58c_testando_dunder1


def funcao2():
    return lab58c_testando_dunder1.funcao1()


if __name__ == '__main__':
    funcao2()
    print(f'lab58d_testando_dunder2.py esta sendo executado localmente e a variável __name__ vale ->> {__name__}')
else:  # Apenas recurso pedagógico
    print(f'lab58d_testando_dunder2.py foi importado e a variável __name__ vale ->> {__name__}')
