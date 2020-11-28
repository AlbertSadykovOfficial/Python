"""
	Конструкии try except
		Нужны для того, чтобы перехватить ошибку в месте, где это очень ожидаемо
		Пример: пользователь вышел за пределы массива, это должно положить программу,
						но except перехватит ошибку и не позволит это сделать
	
	Любое исключение - потомок класса Exception 

"""

short_list = [1,2,3]
position = 5
try:
		short_list[position]
except:
		print('Выбери значение от 0, до ', len(short_list)-1, 'ты выбрал:', position)


			# Проверки на особые исключения и общие исключения:
				try:
							short_list[position]
				except IndexError as err:
							print('Bad Index:', position)
				except Exception as other
								print("It's not Bad Index Error, somthing else broke:", other)


			# Создать свое исключение:
				class UppercaseException(Exception):
							pass # Просит родительский класс Exception выяснить в чем проблема

				word = 'HELLO'
				if word.isupper(): raise UppercaseException(word)