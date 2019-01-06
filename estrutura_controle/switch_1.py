def get_tipo_dia(dia):
    tipo_dias = {
        1: 'Fim de semana',
        2: 'Dia de semana',
        3: 'Dia de semana',
        4: 'Dia de semana',
        5: 'Dia de semana',
        6: 'Dia de semana',
        7: 'Fim de semana',
    }
    return tipo_dias.get(dia, '** invalido **')


def get_dia_semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terca',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sabado',
    }
    return dias.get(dia, '** invalido **')


if __name__ == '__main__':
    for dia in range(0, 9):
        print('{}: {}'.format(dia, get_dia_semana(dia)))
