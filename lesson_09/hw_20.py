def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        answer = True
    elif year % 400 == 0:
        answer = True
    else:
        answer = False
    return answer
year = int(input('Введите год для проверки: '))
print(is_year_leap(year))