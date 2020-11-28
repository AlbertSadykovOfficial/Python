
""" 
	Структуры даных Python:
		-Списки (изменяемы) 
		-Кортежи (неизменяемые списки)
			+ Занимают меньше места, 
			+ Простая альтернатива объектам, 
			+ Аргументы ф-ции передаются как картежи
		-Словари (списки с ключами)
		-Множества (список с неповторяющимеся значениями)
	
"""
# Списки
		
		# Одномерные
			weekdays=['Monday', 'Tuesday','Tuesday', 'Wednesday'] 
			print(weekdays) #['Monday', 'Tuesday'] 

		# Двумерные 
			matreshka=[['Monday','hello'], 'Tuesday', 'Wednesday'] 
			print(matreshka[1][0])
			print(matreshka[0:2])
			print(matreshka[0::-1])

		# Пустой список	
			empty_list = list();

		# Присвоение и копирование списков:
			a = [1,2,3]

			b = a        # - Присвоение (изменение a - меняет b) 
			
			b = a.copy() # - Копирование
			b = list(a)	 # - Копирование
			b = a[:] 		 # - Копирование

		# Генерирование числовых последовательностей:
			for x in range(0,3): print(x)
			list(range(2,-1,-1)) # [2,1,0]
			list(range(0,11,2))  # [0,2,4,6,8,10]

		# Добавить в конец списка (append):
			holidays = ['Saturday','Sunday']
			weekdays.append('Thursday') # ['Monday', 'Tuesday', 'Tuesday', 'Wednesday', 'Thursday'] 
			weekdays.extend(holidays) 	# Добавит двумерность: ['Monday', 'Tuesday', 'Tuesday', 'Wednesday','Thursday',['Saturday','Sunday']] 

		# Объединяем списки (extend)
			holidays = ['Saturday','Sunday']
			weekdays.extend('Friday')
			weekdays.extend(holidays) # ['Monday', 'Tuesday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday','Sunday'] 
			# или
			weekdays += holidays			# ['Monday', 'Tuesday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday','Sunday'] 

		# Добавить элемент (insert):
			num = ['1','2','4']
			num.insert(2,'3')
			num.insert(1000,'5') # Добавт в конец при превышении.

		# Удаление по индексу (del)
			del num[-1]
			del num[2] # 3 удалит

		# Удаление по значению (remove):
			num.remove('1')

		# Удаление и получение значения (pop):
			num = ['1','2','3','4','5']
			num.pop() # Удалить и вернуть последний элемент
			num.pop(1) # Второй элемент

		# Определить элемент (index)
			num.index('3') # Какой индекс у значения '3'

		# Есть ли элемнт в списке:
			'4' in num # True

		# Подсчет кол-ва элементов
			weekdays.len() # Общее кол-во
			weekdays.count('Word') # 0 - нет таких слов 

		# Преобразование строки в список:
			list('cat')			# ['c', 'a', 't']

		# Преобразование списка в строку (phrase)
			phrase = ['Hello','fckg','World']
			', '.join(phrase) # ', ' - разделитель: Hello, fckg, World

		# Сортировка
			x = sorted(y) # - возвращает отсортированную копию списка
			x.sort() # - сортирует САМ список

			num = ['1','2','3','4','5']
			num.sort(reverse=True)

		# Преобразование в список кортежей
			a_touple = ('ready', 'fire', 'aim')
			list(a_touple)  # ['ready', 'fire', 'aim']
		
		# Экстракция списков с помощью split:
			birthday = '1/6/1952'
			splitme  = 'a/b//c/d///e'

			birthday.split('/')   # ['1', '6', '1952']
			splitme.split('/')	 	# ['a','b','', 'c', 'd','','e']
			splitme.split('//')   # ['a/b', 'c/d','/e']



# Кортежи
		
		# Создать:
			empty_tuple  = ()
			tuple1       = 'HELLO'
			multi_tuple1 = 'HELLO', 'My', 'World'

			# Создать картеж из других объектов:
				tuple(num)

		# Распаковка картежа:
			a, b, c = multi_tuple1

		# Обмен 
			tuple1       = 'HELLO'
			tuple2       = 'BYE'

			tuple1, tuple2 = tuple2, tuple1

# Словари
			
		# Ключи должны быть уникальны

		# Создать:
		 	empty_dict = {}
		 	bierce = 
		 	{
		 		"day" : "Heyheyhey",
		 		"may" : "WayWayWay", 
		 		"ray" : "BeyBeyBey"
		 	}

		# Достать:
			bierce['gay']  # - Если нет такого ключа, тогда будет сгенерировано исключеие
			bierce.get('gay') # - если нет такого, то исключеия не будет - False
			bierce.get('day', 'Not a bierce')

		# Получить список всех ключей:
			bierce.keys() # Python 2 вернет список, python 3 - dict_keys (итерабельное представл ключей).
			list(bierce.keys()) # - Преобразовние dict_keys в список (Python 3)

		# Получение всех значений:
			list(bierce.values())

		# Получить пары ключ - значение:
			list(bierce.items())

		# Преобразование
			arr2 = [['1','a'],['2','b'],['3','c']]
			arr2 = [('1','a'),('2','b'),('3','c')]
			arr2 = ['1a','2b','3c']
			arr2 = ('1a','2b','3c')
			dict(arr2)

		# Добавление, изменение элемента:
			nums1 = 
			{
				'1':'first',
				'3':'third'
			}
			nums1['2'] = 'fourth'
			nums1['2'] = 'second'

		# Объединение (update)
			nums2 = { '4': 'fourth', '5':'fifth'}
			nums1.update(nums2)

			nums3 = {'3':'three'}
			nums1.update(nums3)  # - Значение ключа 3 перепишутся на новые

		# Проверка по наличию ключа:
			'6' in nums1 # False
		
		# Удаление по ключу (del)
			del nums1['5']

		# Удаление всех элементов (очистка):
			nums1.clear()
			nums1 = {}


# Множества:
	
		# Создание:
			empty_set = set()
			set('letters') # {'l','e','t','r','s'}
			set({'1':'x', '2':'y', '3':'z'}) # {'1','2','3'} -вернет только ключи

		# Проверка на наличие значения (for in)
			drinks = {
				'martini': {'vodka', 'vermouth'},
				'manhattan':{'vodka', 'kahlua'},
				'screwdriver':{'orange juice', 'kahlua'}
			}

			for name, contents in drinks.items():
					if 'vodka' in contents:
						print(name)

			# Коктейль с водкой без вермута и молочного
			for name, contents in drinks.items():
					if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
						print(name)

			# Комбинации и операторы:

				# Оператор пересечения множетв (&)
				for name, contents in drinks.items():
					if contents & {'vermouth', 'orange juice'}

				# Коктейль с водкой без вермута и молочного
				for name, contents in drinks.items():
					if 'vodka' in contents and not contents & {'vermouth', 'cream'}


				# Примеры:
					a = {1,2}
					b = {2,3}

					m = drinks['manhattan']
					s = drinks['screwdriver']
					
					# Пересечение:
						a & b # 2
						a.intersection(b) #2

						m & s # kahlua

					# Объединение
						a | b # {1,2,3}
						a.union(b) # {1,2,3}

					# Разность (только члены ПЕРВОГО множества, но не второго)
						a - b # 1
						a.difference(b) 

					# Исключающее ИЛИ:
						a ^ b
						a.symmetric_difference(b)

					# Проверка того, явл ли множество подмножеством другого
						a <= b
						m.issubset(s)

					# Проверка на собственное подмножество (множество должно включать подмножестов+неск других эл-в)
						a < b
						m < s




