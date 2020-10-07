"""
 Teste 3 -> Abordagem multiprocessing
            Neste exemplo vamos trabalhar com multiprocessing potencializando a capacidade de
            múltiplos cores de seu equipamento

"""
import time
from multiprocessing import Pool

contador = 50_000_000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    pool = Pool(processes=2)  # Usaremos dois cores da máquina -> confira quantos a sua possui
    inicio = time.time()
    r1 = pool.apply_async(contagem_regressiva, [contador//4])
    r2 = pool.apply_async(contagem_regressiva, [contador//4])
    r3 = pool.apply_async(contagem_regressiva, [contador//4])
    r4 = pool.apply_async(contagem_regressiva, [contador//4])
    pool.close()
    pool.join()
    fim = time.time()
    print(f'O tempo de execução usando multiprocessos em segundos é -> {fim - inicio}')

# O tempo de execução usando multiprocessos em segundos (dois cores) é -> 1.3902828693389893
# O tempo de execução usando multiprocessos em segundos (quatro cores) é -> 1.291546106338501
# Ao aumentar no número de processos, percebe claramente o peso de uma execução multiprocessos
