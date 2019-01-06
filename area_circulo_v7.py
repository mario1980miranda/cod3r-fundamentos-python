#!/usr/local/bin/python3.7
from math import pi
import sys


def calcular(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("E necessario informar o raio do circulo.")
        print(f"Sintaxe: {sys.argv[0][2:]} <raio>")
    else:
        raio = sys.argv[1]
        area = calcular(raio)
        print('Area do circulo: ', area)
