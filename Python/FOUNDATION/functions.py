
"""
Функции 

	Синтаксис: 
		
		def func_name(params):
			'Строка Документации в 1 строчку (''' Многострочные ''')'
			gloabal var1 # указать, что будет использована глобальная переменная.
			code...
			....

		(the end)
		
		Посмтортеть документацию на функцию: 
			help(func_name)
			help(func_name.__doc__) # Без документирования

		! Переменные и ф-ции нельзя начинать с 2х подчеркиваний.
"""

	#  None - специальное значение, чтобы отличать значения от False (и равных ему '', [], {}, (), set())

		# (Попробуй подставить: None, True, False, '', [], {}, (), set())
		def is_none(thing):
				if thing is None:
						print("It's None")
				elif thing:
						print("It's True")
				else ("It's False")


	# Параметры по умолчанию:
		def menu(arg, result=None)
			if result is None:
					result = []
			result.append(arg)
			print(result)

	# Получаем позиционные аргументы (arg) с помощью *
		def print_more(fst,snd, *another):
				print('1: ', fst)
				print('2: ', snd)
				print('another: ', another)

	# Получение аргументов - Ключевых слов (kwarg) с помощью **
		def print_kwarg(**kwargs):
				print('Keyword args:', kwargs)

		print_kwarg(wine='merlot', entree='mutton', dessert='macaroon')


""" 
	Функции - ОБЪЕКТЫ первого класса. type(func_name) # <class 'function'>

	-Мы можем их присваивать их переменным
	-Использовать как аргументы для други функций
	-Возвращать их из другой функции

"""

	def add_args(arg1,arg2): print(arg1+arg2)
	def run_func(func_name, arg1, arg2): func_name(arg1, arg2)
	run_func(answer)

	def sum_args(*args): return sum(args)
	def positional_args_func(func,*args):return func(*args)
	positional_args_func(sum_args,1,2,3,5,5,6,7)

	# Замыканиы - внтрнние ф-ции, которые запоминают значеня переменных, которые были созданы вне функций:

		def knights(saying):
				def inner():
						return "We are the knights who say: '%s'" % saying
				return inner
		a = knights('Hello')
		b = knights('GoodBye')
		a()
		b()

"""
	Анонимные - лямбда ф-ции, ф-ции выраженные одним выражением.

"""
	stairs = ['hello', 'word', 'upper', 'case']
	def edit_story(words, func):
			for word in words:
					print(func(word))
	# Лямбда принимае 1 аргумент - word
	edit_story(stairs, lambda word: word.capitalize() + '!')

"""
	Генераторы - объект,предназначенный для создания послежоваетльностей.
		При иттерировании генератор отслеживает значение последнего вызова, возвращая следующее.

	Можно иттерированть большие последовательности без создания и сохранения всей последовательности.
	(Часто становятся источники данных для итераторов (range))

	Если код велик, чтобы создать включение генератора, можно создать ф-цию генератора.
	Значение функция возвращает словом yield, а не return
	
"""

	# Функция генератора:
		def my_range(first=0, last=10, step=1):
				number = first
				while number < last:
						yield number
						number += step

		ranger = my_range(1,5) # generator object
		for x in ranger: print(x)
	

"""
	
	Декораторы - ф-ция, которая принимаетодну функцию в качестве аргумента и возвращает другую.
	
	Функция может иметь несколько декораторов.
	Декоратор, размещенный ближе всего к функции выполняется раньше, затем идут вышележащие

"""

	def document_it(func):
			def new_function(*args, **kwargs):
					print("Running function: ", func.__name__)
					print("Positional arguments: ", args)
					print("Keywords arguments:", kwargs)
					result = func(*args, **kwargs)
					print("Result: ", result)
					return result
			return new_function


	# Мануальное присвоение декоратора:
		def add_ints(a,b):
				return a + b
		cooler_add_ints = document_it(add_ints)
		cooler_add_ints(3,5)

	# ИНОЕ присвоение декоратора:
		@document_it
			def add_ints2(a,b):
				return a + b

# Второй декортаор
	def square_it(finc):
			def new_function(*args,**kwargs):
					result = func(*args,**kwargs)
					return result*result
			return new_function

		# Функция с несколькими декораторами:
			@document_it
			@square_it
				def add_ints3(a,b):
					return a + b