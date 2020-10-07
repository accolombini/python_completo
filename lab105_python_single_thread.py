"""
Teste 1 -> Abordagem convencional -> Python Single Thread
"""

import time
from threading import Thread

contador = 50_000_000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


inicio = time.time()
contagem_regressiva(contador)
fim = time.time()

print(f'O tempo de execução single thread em segundos é -> {fim - inicio}')

# O tempo de execução single thread em segundos é -> 5.774231195449829
