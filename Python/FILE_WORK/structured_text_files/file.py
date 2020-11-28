"""

	Работа с файлами

		Данные могут хранится в:
			- Оперативной памяти
			- Постоянной памяти
"""


	# Открыть, записать целиком и закрыть файл:
		fileobj = open(filename, mode)

		poem = ''' Пойду поем, \n Что съем, то съем! '''

		# Запись через write()
		fout = open('poem', 'wt')
			fout.write(poem)
			fout.close()

		# Запись через print()
		fout2= open('poem2', 'wt')
			print(poem, file=fout2, sep='', end='') # по умолчанию: sep=' ', end='\n'
			fout2.close()

		# Запись длинной послеовтельности (при условии, что файл не сущствует - x) :
		fout3 = open('poem_long.txt', 'xt')
		size = len(poem)
		offset = 0
		chunk = 10
		while True:
				if offset > size:
						break
				fout3.write(poem[offset:offset+chunk])
				offset += chunk

		fout3.close()

"""

	Считываем данные из текстового файла:
	read()
	readline()
	readlines()

"""
	
	fin = open('poem.txt', 'rt')
	poem = fin.read()
	fin.close
	poem

	# Считывать по символам:

	poem = ''
	fin = open('poem.txt', 'rt')
	chunk = 10
	while TRUE:
			fragment = fin.read(chunk)
			if not fragment:
					break
			poem += fragment

	fin.close()

	# Считывать по строкам:
	poem = ''
	fin = open('poem.txt', 'rt')
	while True:
			line = fin.readline()
			if not line:
					break
			poem += line

	fin.close()

	# Считываем все строки и иттерируем по ним:
	poem = ''
	fin = open('poem.txt', 'rt')
	lines = fin.readlines()
	fin.close()
	for line in lines:
			print(line, end='')
	