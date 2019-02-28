from functools import reduce

pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17},
]

menores = filter(lambda p: p['idade'] < 18, pessoas)
soma_idades_dos_menores = reduce(
    lambda idades, p: idades + p['idade'], menores, 0)
print(soma_idades_dos_menores)

soma_idades = reduce(lambda idades, p: idades + p['idade'], pessoas, 0)
print(soma_idades)

so_idades = map(lambda p: p['idade'], pessoas)
so_menores = filter(lambda idade: idade < 18, so_idades)
soma_so_das_idades = reduce(
    lambda idades, idade: idades + idade, so_menores, 0)
print(soma_so_das_idades)
