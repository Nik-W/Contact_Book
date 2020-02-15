#todo: 
#добавление функционала, найти какой
#выбор языка. все тексты хранить в отдельном файле, сохранять какой язык будет в файл, а менять его внутренней настройкой
#отлов ошибок
#расширение полей класса
#м.б. красивый интерфейс с помощью библиотек расскраски 
#документирование функций
#одинаковые части кода в функицю
#основное тело программы в Класс!!!!!
#пролистать книгу для поиска ещё задач

class Contact:
	def __init__(self, FirstName, LastName, Telephone, Address):
		'''Инициализация данных контакта'''
		self.FirstName = FirstName
		self.LastName = LastName
		self.Telephone = Telephone
		self.Address = Address
	def __repr__(self):
		'''Приведение объекта к строковому типу + формат вывода'''
		return("{} {} - Тел.: {} \n\tАдресс: {}".format(self.FirstName,\
			self.LastName,self.Telephone,self.Address) + \
		   "\n*-----------------------------------------------------------*")

#'''
c1 = Contact("Иван","Иванов","12-23-34","ул. Ленина, 14")
c2 = Contact("Пётр","Максимов","23-34-45","ул. Радищева, 10")
c3 = Contact("Семён","Степанов","11-22-33","ул. Ленина, 26")
c4 = Contact("Василий","Игорев","8-800-555-35-35","ул. Дубровинского, 5")
c5 = Contact("Иван","Зимов","112","ул. Маяковского, 44")
Book = [c1,c2,c3,c4,c5] #тестовый
#'''
#Book = [] #основной

Interface = "Адресная книга\n\tП - просмотр\n\tИ - искать\n\t\
Д - добавить\n\tУ - удалить\n\tВ - выход"

def SearchContact(Book, Search):
	'''Получение словаря найденных контактов.
	
	Получает список контактов и слово поиска, возвращает словарь
	с ключём - счётчик и значением - контакт.'''
	Counter = 0
	SearchBook = {}
	for contact in Book:
		if  contact.FirstName.lower().find(Search.lower()) != -1:
			Counter += 1
			SearchBook[Counter] = contact
		elif contact.LastName.lower().find(Search.lower()) != -1:
			Counter += 1
			SearchBook[Counter] = contact
		elif contact.Telephone.lower().find(Search.lower()) != -1:
			Counter += 1
			SearchBook[Counter] = contact
		elif contact.Address.lower().find(Search.lower()) != -1:
			Counter += 1
			SearchBook[Counter] = contact
	print("Результаты поиска: ")
	for key, value in SearchBook.items():
		print("{}. {}".format(key, value))
	return SearchBook

print(Interface)
Comand = input("Команда: ")
while Comand != 'В':
	
	if Comand == 'П': #добавить сортировку перед выводом
		for counter, value in enumerate(Book, 1):
			print("{}. {}".format(counter, value))
	
	elif Comand == 'И':
		Search = input("Введите известные данные о контакте: ")
		SearchBook = SearchContact(Book, Search)

	elif Comand == 'Д':
		FN = input("\tИмя: ")
		LN = input("\tФамилия: ")
		T = input("\tТелефон: ")
		A = input("\tАдрес: ")
		contact = Contact(FN,LN,T,A)
		Book.append(contact)

	elif Comand == 'У':
		Delete = input("Введите известные данные об удаляемом контакте: ")
		DeleteBook = SearchContact(Book, Delete)
		DeleteInd = input("Введите номер удаляемого контакта: ")
		DeleteObj = DeleteBook[int(DeleteInd)]
		Book.remove(DeleteObj)
		

	else:
		print("Несуществующая команда!")
		Comand = input("Команда: ")
		continue

	Comand = input("Команда: ")

else:
	exit(0) #проверить

	

