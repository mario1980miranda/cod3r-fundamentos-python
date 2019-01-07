#!/usr/local/bin/python3.7
arquivo = open('pessoas.csv')

try:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
except IndexError:
    pass
finally:
    print('finally')
    arquivo.close()

if arquivo.closed:
    print('arquivo foi fechado')