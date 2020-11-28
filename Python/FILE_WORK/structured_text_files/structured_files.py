"""
	
	Структурированные текстовые файлы

"""
"""

		Конфигурационные файлы

		Можно изначально прописать конфигурационный файл, потом ситывать его

"""

	import configparser
	cfg = configparser.ConfigParser()
	cfg.read('settings.cfg')
	cfg['french']
	cfg['french']['greeting']
	cfg['files']['bin']

""" 

	CSV

"""
	# Запись
		import csv
		villains = [
				['Doctor', 'No'],
				['Rosa', 'Klebb'],
				['Mister','Big'],
				['Auric','Goldfinger'],
				['Ernst', 'Blofeld']
				]
		with open('villains', 'wt') as fout:
				csvout = csv.writer(fout)
				csvout.writerows(villains)

	# Запись с помощью DictWriter()  - Создаем таблицу с колонками first и last
		# для этого требуется изначально список словарей (пример DictReader)
		with open('villains', 'wt') as fout:
			cout = csv.DictWriter(fout, ['first', 'last'])
			cout.writeheader()
			cout.writerows(villains)

	# Считывание (Список списков):
		with open('villains', 'rt') as fin:
				cin = cvs.read(fin)
				villains = [row for row in cin] # Включение списка

	# Считывание средсвами DictReader (Список словарей)
		with open('villains', 'rt') as fin:
				cin = csv.DictReader(fin, fieldnames=['first', 'last'])
				villains = [row for row in cin]


"""
	XML 

	(Библиотека ElementTree) http://bit.ly/elementtree
		+ xml.dom - представление документа как иерархческой структуры (загружает элемент полностью в память)
		+ xml.sax - разбирает xml по ходу, не загружаю его целиком в память (подойдет для больших объемов) 

	 Защищенное использование xml:
	  from defusedxml.ElementTree import parse
	  	et = parse(xmlfile)
"""
	import xml.etree.ElementTree as et
	tree = et.ElementTree(file='test.xml')
	root = tree.getroot()
	root.tag
	len(root) # Кол-во разделов в menu
	len(root[0]) # Кол-во элементов breakfast

	for child in root:
			print('tag:', child.tag, 'attributes:', child.attrib)
		for grandchild in child:
					print('ttag:', grandchild.tag, 'attributes:', grandchild.attrib)


"""
	JSON - (JavaScript Object Notation)
	
	Следует аккурано работать с datetime, т.к. json требует строку или epoch, а не объект datetime

"""
	import json
	
	# Преобразовать в JSON
	menu_json = json.dumps(menu)
	menu_json
	# Преобразовать обратно в струтуру данных (порядок в словаре может измениться, т.к это Python)
	menu2 = jsos.loads(menu_json)
	menu2


"""
	
	YAML
		Стандартная библиотека Python не содержит YAML, его нужно устанавливать
		Следует аккуратно использовать такие типы данных, по возможности использовтаь:
		Защищенный загрузчик: safe_load(), вместо load()

"""

"""

	Сериализация с помощью pickle

	Сериализация - сохранение структур данных в файл.
	( Не загружем в pickle данные которым не доверяеим)
"""

	import pickle
	import datetime

	now1 = datetime.datetime.utcnow()
	pickled = pickle.dumps(now1)  # Обработанная бинарная строка
	
	now2 = pickle.loads(pickled)
	now1
	now2


	class Tiny():
			def __str__(self):
					return 'tiny'

	obj1 = Tiny()
	obj1
	str(obj1)

	pickled = pickle.dumps(obj1)  # Загрузить данные в файл
	pickled

	obj2 = pickle.loads(pickled)  # Загрузить данные из файла
	obj2
	str(obj2)