"""
Teste 2 -> Abordagem multithread -> Neste exemplo vamos usar duas threads
"""

import time
from threading import Thread

contador = 50_000_000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


t1 = Thread(target=contagem_regressiva, args=(contador//2,))
t2 = Thread(target=contagem_regressiva, args=(contador//2,))

inicio = time.time()
t1.start()  # start da thread
t2.start()  # start da thread
t1.join()  # Executa a thread
t2.join()  # Executa a thread
fim = time.time()

print(f'O tempo de execução usando duas threads em segundos é -> {fim - inicio}')

# O tempo de execução usando duas threads em segundos é -> 2.692340612411499
