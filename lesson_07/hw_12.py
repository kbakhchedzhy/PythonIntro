from random import randint

lst = [randint(1, 100) for _ in range(10)]
print('Список: \n', lst)
k = int(input('Введите индекс элемента для удаления: '))

for el in range(len(lst)-k-1):
    lst[k] = lst[k+1]
    k += 1
lst.pop()
# lst = lst[:k] + lst[k+1:10]
# lst.remove(lst[k])
print('Новый список: \n', lst)