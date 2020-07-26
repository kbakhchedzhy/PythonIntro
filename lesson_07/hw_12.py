from random import randint

length = 10
lst = [randint(1, 100) for _ in range(length)]
print('Список: \n', lst)
k = int(input('Введите индекс элемента для удаления: '))

for el in range(k, length-1):
    lst[el] = lst[el+1]
lst.pop()
# lst = lst[:k] + lst[k+1:10]
# lst.remove(lst[k])
print('Новый список: \n', lst)