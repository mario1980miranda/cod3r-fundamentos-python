a1 = [1, 2, 3]
a2 = []

for i in a1:
    a2.append(i*2)

print(f'a: {a2}')


a = [1, 2, 3]
m = map(lambda i: i*2, a)
print(f'm: {list(m)}')
print(tuple(map(lambda i: i ** 2, a)))
