#!/usr/local/bin/python3.7
from math import pi


def calcular(raio):
    print('Area do circulo', pi * float(raio) ** 2)


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    calcular(raio)
