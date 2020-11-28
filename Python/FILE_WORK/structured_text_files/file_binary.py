"""
	
	Работа с бинарными файлами

		Чтобы файл считался бинарным, слежует добавить аргумент (b)

"""

	bdata = bytes(range(0,256))

	fout = open('bfile', 'wb')
	fout.write(bdata)
	fout.close()


	# Чтение файлов 

	fin = open('bfile', 'rb')
	bdata = fin.read()
	fin.close()

	# Автоматическое закрытие файлов менеджером контекстов (with)
	 with open('bfile2', 'wt') as fout:
	 		fout.write(poem)


"""	# Смена позиции:
	
		Функция seek(offset,origin):
		offset - отступ 
		origin:
					 0 - Сместится на offset байт от начала файла (по умолчанию)
					 1 - Сместится на offset байт от текущей позиции
					 2 - Сместится на offset байт от конца файла

"""

	fin = open('bfile', 'rb')
	fin.tell() # Узнать текущую позицию
		fin.seek(255) # Перейти на предпоследний байт
		# или
		fin.seek(-1,2)
		# или
		fin.seek(254,0) fin.seek(1,1)
	bdata = fin.read() # Считать предпоследний байт
	len(bdata)