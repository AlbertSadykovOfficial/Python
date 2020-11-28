"""

	События (gevent)

		gevent модифицирует многи стандартные библиотеки Python по типу socket
		для того, чтобы исп его механизм, вместо блокирования. 

		Следует использовать gevent только по назнаени, т.к. нон может нести опасность

		Вместо класса socket модуля gevent, можно использовать его функцию для monkey-pathching.
		Они модифицирую стандартные модули вроде  socket так, чтобы они использоватли зеленые потоки
		вместо того, чтобы каждый раз вызывать версию модуля gevent.
		 # Изменить все обычные сокеты на сокеты gevent (даже в стандартной библиотеке)
			from gevent import monkey
			monkey.patch_socket()
			monkey.patch_all() # Более  масштабно
			
			Monkey-patching, к примеру имп Pinterest

"""

# Пример синхронного поиска сайтов 

	import gevent
	from gevent import socket
	#  Раскомментировать для максимального ускорения
	# import gevent
	# from gevent import monkey; monkey.patch_all()
	# import socket

	hosts = ['www.crappytaxidermy.com', 'www.walterpotterraxidermy.com', 'www.antique-taxidermy.com']
	
	# givent.spawn() - создать зеленый поток ( for: Передаем каждое имя хоста)
	jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts] 
	gevent.joinall(jobs, timeout=5) # Ожидаем завершения всех задач.
	for job in jobs:
			print(job.value)