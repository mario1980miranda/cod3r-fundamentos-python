#!/usr/local/bin/python3.7

PALAVRAS_PROIBIDAS = ('futebol', 'religiao', 'politica')
TEXTOS = [
    'Joao gosta de futebol e politica',
    'A praia foi divertida',
]

for texto in TEXTOS:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print(f'Texto possui palavras proibidas: {palavra}')
            found = True
            break

    if not found:
        print(f'Texto autorizado: {texto}')
