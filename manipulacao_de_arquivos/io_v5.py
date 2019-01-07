#!/usr/local/bin/python3.7

with open('pessoas.csv') as arquivo: #garantir que o recurso sera fechado no final
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))


if arquivo.closed:
    print('arquivo foi fechado')