from bottle import route, run, static_file
@route('/') # Связываем URL со следующей функцией (/)-домашняя страница
def home():
		return static_file('index.html', root='.')
@route('/echo/<thing>') 
def echo(thing):
		return 'Say hello to my friend: %s (bottle)' % thing # Перейдя по ссылке http://localhost:9999/echo/Maria, получим Maria
run(host='localhost', port=9999) # зАПУСТИТЬ СТРОЕННЫЙ ТЕСТОВЫЙ ВЕБ-сервер Bottle