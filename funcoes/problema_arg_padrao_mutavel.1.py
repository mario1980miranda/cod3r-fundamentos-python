def fibonacci(sequencia=[0, 1]):
    # Uso de mutaveis como valor default (armadilha)
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


def fibonacci_imutavel(sequencia=(0, 1)):
    return sequencia + (sequencia[-1] + sequencia[-2],)


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))

    inicio_imutavel = fibonacci_imutavel()
    print(inicio_imutavel, id(inicio_imutavel))
    print(fibonacci_imutavel(inicio_imutavel))
    restart_imutavel = fibonacci_imutavel()
    print(restart_imutavel, id(restart_imutavel))
