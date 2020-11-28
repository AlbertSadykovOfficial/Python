"""
	Структуры кода Python

"""

# - Комментарии


	# Продление кода:
		phrase = "Hello" + \
						 "World" + \
						 "!"

# Условне операторы
		color = 'white'
		if 		color == 'red':		print('red')
		elif	color == 'green': print('green')
		else: print('not red, not green')

# Циклы while (Если не пашет в команлной строке, то это потому что при копировании, он отступы слева не вставляет, а они важны для python)
	while True:
				x = input("Input (+) num (q to quite): ")
				if x == 'q': 
					break
				number = int(x)
				if number == 5:
					continue
				print("It's not 5, not 0 and greater than 0")


	# Циклы for:
		rabbits =['NUM1', 'NUM2','NUM3', 'Sleep']
		for rabbit in rabbits:
			print(rabbit)

		accustation = {'room':'ballroom', 'weapon':'lead pipe', 'person':'Col. Mustard'}
		for key in accustation:
			print(key)

		for value in accustation.values():
			print(value)

		for item in accustation.items():
			print(item)

		for key, value in accustation.items():
			print('Key=', key, 'Value=', value)



# Итерирование по нескольким последовательностям (zip):
# (Происходит, пока не закончится наименьшая последовательность):
		days = ['Monday', 'Tuesday', 'Wednesday']
		fruits=['banana', 'apple', 'pineapple', 'peach']

		for day, fruit in zip(days,fruits):
				print(day, ": eat", fruit, '!')

		# Объедиенение Кортежей:
			english = 'Monday', 'Tuesday', 'Wednesday'
			french  = 'Lundi', 'Mardi', 'Mercredi'

			list(zip(english,french)) 
			dict(zip(english,french))

	

# Включения - компактный способ создания структуры данных:
		number_list = []
		for number in range(1,6):
			number_list.append(number)

		# или
		 number_list = list(range(1,6))

		 number_list = [number-2 for number in range(1,6)] # [-1,0,1,2,3,4]

		 number_list = [number for number in range(1,6) if number % 2 ==1] # [1,3,5]

		 rows = range(1,4)
		 cols = range(1,3)
		 cells = [(row,col) for row in rows for col in cols]
		 for cell in cells:
		 	print(cell)
		 for row, col in cells:
		 	print(row,col)

		# Включение словаря:
				word = 'letters'
				letter_counts = {letter: word.count(letter) for letter in word}
				# Иной вариант, ключи будут располагаться по-другому
				letter_counts = {letter: word.count(letter) for letter in set(word)}

		# Включение множества:
				a_set = {number for number in range(1,6) if number % 3 == 1} # {1,4}