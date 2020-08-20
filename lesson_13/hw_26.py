
s = 'AABABBAABBBAB'
print(s)
print()


def ab_replace(str):
    str = s.replace('A', '*').replace('B', 'A'). replace('*', 'B')
    print(str)


ab_replace(s)
