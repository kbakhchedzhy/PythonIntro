from random import randint


def myprint(lst):
    for line in lst:
        for x in line:
            print('{:^4}'.format(x), end=' ')
        print()


def bubble_sort(lst):
    for k in range(m): #счетчик
        for j in range(m - 1 - k): #символ
            if lst[-1][j] > lst[-1][j+1]:
                lst[-1][j], lst[-1][j+1] = lst[-1][j+1], lst[-1][j]
                for i in range(m):
                    lst[i][j], lst[i][j + 1] = lst[i][j + 1], lst[i][j]
    for k in range(m):
        for j in range(m):
            if j % 2:
                for i in range (m - 1 - k):
                    if lst[i][j] > lst[i + 1][j]:
                        lst[i][j], lst[i + 1][j] = lst[i + 1][j], lst[i][j]
            else:
                for i in range(m - 1 - k):
                    if lst[i][j] < lst[i + 1][j]:
                        lst[i][j], lst[i + 1][j] = lst[i + 1][j], lst[i][j]
    return lst


m = int(input('Введите размер сетки: '))
lst = [[randint(1, 50) for _ in range(m)] for _ in range(m)]

sum_col = [sum(line[i] for line in lst) for i in range(m)]
lst.append(sum_col)
myprint(lst)

print()
print()

myprint(bubble_sort(lst))