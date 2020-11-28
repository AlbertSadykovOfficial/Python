"""
		
	Веб-серверы Python
		

"""

"""
	Простейший web-сервер Python
	
		Включить (в командной строке):
			python -m http.server
			python -m http.server 9999 # Установить сервер на порт 9999
		Выключить:
			Ctrl+C
			
			После установки,по порту 8000 через любой адрес будет открыт доступ к текущему каталогу:
				- Можно ввести в браузере: localhost:8000 или 127.0.0.1:8000
		
		Данный сервер медленнее, чем apache или nginx, поэтому использовать его можно для тестов или простых проектов.

"""


"""
		
	Фреймворки 

"""

"""
	
	Bottle (фрейморк, состоящий из 1 файла) http://bottlepy.org/docs/dev/.

		bottle1.py - запустить сервер с содержимым "It isnt fancy, but it's home page"
		bottle2.py - запустить сервер и ссылаться на фалй index.html
		bottle3.py - запустить сервер и генерировать строку, если перейти по определенному адресу

		Юнит-тест:
		bottle3.py + bottle_test.py:
			[bottle_test заходит на bottle3 созданный сайт, получает от него ответ, 
			сравнивает с шаблоном и если все совпадает, выводит It works]

		Доп параметры run():
			- debug=True - генерирует страницу отладки, если возникает HTTP ошибка 
				(НЕ УСТАНАВЛИВАТЬ debug=True на производственных серверах, чтоы не дать информаию для взлома)
			- reloader=True- перезагружает страницу в бразуере, если именим код 


"""

"""
		
		Flask ("Склянка")

			Более продвинутый фреймвор, чем Bottle, был создан как 1-апрельская шутка, но потом подхвачен... 
			
			Установка:
				pip install flask

			flask1.py - запустить сервер и генерировать строку, если перейти по определенному адресу (альтернатива bottle3.py)
			flask2.py - Передача GET параметров

"""

"""
		Крупные фреймворки, которые позволяют работать с БД:
			django
			web2py
			pyramid
			turbogears
			wheezy.web (Фреймовр повышенной производительности)

			Сравнение фреймворков по таблице:	http://bit.ly/web-frames

"""

"""
		Другие веб-серверы Python, которые работают как Apache и используют несколько процессов:
			uwsgi
			cherrypy
			pylons

		Серверы, использующие 1 процесс, основаны на событиях:
			tornado
			gevent
			gunicorn



"""
"""

		Веб-серверы, не использующие Python

		Apache 
			+ Лучший WSGI модуль: mod_wsgi (https://code.google.com/p/modwsgi/)  (если установлен)
			+ В Windows обычно Apache не установлен и надо его установить: http://bit.ly/apache-htpp

		Чтобы все работало, следует помещать файлы (Linux) в /var/www/test/home.wsgi
			import bottle
			application = bottle.dedault_app()
			@bottle.route('/')
			def home():
					return "apache and wsgi, sitting in a tree"
			# ф-ЦИЮ RUN ВЫЗЫВАТЬ НЕ НУЖНО (т.к не нужно хапускать строенный сервер)

			Чтобы определить сайт по умолчанию для apache, следует прописать строку в VirtualHost:
				WSGIScriptAlias / /var/www/test/home.wsgi

			Или можно запустить через демон, для того следует добавить 2 строки:
				WSGIDeamonProcess mydomain.com user=myuser group=mygroup threads=25
				WSGIProcessGroup mydomain.com


		nginx
			+ Установка: https://wiki.nginx.org/Install
			+ Модуль uWSGI: http://bit.ly/uWSGI

"""