#!/usr/local/bin/python3.7
arquivo = open('pessoas.csv')

for registro in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
arquivo.close()
