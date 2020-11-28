from bottle import route, run, static_file
@route('/') # Связываем URL со следующей функцией (/)-домашняя страница
def main():
		return static_file('index.html', root='.')
run(host='localhost', port=9999) # зАПУСТИТЬ СТРОЕННЫЙ ТЕСТОВЫЙ ВЕБ-сервер Bottle