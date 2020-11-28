from bottle import route, run
@route('/') # Связываем URL со следующей функцией (/)-домашняя страница
def home():
		return "It isnt fancy, but it's home page"
run(host='localhost', port=9999) # зАПУСТИТЬ СТРОЕННЫЙ ТЕСТОВЫЙ ВЕБ-сервер Bottle