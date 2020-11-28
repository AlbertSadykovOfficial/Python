"""
	
	Модули, Пакеты, программы

"""

# Подключение модулей:
	import report
	import report as new_name
	# Вызов функции из модуля:
		report.get_description()
# Подключаем функции из модулей:
	from report import get_description, get_other_info
	from report import get_description as new_name

# Каталог поиска модулей ()
	import sys
	for place in sys.path:
			print(place)

# Обработка отсутствующих ключей:

	# Добавить несуществующий ключ (setdefault) 
		periodic_table = {'Hydrogen': 1, 'Helium': 2}
		carbon = periodic_table.setdefault('Carbon', 12)
		# Если попытаться добавить значение уже в существующий ключ, то будет возвращено существующие значение:
			helium = periodic_table.setdefault('Helium', 228)

	# Значения по умолчанию (defaultdict)
		from collections import defaultdict
		periodic_table = defaultdict(int) # Присвоить в пару новому ключу значение 0 
		periodic_table['Oxygen'] # defaultdict(<class 'int'>, {'Oxygen': 0})

		def no_idea(): return "Huh?"
			bestiary = defaultdict(no_idea) 
		# или через лямбда ф-цию
			bestiary = defaultdict(lambda: "LHuh?") 
		
		bestiary['A'] = 'Basilisk'
		bestiary['B'] # 'Huh?'

			# Пример - счетчик элементов:
					food_counter = defaultdict(int)
					for food in ['spam', 'spam', 'eggs', 'spam']:
							food_counter[food] += 1

					for food, count in food_counter.items():
							print(food,count)

	# Подсчет эл-тов с помощью Counter()
			breakfast = ['spam', 'spam', 'eggs', 'spam']
			breakfast_counter = Counter(breakfast)
			breakfast_counter.most_common() # Вернуть эл-ты по убыванию
			breakfast_counter.most_common(1)# Вернуть эл-ты по убыванию, больше, чем параметр

				# Объединение счетчиков:
						lunch = ['eggs', 'bacon', 'eggs']
						lunch_counter = Counter(lunch)

						breakfast_counter + lunch_counter
						breakfast_counter - lunch_counter
						lunch_counter - breakfast_counter
						breakfast_counter & lunch_counter # Общие элементы (наименьшее значение)
						breakfast_counter | lunch_counter # Выбирает наибольшие значения

	# Упорядочивание по ключу (OrderedDict) - запоминаем порядок, в котором добавлены ключи
			from collections import OrderedDict
			quotes = OrderedDict([
						('Moe', 'A wise guy, huh?'),
						('Larry', 'Ow')
						('Curly', 'Nyuk, Nyuk')
				])
			for stooge in quotes:
					print(stooge)


# Стек + очередь == deque (Удаление элементов с концов последовательнсоти):
		def palindrome(word):
				from collections import deque
				dq = deque(word)
				while len(dq)>1:
						if dq.popleft() != dq.pop()
								return False
				return True

# Иттерируем по структурам кода:
		import itertools

		for item in itertools.chain([1,2], ['a','b']):
				print(item)

		for item in itertools.cycle([1,2]):
				print(item)

		for item in itertools.accumulate([1,2,3,4,5]):
				print(item)

				def multiply(a,b): return a*b
				for item in itertools.accumulate([1,2,3,4,5], multiply):
				print(item)

# Pretty print (pprint)
	from pprint import pprint
	print(quotes)
	pprint(quotes)