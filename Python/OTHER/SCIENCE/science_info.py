"""

		Python в науке 

			Обработка просто статистики: Модуль statistics (Начиная с Python 3.4 встроен)
			
			Перемножене матриц происходит за счет символа (@) (Начиная с Python 3.5)
		
		Библиотеки (общие):
			NumPy - математичсеская библиотека
			SciPy - расширенная библиотека, основанная на NumPy вкл:(интерполяцию, лин регреию, статистику и тд.)
			SciKit - Группа пакетов, основанных на SciPy, спеиалихируется на машинном обучении
			IPython- Удобная библиотека с улучшенным интерпретатором и возможностью ведения Блокнота (Отчета)
			Pandas - пакет для интерактивного анализа данных Книга: (Python for Data Analysis: Data Wrangling with Pandas, NumPy and IPython) 
		
		Python в научных областях:
				Общие:
						- Вычисления Python в науке и инженерном деле (http://bit.ly/py-comp-sci)
						- Интерактивный курс Python для ученных (http://bit.ly/pyforsci)
				Физика:
						- Физические вычисления (http://bit.ly/pyforsci)
				Биология и медицина
						- Python для биологов (http://pythonforbiologists.com)
						- Neuroimaging с помощью Python (http://nipy.org/)

"""

"""
			Стандартные математические ф-ции библиотеки math:

"""
			import math
			math.hypot(3, 4) # Гипотенуза = 5
			math.radians(180) # Перевод в радианы = 3.14..
			math.degrees(math.pi) # 180
			
		# Поддерживается раьоты с комплексными числами:
			(7 + 1j)* 1j

"""

	Точное значение чисел decimal

			Компьютеры изначально разрабатывались для бинарной математики 
			Числа, не кратные степени двойки могут ыть посчитаны неправильно:
				x = 10/3
				x
				3.333333335

			Чтобы записывать числа с желаемым уровнем точности, следует исп decimal
"""

		from decimal import Decimal
		price = Decimal('19.99')
		tax = Decimal('0.06')
		total = price + (price * tax)
		total

		penny = Decimal('0.01') 
		total.quantize(penny) # Привести к нудной точности


"""

	Рациональные числа 

		Модуль fraction

"""

		from fractions import Fraction
		Fraction(1,3)*Fraction(2,3)
		Fraction(1.0/3.0)
		fractions.gcd(24,16) #8 Наибольший общий делитель

