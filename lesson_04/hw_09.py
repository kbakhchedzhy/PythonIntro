n = int(input('Введите число: '))
i = 0
res = 1
res2 = 1
while res <= n:
    res2 = res
    res *= 2
    i += 1
print(n, i-1, res2, sep=' ')


