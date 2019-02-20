from abc import ABCMeta, abstractproperty

class Humano(metaclass=ABCMeta):
    # atributo de classe
    especie = 'Homo Sapiens'


    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @abstractproperty
    def inteligente(self):
        pass

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um inteiro positivo')
        self._idade = idade

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

    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True


if __name__ == '__main__':
#    try:
#        anonimo = Humano('John Rambo')
#        print(anonimo.inteligente)
#    except TypeError:
#        print('classe abstrata')

    jose = HomoSapiens('Jose')
    print('{} da classe {}, inteligente: {}'
        .format(jose.nome, jose.__class__.__name__, jose.inteligente))
    grok = Neanderthal('Grok')
    print('{} da classe {}, inteligente: {}'
        .format(grok.nome, grok.__class__.__name__, grok.inteligente))
