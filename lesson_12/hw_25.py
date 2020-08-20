from random import randint


def myprint(array):
    for line in array:
        for x in line:
            print('{:^4}'.format(x), end=' ')
        print()


def bubble_sort(array):
    for k in range(m): #счетчик
        for j in range(m - 1 - k): #символ
            if array[-1][j] > array[-1][j+1]:
                array[-1][j], array[-1][j+1] = array[-1][j+1], array[-1][j]
                for i in range(m):
                    array[i][j], array[i][j + 1] = array[i][j + 1], array[i][j]
    for k in range(m):
        for j in range(m):
            if j % 2:
                for i in range (m - 1 - k):
                    if array[i][j] > array[i + 1][j]:
                        array[i][j], array[i + 1][j] = array[i + 1][j], array[i][j]
            else:
                for i in range(m - 1 - k):
                    if array[i][j] < array[i + 1][j]:
                        array[i][j], array[i + 1][j] = array[i + 1][j], array[i][j]
    return array


m = int(input('Введите размер сетки: '))
lst = [[randint(1, 50) for _ in range(m)] for _ in range(m)]

sum_col = [sum(line[i] for line in lst) for i in range(m)]
lst.append(sum_col)
myprint(lst)

print()
print()

myprint(bubble_sort(lst))