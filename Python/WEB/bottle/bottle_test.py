import requests
resp = requests.get('http://localhost:9999/echo/Alba')
if resp.status_code == 200 and resp.text == 'Say hello to my friend: Alba':
	 print('It works')
else:
	print('Faild:', resp.text)