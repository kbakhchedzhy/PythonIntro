file = open('rec.txt', 'w', encoding = 'utf-8')

while True:
    str = input('Введите строку: ')
    if str == '':
        print('Запись в файл завершена.')
        break
    file.write(str)
    file.write('\n')

file.close()
