N = int(input('Введите число для сравнения: '))
i = 1
print(N, end=' ')
while 1:
    k = i ** 2
    if N < k:
        break
    print(k, end=' ')
    i += 1
