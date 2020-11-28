"""
	
	Redis 

	Сервер структур данных. Данные помещаются в оперативную память (с возможностью сохранения на диск)

		Отличие от memcache:
			1) Умеет сохранять анные в ПЗУ для надежности в случае перезагрузки
			2) Хранить старые данные 
			3) Предоставлять более сложные структуры данных.

	Типы данных схожи с Python, 
	поэтому Redis может быть использован как промежуточное решение, чтобы несколько приложений делились данными друг с другом
	
	Установить драйвер:
	pip install redis

	Параметры подключения к Redis по умолчанию:
		- localhost
		- Порт: 6379
"""

	import redis
	conn = redis.Redis()
	# ИЛИ
	conn = redis.Redis('localhost')
	conn = redis.Redis('localhost', 6379)


	# Перечислитиь все ключи:
		conn.keys('*')

"""
	Строки 

"""
	# Создадим строку:
		conn.set('secret', 'ni!')
		conn.set('carats', 24)
		conn.set('fever', 101.5)
		conn.mset({'pie': 'cherry', 'cordial': 'sherry'})

		con.get('carats')
		con.mget(['fever', 'carats'])

	# Удалить строку:
		conn.delete('fever')

	# Установить новое значение, если ключа НЕ существует:
		conn.setnx('secret', 'new_value_secret')

	# Установить новое значение, и вернуть старое значение:
		conn.getset('secret', 'new_value_secret')

	# Получить подстроку:
		 conn.getrange('secret', -6, -1)

	# Заменть подстроку
		conn.setrange('secret', 0, 'NEW')


	# Инкремент, декремент:
		 conn.set('fever', 101.5)

		 conn.incr('carats')
		 conn.incr('carats', 10)
		 conn.decr('carats')
		 conn.decr('carats',15)

		 conn.incrbyfloat('fever')
		 conn.incrbyfloat('fever', 0.5)
		 conn.incrbyfloat('fever', -2.0)


"""
	Списки (l)
	
	Списки Redis могут содержать только строки 

"""
	# Добавим 1 элемент (1й параметр - ключ)
	conn.lpush('zoo', 'bear')

	# Добавим еще 2 эл-та:
	conn.lpush('zoo', 'alligator', 'duck')

	# Вводим элементы до и после другого:
	conn.linsert('zoo', 'before', 'bear', 'beaver')
	conn.linsert('zoo', 'after', 'bear', 'cassowary')

	# Добавим элемент со смещением:
	conn.lset('zoo', 2, 'marmoset')

	# Добавим эл-т в конец:
	conn.rpush('zoo', 'yak')

	# ПОЛУЧИТЬ ЭЛ-Т ПО ЗАДАННОМУ СМЕЩЕНИЮ С ПОМОЩЬЮ LINDEX:
	conn.lindex('zoo', 3)
	
	# ПОЛУЧИТЬ ЭЛ-Т в  диапазоне СМЕЩЕНИй С ПОМОЩЬЮ lrange:
		conn.lrange('zoo', 0, 2)

	# Обрезать список с помощью ltrim:
	conn.ltrim('zoo', 1, 4)


"""
		ХЭШИ (h)
	
		Хэши Redis похожи на словари Python, но могут содержать только строки. 
		Поэтому можно создать только одноменый словарь 

"""
	
	conn.hset('song', 'do', 'a deer')
	сonn.hmset('song', {'re': 'about a deer', 'mi': 'a note to follow re'})
	conn.hsetnx('song', 'fa', 'a note that rhymes with la') # Записать значене, если его еще нет

	# Получить значение
	conn.hget('song', 'me')
	conn.hmget('song', 're', 'do')
	
	# Получить все ключи и значения
	conn.hkeys('song')
	conn.hvals('song')
	conn.hgetall('song')

	con.hlen('song')


"""
		Множества (s)
		
		Похожи на Python

"""

		conn.sadd('zoo', 'duck', 'goat', 'lion')
		con.sadd('better_zoo', 'wolf', 'tiger', 'duck')
		
		conn.scard('zoo')
		conn.smembers('zoo')
		conn.srem('zoo', 'lion')

		# Получение общих членов (и сохраение в новое множестово fowl_zoo):
		conn.sinter('fowl_zoo', 'zoo', 'better_zoo')
		conn.smembers('fowl_zoo')

		# Объединение:
			conn.sunion('zoo', 'better_zoo')
			conn.sunion('union_zoo','zoo', 'better_zoo')

		# Присутствуют в zoo, отсутствуют в better zoo:
			conn.sdiff('zoo','better_zoo')
			conn.sdiffstore('zoo_sale','zoo','better_zoo')

"""
		Упорядоченные множества (z)
		
		Набор уникальных значений, связанных с дробным счетчиком.
		Можно получать доступ к элементу по значению или счетчику

		Применяются как:
			1) Списков лидеров
			2) Вторичных индексов
			3) Временных рядов, где отметки времени исп как счетчик 
	
"""

# Применяются в качестве временных рядов, где отметки времени исп как счетчик:
		
		import time
		now = time.time()

		conn.zadd('logins', 'smeagol', now)
		conn.zadd('logins', 'sauron', now+(5*60))
		conn.zadd('logins', 'bilbo', now+(24*60*60))

		# Каким прибыл bilbo:
		conn.zrank('logins','bilbo')

		# Когда это было
		conn.zscore('logins','bilbo')

		# Все гости:
			conn.zrange('logins', 0, -1)
			conn.zrange('logins', 0, -1, withscores=True)


"""
	Биты 

	Быстрый и эффективный способ обработки множества чисел.

	Если пользователи используют ID, то информация о посещаемости может быть проанализирована быстрее.

"""

	days = ['2020-11-10', '2020-11-12','2020-11-13']
	big_spender = 1089
	tire_kicker = 40459
	late_joiner = 550212

	# Дата - отдельный ключ, установим бит для пользователя в дату:
	conn.setbit(days[0], big_spender, 1)
	conn.setbit(days[0], tire_kicker, 1)

	conn.setbit(days[1], big_spender, 1)

	conn.setbit(days[2], big_spender, 1)
	conn.setbit(days[2], late_joiner, 1)

	# Счетчик ежедневных посещений за 3 дня: 
	for day in days: 
			conn.bitcount(day)

	# Посещал ли сайт пользователь в заданыей день
	conn.getbit(days[1], tire_kicker)

	# Сколько пользователей посещает сайт каждый день
	conn.bitop('and','everyday', *days)
	conn.bitcount('everyday')
	conn.getbit('everyday', big_spender)

	# Сколько уникальных пользователей посетили сайт за 3 дня:
	conn.bitop('or', 'alldays', *days)
	conn.bitcount('alldays')

"""
	Кэши и истечение срока действия

	По умолчанию срок жизни у кэша бескнечность, но мы можем установить конечное время
	expire() - ичтечет через определенное время
	expireat() - истечет в заданное время по UNIX

"""

	import time
	key = 'now you see it'
	conn.set(key, 'but not for long')
	conn.expire(key,5)
	conn.ttl(key)
	conn.get(key)
	time.sleep(6)
	conn.get(key)