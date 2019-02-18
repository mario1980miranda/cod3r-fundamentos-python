class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'


    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthanlensis'

    # metodo estatico
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthanlensis', 'Sapiens')
        return ('Austrolapiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('Jose')
    grok = Neanderthal('Grok')
    print(f'Evolucao (a partir da classe): {"", "".join(HomoSapiens.especies())}')
    print(f'Evolucao (a partir da instancia): {", ".join(jose.especies())}')
    print(f'Homo Sapiens evlouido? {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal evoluido? {Neanderthal.is_evoluido()}')
    print(f'Jose evoluido? {jose.is_evoluido()}')
    print(f'Grok evoluido? {grok.is_evoluido()}')