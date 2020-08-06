str = 'Ах, Арлекино, Арлекино, \
Нужно быть смешным для для для для всех. \
Арлекино, Арлекино, \
Есть одна награда - смех смех смех смех!'
lst = str.lower().split('. ')
str = ' '.join(lst)
lst = str.lower().split(', ')
str = ' '.join(lst)
lst = str.lower().split('!')
str = ''.join(lst)
lst = str.lower().split(' - ')
str = ' '.join(lst)
lst = str.lower().split(' ')
print(lst)
d = {}
for i in range(len(lst)):
    d[lst[i]] = lst.count(lst[i])
max = 0
for i in range(len(lst)-1):
    key = lst[i]
    key2 = lst[i+1]
    if d[key] > d[key2] and d[key] > max:
        max = d[key]
        t = i
    elif d[key] <= d[key2] and d[key2] >= max:
        max = d[key2]
        t = i

for i in range(len(lst)):
    key = lst[t]
    print(key, d[key])
    break