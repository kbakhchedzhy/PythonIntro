def season(month):
    if month.lower() == 'январь' or month.lower() == 'февраль' or month.lower() == 'декабрь':
        answer = 'Зима'
    elif month.lower() == 'март' or month.lower() == 'апрель' or month.lower() == 'май':
        answer = 'Весна'
    elif month.lower() == 'июнь' or month.lower() == 'июль' or month.lower() == 'август':
        answer = 'Лето'
    elif month.lower() == 'сентябрь' or month.lower() == 'октябрь' or month.lower() == 'ноябрь':
        answer = 'Осень'
    else:
        print('Такого месяца не существует.')
        exit()

    return answer


a = input('Введите месяц для проверки: ')

print(season(a))