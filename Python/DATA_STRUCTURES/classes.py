"""

	 Классы

"""


# Создать класс:
	class Person():
		"""docstring for ClassName"""
		def __init__(self, name):
			self.name = name

		def exclaim(self):
			print("I'm Person, My name is ", self.name)

	hunter = Person('Elmer Fudd')


# Наследование:

	class BadPerson(Person):
		# Перегрузочный метод с добавлением email
		def __init__(self, name, email):
			super().__init__(name) # Приемущество super() в том, что если мы изменим родительский класс, то этот изменится автоматически
			self.email = email  

		def exclaim(self):
			print("I'm Bad person, My name is ", self.name)

		def why_you_bad(self):
			print('i like to kill people')
			

"""
  Геттеры и сеттеры

  В Python все элеметы класса открыты, для имитации закрытия следет использовать геттеры и сеттеры  

"""
# Метод 1 (Параметрически)
	class Duck():

		def __init__(self, input_name):
				self.hidden_name = input_name

		def get_name(self):
				print('Inside the getter')
				return self.hidden_name
		
		def set_name(self, input_name):
				print('Inside the setter')
				self.hidden_name = input_name

		name = property(get_name, set_name) # Функция property задает методы Геттер и сеттер

# Метод 2 (декаратором)
	class Duck():

		def __init__(self, input_name):
				self.hidden_name = input_name

		@property
		def name(self):
				print('Inside the getter')
				return self.hidden_name

		@name.setter
		def set_name(self, input_name):
				print('Inside the setter')
				self.hidden_name = input_name

"""

Искажение имен для безопасности.

	Python предлагает соглашение по именованию для атрибутов, которые не должны быть видимы за пределами класса:
	Имена начинаются с 2х нижних подчеркиваний
	name -> __name
	ранее, использовалось name->hidden_name 

"""
	class Duck():

		def __init__(self, input_name):
				self.__name = input_name

		def get_name(self):
				print('Inside the getter')
				return self.__name
		
		def set_name(self, input_name):
				print('Inside the setter')
				self.__name = input_name

		# Пример 
		fowl = Duck("Donald")
		fowl.__name # Ошибка
		fowl._Duck__name # Так моно достучаться


"""

	Python имеет Методы ЭКЗАМПЛЯРА класса и Методы КЛАССА, Статические методы
	Методы Экземпляра класса - относятся непосредственно к объекту класса
	Методы КЛАССА влияют на класс целиком (на все объекты)
	Статические методы - методы, не требующие создания экземпляра класса, это обычные функции, которые по какой-то причине логичнее засунуть в класс, чем создавать их обособленно

""" 

	class A():
			count = 0
			def __init__(self):
					A.count += 1
			@classmethod
			def kids(cls): # словов cls заменяет слово зарезервированное слово class
					print("A has ", cls.count, "objects")
			
			@staticmethod
			def some_phrase():
					print('Hello, you can use this method')

"""

Полиморфизм - спосбоность объекта иметь разную реализацию 

"""
	class Quote():
			def __init__(self, person, words):
				self.person = person
				self.words = words
			def who(self):
				return self.person
			def says(self):
				return self.words + '.'

	class QuestionQuote(Quote):
			def says(self):
				return self.words + '?'

	class ExclamationQuote(Quote):
			def says(self):
				return self.words + '!'


"""

	Специальные методы (__method__) (http://bit.ly/pydocs-smn)

	Cущность этих методов в том, что они основаны на часто используемых методах
	и позволяют короче и понятнее вызывать эти функции

	Пример:
	equal -> __eq__(self,other) => self == other
	noteq -> __ne__(self,other) => self != other
	greater -> __gt__(self,other) => self > other
	+
	__str__(self) => str(self)
	__len__(self) => len(self)
"""

# Пример написания обычного кода своими руками (+ вызов)
	class Word():
		def __init__(self,text):
				self.text = text

		def equals(self,word2):
				return self.text.lower() == word2.text.lower()

	first = Word('Ha')
	second = Word('HA')
	first.equals(second)

# Пример использования специальных методов:
	class Word():
		def __init__(self,text):
				self.text = text

		def __eq__(self,word2):
				return self.text.lower() == word2.text.lower()

		def __str__(self):
				return self.text

	first = Word('Ha')
	second = Word('HA')
	first == second

	print(first)

"""
	
	Именованные кортежи - подкласс кортежей с помощью оторых можно получить доступ к значению по имени
	Стоить помнить: Словарь,список,кортеж проще и быстрее модулей, а модули проще и быстрее, чем классы.
									-> Отсюда: Стремимся использовать более простые структуры данных

	+ Именованные кортежи не поддерживаются Python автоматически, нужно загружать отдельный модуль
	+ Поля в именованный кортеж не добавляются
"""
	 from collections import namedtuple
	 Duck = namedtuple('Duck', 'Bill tail')
	 duck = Duck('wide orange', 'long')
	 duck
	 duck.bill
	 duck.tail

	 parts = {'bill': 'wide orange', 'tail': 'long'}
	 duck2 = Duck(**parts) # **parts - извлекает ключи и значения parts и передает их Duck
	 duck2