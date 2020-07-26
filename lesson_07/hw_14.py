from random import randint

length = 10
lst1 = [randint(1, 100) for _ in range(length)]
lst2 = [randint(1, 100) for _ in range(length)]
lst1.sort()
lst2.sort()
lst3 = []
print(lst1, '\n', lst2)
j = 0
for i in range(len(lst1)):
    while j != length:
        if lst1[i] < lst2[j]:
            lst3.append(lst1[i])
            break
        elif lst2[j] == lst1[i]:
            lst3.append(lst1[i])
            lst3.append(lst2[j])
            j += 1
            break
        # else lst1[i] > lst2[j]
        else:
            lst3.append(lst2[j])
            j += 1
            continue
    else:
        lst3.append(lst1[i])
if i == length - 1:
    while j != length:
        lst3.append(lst2[j])
        j += 1

print(lst3)
