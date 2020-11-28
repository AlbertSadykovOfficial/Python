"""
	
	Файлы

	Python создал свои файловые опреации по шаблону Unix

"""

	  # Создать файл:
	  	fout = open('oops.txt', 'wt')
	  	print('Oops, Icreated a file', file=fout)
	  	fout.close()

	  # Удалить файл:
	  	 os.remove('oops.txt')
	  	 
	  # Проверить существование:
	  	import os
	  	os.path.exists('oops.txt')
	  	os.path.exists('./oops.txt')

	  # Проверить тип:
	  	name = 'oops.txt'
	  	os.path.isfile(name)
	  	os.path.isdir(name)

	  # Получить путь до файла:
	  	os.path.abspath('oops.txt')

	  # Является ли аргумент абсолютным путем (аргумент не обяхательно должен существовать):
	  	os.path.isabs(name)
	  	os.path.isabs('/big/fake/name')
	  	os.path.isabs('big/fake/name/without/a/leading/slash')

	 	# Копирование/перемещение:
	 		import shutil
	 		shutil.copy('oops.txt', 'ohno.txt')
	 		shutil.move('oops.txt', 'ohno.txt')

	 	# Создаем ссылку:
	 		os.link('oops.txt', 'yikes.txt') # Жесткая ссылка
	 		os.path.isfile('yikes.txt')

	 		os.symlink('oops.txt', 'jeepers.txt') # Символическая ссылка
	 		os.path.islink('jeepers.txt')
	 		# Получить ссылку:
	 			os.path.realpath('jeepers.txt')

	 	# Права и ращрешения на файл:
	 		os.chmod('oops.txt', 0o400) # Возможно, опечатка os.chmod('oops.txt', 0x400)
	 		# Или можно исп констаныт stat
	 			import
	 			os.chmod('oops.txt', stat.S_IRUSR)

	 	# Изменение владельца с помощью chown
	 		uid = 5
	 		gid = 22
	 		os.chown('oops', uid, gid)
