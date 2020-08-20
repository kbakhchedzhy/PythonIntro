file = open('students.txt', 'r', encoding = 'utf-8')

lst = file.readlines()
file.close()
list(map(lambda x: x.strip('\n'), lst))

list_std = ['{:<20}'.format(line.split()[1] + ' ' + line[:1] + '. ') + str(round(sum(int(x) for x in line.split()[2:]) / len(line.split()[2:]), 2)) for line in lst]


def compute(array):
    s = 0
    flag = False
    for x in array:
        if float(x.split()[-1]) < 5:
            if not flag:
                print('\nСтуденты, чей средний балл меньше 5:')
            print(x)
            flag = True
        s += float(x.split()[-1])
    print('\nСредний бал всех студентов: ', s)


def rec(array):
    file2 = open('students2.txt', 'w', encoding = 'utf-8')
    for x in array:
        file2.write(x)
        file2.write('\n')
    file2.close()


compute(list_std)
rec(list_std)

file.close()

