number = input('Введите число для вычисления: ')


def multiple(array):
    print(sum(int(x[i]) * int(x[i+1]) for i in range(1) for x in enumerate(list(array), 1)))
    # OR
    # print(sum([int(array[i]) * (i + 1) for i in range(len(array))]))


multiple(number)