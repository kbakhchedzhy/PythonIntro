from math import sqrt
def square(a):
    P = a * 4
    S = a * a
    d = a * sqrt(2)
    t = (P, S, d)
    return t

a = int(input('Введите сторону квадрата: '))
print('Периметр, площадь и диагональ квадрата: ', square(a))
