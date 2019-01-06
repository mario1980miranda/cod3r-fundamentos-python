#!/usr/local/bin/python3.7

PALAVRAS_PROIBIDAS = {'futebol', 'religiao', 'politica'}
TEXTOS = [
    'Joao gosta de futebol e politica',
    'A praia foi divertida',
]

for texto in TEXTOS:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print(f'Texto possui palavras proibidas: {intersecao}')
    else:
        print(f'Texto autorizado: {texto}')
