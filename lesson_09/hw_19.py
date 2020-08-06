def arithmetic(a, b, op):
    if op == '+':
        c = a + b
    elif op == '-':
        c = a - b
    elif op == '*':
        c = a * b
    elif op == '/':
        c = a / b
    return c

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
op = input('Введите операцию над ними: ')
if op == ('+' or '-' or '*' or '/'):
    c = arithmetic(a, b, op)
    print(c)
else:
    print('Error')

