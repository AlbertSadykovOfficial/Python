"""

	Каленадри и часы
	
		Всегда стараемся использовать UTC ЗИМНЕЕ время, НЕ летнее.

		Дополнительные сторонние модули:
			arrow
			dateutil
			iso8601
			fleming
"""
	
	# Проверить является ли год високосным:
		import calendar
		calendar.isleap(1900)
		calendar.isleap(1996)


"""
	
	Модуль datetime

		Основные объекты:
			-date для годов, месяцев, дней (min: year=1, month=1, day=1; max: year=9999, month=12, day=31)
			-time для часов, минут, секунд, долей секнуд.
			-dateime для даты и времени одновеменно
			-timedelta для интервалов даты и времени

"""
# Объект date

	from datetime import date
	halloween = date(2014,10,31)
	halloween
	
	halloween.day
	halloween.month
	halloween.year
	
	halloween.isoformat() # Вывод по международному стандарту ISO 8601

	# Генерация сегодняшней даты:
		now = date.today()

	# Добавить к объекту date временной интервал:
		one_day = timedelta(days=1)
		tomorrow = now + one_day
		now + 17*one_day


# Объект time
	
	from datetime import time
	noon = time(12,0,0)
	noon

	noon.hour
	noon.minute
	noon.second
	noon.microsecond


# Объект datetime

	from datetime import datetime
	now = datetime.now()
	now.month

	some_day = datetime(2014, 1, 2, 3, 4, 5, 6)
	some_day
	some_day.isoformat() # T - разделяет дату и время


# Объединение объектов date и time в datetime
	
	from datetime import datetime, date, time
	noon = time(12)
	this_day = date.today()
	noon_today = datetime.combine(this_day, noon)
	noon_today

	# Использовать объекты date и time из datetime
		noon_today.date()
		noon_today.time()



"""
	
	Модуль time

	epoch - Кол-во секнуд прошедших с полуночи 1 января 1970г (примерное время зарождения UNIX)
"""

	# Текущее время через epoch
		import time
		now = time.time()
		now

	# Преобразовать epoch в строку:
		time.ctime(now)

	# Время в текущем часовом поясе (struct_time):
		time.localtime(now)

	# Время в поясе UTC Гринвичу, Зулу) (struct_time):
		time.gmtime(now)

	# Преобразовать struct_time в epoch:
		tm = time.mktime(tm)


"""

 Читаем и записываем дату и время

 		На подоюие ctime() есть еще ф-ции преобразования даты в строки:
 			strftime() - ф-ция, использующая для вывода информаци спецификаторы формата:
 				%Y - Год (1900-...)
 				%d - сокращение для месяца (Янв)
 				a  - сокращение для дня (Вск)
 				и др...

"""

# Преобразование из даты в строку
	import time
	from datetime import date
	from datetime import time
	fmt = "It's %A, %B, %d, %Y, local time %I:%M:%S%p"
	
	t = time.localtime()
	t
	time.strftime(ftm, t)

	some_day = date(2014, 7, 4)
	some_day.strftime(fmt)

	some_time = time(10,35)
	some_time.strftime(fmt)

# Преобразование из строки в дату (Требуется точно совпадение ШАБЛОНУ!!!)
	import time
	fmt = "%Y-%m-%d"
	time.strptime("2012-01-29", fmt)

"""
		Локали

"""
# Название дат соотвествуют локали, чтобы поменять локаль (на немецкую, к примеру):
		local.setlocale(locale.LC_TIME, 'de_de')
		
# Получить названия всех локалей можно так(выведет все, лучше гуглить):
		names = locale.locale_alias.keys()
	
# Получить названия локалей, которые работают с методом setlocale:
		good_names = [name for name in names if len(name) == 5 and name[2] == '_']
		# Первые 5 результатов:
			good_names[:5]

# Получить все локали для Германии
		de = [name for name in names if name.startswith('de')]
		de