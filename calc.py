print('-Введите "хуй знает что"')
while True:
	var = input('>> ')
	if var == "+":
		while True:
			a = input('1 chislo\n>> ')
			if a == 'x':
				break
			b = input('2 chislo\n>> ')
			if b == 'x':
				break
			try:
				print('result = ' + str(int(a) * int(b)))
			except ValueError:
				print('Ошибка! Вы ввели букву, или пропуск.')
				print('Повторите попытку, введя число')
			else:
				break

	elif var == "-":
		while True:
			a = input('1 chislo\n>> ')
			if a == 'x':
				break
			b = input('2 chislo\n>> ')
			if b == 'x':
				break
			try:
				print('result = ' + str(int(a) - int(b)))
			except ValueError:
				print('Ошибка! Вы ввели букву, или пропуск.')
				print('Повторите попытку, введя число')
			else:
				break

	elif var == "*":
		while True:
			a = input('1 chislo\n>> ')
			if a == 'x':
				break
			b = input('2 chislo\n>> ')
			if b == 'x':
				break
			try:
				print('result = ' + str(int(a) * int(b)))
			except ValueError:
				print('Ошибка! Вы ввели букву, или пропуск.')
				print('Повторите попытку, введя число')
			else:
				break

	if var == "/":
		while True:
			a = input('1 chislo\n>> ')
			if a == 'x':
				break
			b = input('2 chislo\n>> ')
			if b == 'x':
				break
			try:
				print('result = ' + str(int(a) / int(b)))
			except ValueError:
				print('Ошибка! Вы ввели букву, или пропуск.')
				print('Повторите попытку, введя число')	
			except ZeroDivisionError:
				print('Ошибка! На ноль делить нельзя!')
	if var == 'x':
		break