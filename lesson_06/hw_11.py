rows = int(input('Введите высоту (нечетное число): '))
cols = rows * 2 - 1
for i in range(rows):
    print(i, end='\t')
    for j in range(cols):
        if (j == cols // 2 - i or j == cols // 2 + i or i == rows - 1):
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()	

rows = int(input('Введите высоту (нечетное число): '))
cols = rows * 2 - 1
for i in range(rows):
	print(i, end='\t')
	for j in range(cols):
		if j >= cols // 2 - i:
			print('* ', end='')
			if j == cols // 2 + i:
				break
		else:
			print('  ', end='')
	print()
print()

rows = int(input('Введите высоту (нечетное число): '))
cols = rows
for i in range(rows):
	print(i, end='\t')
	for j in range(cols):
		if (j >= cols // 2 - i and i <= rows // 2):
			print('* ', end='')
			if j == cols // 2 + i:
				break
		elif ((j == i - cols // 2 or j == 1.5*(cols - 1) - i) and i >= rows // 2):
			print('* ', end='')
		else:
			print('  ', end='')
	print()
	
rows = int(input('Введите высоту (нечетное число): '))
cols = rows
for i in range(rows):
	print(i, end='\t')
	for j in range(cols):
		if (j >= cols // 2 - i and i <= rows // 2):
			print('* ', end='')
			if j == cols // 2 + i:
				break
		elif ((j == i - cols // 2 or j == 1.5*(cols - 1) - i or j == cols // 2) and i >= rows // 2):
			print('* ', end='')
		else:
			print('  ', end='')
	print()