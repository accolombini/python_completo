"""
Deltas de Data e Hora => diferença de datas e horas -> data inicial e data final => delta = data final - data inicial


# Temos a data de hoje
data_hoje = datetime.datetime.now()

# Data para um evento agendado no futuro
aniversario = datetime.datetime(2021, 3, 3, 0)

# Cálculo de delta
tempo_para_evento = aniversario - data_hoje

# Análise dos resultados
print(f'Vamos ao nosso primeiro delta seu tipo -> {type(tempo_para_evento)} seu valor -> {repr(tempo_para_evento)}')
print(f'O tempo que falta para o evento é de -> {tempo_para_evento}')

# Visualizando dados específicos => pode ser feito para qualquer argumento do datetime
print(f'Vamos olhar só para o número de dias -> {tempo_para_evento.days} dias')

# Note a // isso significa divisão de inteiros / divisão float
print(f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 60 // 60} horas')

"""

# Praticando delta de datas

import datetime


# Imagine que estamos trabalhando com boletos e nosso processo concede 3 dias para pagamento do boleto

data_da_compra = datetime.datetime.now()

print(f'A compra foi efetuada em -> {data_da_compra}')

regra_boleto = datetime.timedelta(days=3)  # Note o uso do método timedelta() aplicando nossa regra de 3 dias

print(f'Conhecendo a regra do boleto -> {regra_boleto}')

vencimento_boleto = data_da_compra + regra_boleto

print(f'Imprima o vencimento do boleto -> {vencimento_boleto}')
