from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

setlocale(LC_ALL, 'pt_BR')

# Listar todos os meses do ano com 31 dias
# 1. (filter)Pegar os indices de todos os meses com 31 dias
# 2. (map) transformar os indices em nome
# 3. (reduce) juntar tudo para imprimir
# print(month_name[1])
# print(mdays[1])
meses_com_mais_dias = filter(lambda mes: mdays[mes] == 31, range(1, 13))
meses_nome = map(lambda mes: month_name[mes], meses_com_mais_dias)
juntar_meses = reduce(
    lambda todos, nome_mes: f'{todos}\n- {nome_mes}', meses_nome, 'Meses com 31 dias: ')
print(juntar_meses)
