"""
	
	Всемирная паутина в Python

"""

"""

	Стандартные web-библиотеки Python

	В Python 2 модули web были разбросаны, в Python 3 они в 2х компонентах:
		-http
		-urllib

"""
	import urllib.request as ur
	url = 'http://www.iheartquotes.com/api/v1/random'
	conn = ur.urlopen(url)
	print(conn)
	data = conn.read()
	print(data)
	print(conn.status)
	print(conn.getheader('Content-Type'))

	for key, value in conn.getheader():
			print(key, value)

"""

	Дополнительная библиотека requests:

		Установка:
			pip install requests

"""

	import requests
	url = 'http://www.iheartquotes.com/api/v1/random'
	resp = requests.get(url)
	resp
	print(resp.text)

