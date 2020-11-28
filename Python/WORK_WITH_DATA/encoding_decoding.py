"""

	Текстовые строки - последовательность символов в формате Unicode

	Форматы:
		ASCII - стандартынй формат, разработанный в 60-х, имеющий 8 бит (256 значений)
		Unicode - формат, содержащий множество символов разных языков (включает в себя ASCII) (сейчас около 110000 значений)
"""

"""
	Строки в Python 3 - строки формата UNicode, а не массив байтов
	
	Спсобы написания символов:
		\u (\u00FF) - определяют символ, находящийся в одной из 256 плоскостей(первые 2 цифры в 16-м формате) 00-ASCII
		\U (\U01234567A) - Для символов высоких плоскостей (крайний слева 0, затем 8 символов)
		\N (N\{имя}) - позволяет указать символ с помощью Стандартнго имени
									-> имена в списке Unicode были изменены для удобства, чтобы испольовать их в Python нужно:
										(E WITH ACUTE, LATIN SMALL LETTER) изменить на (LATIN SMALL LETTER E WITH ACUTE)

		Модуль unicodedata сдержит функции, которые преобразуют ф-ции в обоих направлениях
			lookup() - принимает имя и возвращает символ
			name()   - принимает символ, возвращает имя в верхем регистре
"""

		import unicodedata
		name = unicodedata.name('A')
		value = unicodedata.lookup(name)

		name = unicodedata.name('\u2603')
		value = unicodedata.lookup(name)

		# Пример \N с изменением написания:
			# ! В списках Unicode E WITH ACUTE, LATIN SMALL LETTER
			place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'

"""
	Так как UNicode содержит 110 000, то для его хранения требуется 3 или 4 байта, что давольно много
	и текст занимает очень много дискового пространства.

	UTF8 - динамическая схема кодирования, использующая для символа Unicode от 1 до 4 байтов,
				 (является стандартной текстовой кодировкой для Python, Linux, HTML)

	Иногда сайты используют другие кодировки (Windows 1252...), 
	если скопирвать такой текст в строку Python, то может сгенерироваться исключение:
 	Некорректная последовательность байтов

 	Лучше всегда спользовать UTF-8, т.к она широко поддерживается и универсальна.
"""

	snowman = '\u2603'
	ds = snowman.encode('utf-8')
	len(snowman) # 1 символ
	len(ds) 		 # 3 байта (т.к ds - переменная bytes)
	ds 					 # b'\xe2\x98\x83'

	# encode имеет 2 параметр, который говорит что делать с неизвестнйо кодировкой:
	ds = snowman.encode('ascii') # Ошибка (strict режим)
	ds = snowman.encode('ascii', 'ignore') #  игнорировать неизвестное : b''
	ds = snowman.encode('ascii', 'replace') #  заменить неизвестное (?): b'?'
	ds = snowman.encode('ascii', 'backslashreplace') # заменить неизвестное Unicode-кодом: b'\\u2603'
	ds = snowman.encode('ascii', 'xmlcharrefreplace') # заменить неизвестное строкой символьной сущности(веб): b'&#9137'
	
	# Декодирование:
	place = 'caf\u00e9'
	place_bytes = place.encode('utf-8')
	place1 = place_bytes.decode('ascii') # Ошибка
	place2 = place_bytes.decode('latin-1') # Искажение
	place3 = place_bytes.decode('windows-1252') # Искажение
	place4 = place_bytes.decode('utf-8')