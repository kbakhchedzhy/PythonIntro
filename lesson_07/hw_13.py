from random import randint

length = 10
lst = [randint(1, 100) for _ in range(length)]
print('Список: \n', lst)
k = int(input('Введите индекс элемента для добавления: '))
C = int(input('Введите число для вставки: '))
i = 1
for el in range(length-1, k, -1):
    lst[el] = lst[el-1]
lst[k] = C
lst.append(randint(1, 100))
print('Новый список: \n', lst)