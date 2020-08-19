from random import randint

m = int(input('Введите кол-во колонок: '))
n = int(input('Введите кол-во строк: '))

lst = [[randint(10, 99) for _ in range(m)] for _ in range(n)]
c_sum = [0, ] * m

for line in lst:
    r_sum = 0
    for x in line:
        r_sum += x
        print('{:^4}'.format(x), end=' ')
    print('{:6}'.format(r_sum))
for i in range(n):
    for j in range(m):
        c_sum[j] += lst[i][j]
print()
for i in c_sum:
    print('{:<4}'.format(i), end=' ')
