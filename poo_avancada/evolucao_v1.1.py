class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'


    def __init__(self, nome):
        self.nome = nome

    # encadeando objetos
    def das_cavernas(self):
        self.especie = 'Homo Neanderthanlensis'
        return self


if __name__ == '__main__':
    jose = Humano('Jose')
    grok = Humano('Grok').das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'Jose.especie: {jose.especie}')
    print(f'Grok.especie: {grok.especie}')