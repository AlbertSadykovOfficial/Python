"""

Регулярные выражения:

"""

	import re
	source = 'Young Frankenstain'

	# Поиск совпадения в начале (match)
	m = re.match('You', source)
	if m:
		print(m.group()) # Ф-ция возвращает объект совпадения

	# Поиск шаблона любое кол-во(.) любых символов(*) до слова Frank
	m = re.match('.*Frank', source)  
	if m:
		print(m.group()) # Ф-ция возвращает объект совпадения

	# Поиск шаблона в любом месте (search)
	m = re.search('Frank')
	if m:
			print(m.group())

	# Поиск всех совпадений (findall)
	m = re.findall('n', source)
	m = re.findall('n.', source) # Найти n сиволом после 
	m = re.findall('n.?', source)# Найти n сиволом после (но не обязательно, чтобы этот символ был)

		m # вернет список 

	# Разбить совпадения на списки (split)
	m = re.split('n', source)

	# Заменить совпадения (sub())
	m = re.sub('n', '?', source)


"""
	Шаблоны: специальные символы:

	 \d - Цифровой символ
	 \D - нЕЦИФРОВОЙ СИМВОЛ
	 \w - Букенный или Цифровой символ + знак подчеркивания
	 \W - НЕ \w
	 \s - Пробельный символ
	 \S - НЕ \s
	 \b - Граница слова
	 \B - НЕ \b
"""
	# Для примера возьмем константой, содержащей 100 печатаемых символов ASCII
	import string 
	printable = string.printable
	printable[:]

	re.findall('\d') # Все цифры
	re.findall('\s', printable) # пробелы


"""
	Шаблоны: использование спецификаторов
		
		abc - Буквосочетание abc
		(expr) - expr
		expr1 | epxr2 - expr1 или epxr2

		^ - начало строки
		& - конец строки 

		[abc]  === a|b|c
		[^abc] === !(a|b|c)
		
		prev ? - ноль или одно вклчение prev
		prev * - Ноль или больше включений prev, max кол-во
		prev *?- Ноль или больше включений prev, mon кол-во (символ ? === min)

		prev + - одно или больше вклбченйи prev
		prev{m,n}- От m до n послед вкл prev, max кол-во

		prev (?!next)  - prev, если за ним не нахдится next
		(?<=prev) next - next, если перед ним находится prev

"""

		 source = '''I wish I may, I wish I might
		 							Have a dish of fish tonight'''

		 re.findall('wish|fish', source)
		 re.findall('[wf]ish', source)
		 re.findall('fish tonight.&', source) # Поиск в конце 

		 re.findall('[wsh]+', source) # Найти сочетания сиволов w, s, h
		 re.findall('ght\W', source)  # Найти сочетание ght за которым следует любой символ, кроме букв,цифр и _

		 re.findall('I (?=wish)', source) # СИМВОЛ I, за которым следует слово wish
		 re.findall('(?<=I) wish', source) # wish, перед которым I

		 # Правила Python для регулярных выхражений могут кофнликтовать с правилами для строк
		 # Чтобы избежать этого, следует ставить (r) перед строкой шаблона
		 	re.findall('\bfish', source)
		  re.findall(r'\bfish',source)

"""
	
	Шаблоны - указываем способ вывода совпадения:
	 Шаблоны можно организовывать в группы и выводить, 
	 чтобы организовать группу, нужно поместить шаблон в скобки(шаблон)
	 чтобы дать имя группе, следует сделать так: (?P<GROUP_NAME>.шаблон)

"""

	m = re.search(r'(. dish\b).*(\bfish)', source)
	m.group()
	m.groups()

	m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
	m.group('DISH')
	m.group('FISH')