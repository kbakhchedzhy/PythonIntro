print('Введите последовательность целых чисел: ')
i = 0
s = 0
k1 = 0
k2 = 0
while 1:
    n = int(input())
    if n == 0:
        print('Конец ввода.\n')
        break
    i += 1
    # сумма
    s += n
    if i == 1:
        maxi = n
        mini = n
    else:
        if n >= maxi:
            maxi = n
        if n <= mini:
            mini = n
    if n % 2 != 0:
        k1 += 1
    else:
        k2 += 1

if i >= 1:
    print('Введено чисел: ', i, 'Сумма чисео: ', s, 'Среднее значение: ', s / i, 'Максимальное число: ', maxi, 'Минима\
льное число: ', mini, 'Нечетных чисел: ', k1, 'Четных чисел: ', k2, sep='\n')
