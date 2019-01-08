def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == '__main__':
    print('1')
    todos_params('a', 'b', 'c')
    print('2')
    todos_params(1, 2, 3, legal=True, valor=12.99)
    print('3')
    todos_params('Ana', False, [1, 2, 3], tamanho='M', fragil=False)
    print('4')
    todos_params(primeiro='Joao', segundo='Maria')
    print('5')
    todos_params('Maria', primeiro='Joao')
