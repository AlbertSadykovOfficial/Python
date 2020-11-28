
"""
		
		Реляционные базы данных (Relation - отношения) - показывают отношения между различными типами данных.

"""

"""
		SQL - Structured Query Lenguage

		Язык структурированных запросов. 
		Суть: Пишем то, что хотим найти, а не как это найти.

		Категории SQL:
			DDL(Data Definition Language, язык определения данных) - работа с хранилищами данных (Таблицы, БД)
			DML(Data Manipulation Language, язык манипулированя данными) - работа непосредсвенно с данными 

"""

"""
	DB-API

	Стандартный API в Python, предназначенный для получения доступа к реляционным БД.
	API обеспечивает совместимость с разными ипами SQL.

		Основыне функции:
			connect() - Соединение с БД.
			cursor() - создание объекта, предназначенного для работы с запросами.
			execute() executemany() - запуск команд (одна, много)
			fetchone(), fetchmany(), fetchall() - получения результатов работы ф-ции execute

"""

"""
	SQLite (стандартная библиотека Pythn)

	Легковесная, хранит БД в обчных файлах --> портативна. 
	Не такая мощная как MySQL и PostgreSQL.
	Браузеры, смартфоны исп SQLite как встроенную БД.

	Запуск производится с исп ф-ции connect(), можно для тестов создать ее только в память (:memory)
	
"""

		import sqlite3
		conn = sqlite3.connect('enterprise.db')
		curs = conn.cursor()
		curs.execute('''CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)''')
		curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
		curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')
		# Добавить данные через заполнитель
		ins = 'INSERT INTO zoo (critter, count, damage) VALUES(?,?,?)'
		curs.execute(ins, ('weasel', 1, 2000.0))

"""
	MySQL 

		В отличие от SQLite является полноценной реляционная БД.
		В Python 3 еще не завезли, нужно устанавливать драйверы:
			+ MySQL Connector (http://bit.ly/mysql-cpdg)   пакет PyPi: mysql-connector-python Импорт: mysql.connector 
			+ PYMySQL (https://github.com/petehunt/PyMySQL)пакет PyPi: pymysql Импорт: pymysql
			+ oursql (http://pythonhosted.org/oursql/)     пакет PyPi: oursql Импорт: oursql  Примечание: требуется наличие клиентской библиотеки  MYSQL C

"""

"""
	PostgreSQL

		Более продвинута, чем MySQL.

		Драйверы для доступа к ней в Python 3:
			+ psycopg2 (http://initd.org/psycopg/) пакет PyPi: psycopg2 Импорт: psycopg2  Примечание: Необходим pg_config из клиентских инструментов PostgreSQL
			+ py-postgresql (http://python.projects.pgfoundry.org/) пакет PyPi: py-postgresql Импорт: postgresql
"""

"""
	SQLAlchemy

		Библиотека для работы с разными БД, предназначенная для минимизации различия диалектов разных БД.
			
			Уровни использования SQLAlchemy:
				+ Пулы - самый нищкий ур-нь (похож на DB-API). Работает с пулами соединений к БД.
				+ SQL
				+ ORM - связвает код приложений с реляционными структурами данных.

		Устанока (Linux):
			pip install sqlalchemy
		
		SQLAlchemy работает с драйверами БД, они импортируются при соединении:
			dialect + driver ://user:password@host:port/dbname 

				Параметры:
				dialect - тип БД
				driver - драйвер, который будем исп для этой БД.

				Диалект 		| Драйвер
				sqlite 			| pysqlite
				mysql   		| mysqlconnector
				postgresql 	| pypostgresql


		1) Уровень Движка (похоже на метод SQLite):
				import sqlalchemy as sa
				conn = sa.create_engine('sqlite://') # или sqlite:///:memory

				conn.execute('''CREATE TABLE zoo 
												(critter VARCHAR(20) PRIMARY KEY, 
												count INT, 
												damages FLOAT)'''
												) # Вернет объект ResultProxy
				
				ins = 'INSERT INTO zoo (critter, count, damage) VALUES(?,?,?)'
				conn.execute(ins, ('weasel', 1, 2000.0))

				rows = conn.execute('SELECT * FROM zoo')
				print(rows)
				for row in rows: print(row)


		2) Язык выражений SQL
				import sqlalchemy as sa
				conn = sa.create_engine('sqlite://')

				meta = sa.MetaData()
				zoo = sa.Table('zoo', meta,
												sa.Column('critter', sa.String, primary_key=True),
												sa.Column('count', sa.Integer),
												sa.Column('damages', sa.Float)
												)

				mata.create_all(conn)

				conn.execute(zoo.insert(('bear', 2, 1000.0)))

				result = conn.execute(zoo.select())
				rows = result.fetchall()
				print(rows)

		3) The Object-Relational Mapper

				import sqlalchemy as sa
				from sqlalchemy.ext.declarative import declarative_base

				conn = sa.create_engine('sqlite:///zoo.db')

				Base = declarative_base()
				class Zoo(Base):
						__tablename__ = 'zoo'
						critter = sa.Column('critter', sa.String, primary_key=True)
						count   = sa.Column('count', sa.Integer)
						damages	= sa.Column('damages', sa.Float)
						def __init__(self, critter, count, damages):
									self.critter = critter
									self.count   = count
									self.damages = damages
						def __repr__(self):
								return "<Zoo({},{},{})>".format(self.critter, self.count, self.damages)

				Base.metadata.create_all(conn)

				first  = Zoo('duck', 10, 0.0)
				second = Zoo('bear', 2, 1000.0)
				third  = Zoo('weasel',1,2000.0)
				first

				# Создать сессию
				from sqlalchemy.orm import sessionmaker
				Session = sessionmaker(bind=conn)
				session = Session()
				session.add(first)
				session.add_all([second, third])
				session.commit() # Завершить сессию
			
			ORM - абстракция, а абстракциям свойственны разрушения - утечки памяти.
			Нужно стараться использовать ORM реже и только в простых приложениях, но при этом можно испольховтаь и обычный (SQL)
			Или можно попробовать еще боле простой dataset на основе SQLAlchemy  и представляет собой простой ORM для хранилищ SQL, JSON,CSV.

"""
