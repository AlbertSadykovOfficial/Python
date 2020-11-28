"""

	Веб-сервисы

"""

"""
		Модуль webbrowser
"""

	import antigravity
	import webbrowser

	url = 'http://www.python.org/'
	webbrowser.open(url)
	webbrowser.open_new(url)
	webbrowser.open_new_tab(url)

"""

	API для сети и Representational State Transfer

	Зачастую данные доступны внутри веб страниц, чтобы получить информаци, нужно ее прочитать.
	Вместо того, чтоюы публиковать страницы, можо открыть доступ к данным через web-интерфейс API.
	Клиенты делают запросы по URL  и получают ответы, содержащие статус и данные, 
	вместо HTML, они получают данные по типу JSON или XML.

	Это реализуется через REST-интерфейс.
	Передача состояния предсавления (REST)
		RESTful использует галголы HTTP определенным способом:
		HEAD- информация о ресурсе
		GET - получить данные с сервера
		POST- обновить данные на сервере
		PUT - создать ресурс 
		DELETE - удаление.

	К примеру: сервис REST принимает анные в формате JSON, анализирует их и отравляет ответ в том же формате.


	Краулер (веб-паук) - Программа, получающая данные по сети.
		После того, как программа получила данные, их следует проанализировать  парсинг.
	
	Парсер-фреймворк (Scrapy) (http://scrapy.org/):
		pip install scrapy

	Парсер-модуль BeautifulSoup (http://www.crummy.com/software/BeautifulSoup/)
		pip install beautifulsoup4

"""
