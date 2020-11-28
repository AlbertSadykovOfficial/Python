"""
		
		Программы и процессы
	
		Когда мы запускаем отдельную программу, ОС создает один процесс.
		Процесс изолирован от других процессов, он не может видеть другие процессы и мешать им

"""

	# Узнать ID процесса и текущую рабочую папку интерпретатора Python:
		import os
		os.getpid()
		os.getcwd()

	# UID и GID:
		os.getuid()
		os.getgid()

"""
	Процессы

"""
	# Запуск и остановка програм через subprocess:
		import subprocess
		ret = subprocess.getoutput('date')
		ret
			# getoutput принимает команду оболочки 
				ret = subprocess.getoutput('date -u')
				ret = subprocess.getoutput('date -u | wc')
			
			# check_output() принимает список команд, возвращает объект byte
				ret = subprocess.check_output(['date', 'u'])

			# getstatusoutput() Статус выхода другой программы 
				ret = subprocess.getstatusoutput('date')

			# Вернуть код работы, а не результат
				ret = subprocess.call('date')
				ret # 0 - успех
					# Варианты:
					ret = subprocess.call('date -u', shell=True)
					ret = subprocess.call(['date', '-u'])

	# Создать процесс
		# Ф-ция Process порождает новый процесс и запускает функцию do_this() (4 раза).
		 import multiprocessing
		 import os
		 def do_this(what):
		 		whoami(what)
		 def whoami(what):
		 		print('Process %s says: %s' % (os.getpid(),what))
		 if __name__ == '__main__':
		 		whoami("I'm the main program")
		 		for n in range(4):
		 				p = multiprocessing.Process(target=do_this, args=("I'm function %s" % n))
		 				p.start()

	# Убить процесс:
		p.terminate()
	

