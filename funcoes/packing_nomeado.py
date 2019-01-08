# **kwargs -> keyworded args
# def resultado_f1(**podium):
#    for posicao, piloto in podium.items():
#        print(f'{posicao} -> {piloto}')


def resultado_f1(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'2) {segundo}')
    print(f'3) {terceiro}')


if __name__ == '__main__':
    # resultado_f1(primeiro='L Hamilton',
    #             segundo='M Vestappen',
    #             terceiro='S. Vettel'
    #             )
    podium = {'segundo': 'M. Vestappen',
              'primeiro': 'L. Hamilton',
              'terceiro': 'S. Vettel',
              }
    resultado_f1(**podium)
