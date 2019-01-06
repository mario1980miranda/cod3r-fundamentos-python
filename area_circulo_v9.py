#!/usr/local/bin/python3.7
from math import pi
import sys
import errno


def calcular(raio):
    return pi * float(raio) ** 2


def help():
    print("E necessario informar o raio do circulo.")
    print(f"Sintaxe: {sys.argv[0][2:]} <raio>")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(1)
    raio = sys.argv[errno.EPERM]
    area = calcular(raio)
    print('Area do circulo: ', area)
