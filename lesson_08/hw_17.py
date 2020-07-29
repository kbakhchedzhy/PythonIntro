str = 'Привет пока и как дела привет еще раз как дела после'
lst = str.lower().split()
d = {}
for i in range(len(lst)):
    d[lst[i]] = lst.count(lst[i])
print(d)