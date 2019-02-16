class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'


    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthanlensis'


if __name__ == '__main__':
    jose = Humano('Jose')
    grok = Humano('Grok')
    grok.das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'Jose.especie: {jose.especie}')
    print(f'Grok.especie: {grok.especie}')