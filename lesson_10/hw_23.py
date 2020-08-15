n = int(input('Введите количество всего заказов: '))
order = []
for i in range(n):
    number = int(input('Введите номер заказа: '))
    book = input('Введите название книги и ее автора: ')
    quantity = int(input('Введите количество книг: '))
    price = float(input('Введите стоимость одной книги: '))
    order.append([])
    order[i].append(number)
    order[i].append(book)
    order[i].append(quantity)
    order[i].append(price)
print(order)
order2 = list(map(lambda x: (x[0], round(x[3]*x[2] + 10 if x[2] * x[3] < 100 else x[2] * x[3],2)), order))

print(order2)
