#!/usr/local/bin/python3.7
with open('pessoas.csv') as arquivo: #garantir que o recurso sera fechado no final
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)


if arquivo.closed:
    print('Arquivo de leitura foi fechado')

if saida.close:
    print('Arquivo de escrita foi fechado')