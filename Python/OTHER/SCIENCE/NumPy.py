"""

		NumPy

			NumPy был написан по аналогии с языком FORTRAN на C, что дает высокую скорость работы.

			Скачать: http://www.scipy.org/scipylib/download.html

			Основная структура данных NumPy - многомерный массив ndarray (все переменные должны иметь ожинаковый тип). 

"""
		import numpy as np

		# Создание массива с помощью array()
				b = np.array([2,3,45,6])
				b.ndim # ранг массива
				b.size # Общее число знаений

		# Создание массива с помощью arange()
				a = np.arange(10)
				b = np.arange(2.0, 9.8, 0.3)
		# Создание массива с помощью ones() и random()
				a = np.zeros((3))
				b = np.zeros((2,4)) # 2 строки по 4 эл-ты

				k = np.ones((3,5))

		# Изменить форму массива reshape():
				a = np.arange(10)
				a = a.reshape(5,2) # 5 строк по 2 эл-та
				# Или
				a.shape = (2,5)				

		# Получить эл-т:
				a[1,2]
				a[0, 2:]
				a[-1, :3]

		# Присвоение значения более, чем 1 эл-ту:
				a[:, 2:4] = 1000

		# Математика массивов
				a = arange(4)
				a *= 3
				a = zeros((2,5)) + 17.0

		# Линейная алгебра:
				# 4x + 5y = 20
				#  x + 2y = 13
				coeff = np.array([4,5], [1,2])
				depen = np.array([20,13])
				answer = np.linalg.solve(coeff,depen)

				# Проверка:
						product = np.dot(coeff, answer) # Скалярное произведение массивов
						np.allclose(product, depen) # Являются массивы приблизительно равными
