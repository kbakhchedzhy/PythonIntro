a = input('Введите количество учащихся в первом классе: ')
b = input('Введите количество учащихся во втором классе: ')
c = input('Введите количество учащихся в третем классе: ')
s = (int(a) + int(b) + int(c)) // 2 + (int(a) + int(b) + int(c)) % 2
print('Всего нужно ', s, ' парт.')