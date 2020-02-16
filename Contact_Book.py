#todo: 
#добавление функционала, найти какой
#выбор языка. Адаптация кода к английскому языку и тестирование
#отлов ошибок
#расширение полей класса
#м.б. красивый интерфейс с помощью библиотек расскраски 
#документирование функций
#одинаковые части кода в функицю
#основное тело программы в Класс!!!!! Пока не понял как
#пролистать книгу для поиска ещё задач
#запись в файл, кнопка Сейв и вопрос о сохранении при выходе
#добавить экран опций: смена языка, сохранение при добавлении или выходе, сортировка по..., 
import RuLang, EnLang
import pickle

class Contact:
	def __init__(self, FirstName, LastName, Telephone, Address):
		'''Инициализация данных контакта'''
		self.FirstName = FirstName
		self.LastName = LastName
		self.Telephone = Telephone
		self.Address = Address
	def __repr__(self):
		'''Приведение объекта к строковому типу + формат вывода'''
		return(Lang.reprT.format(self.FirstName,\
			self.LastName,self.Telephone,self.Address) + \
		   "\n*-----------------------------------------------------------*")

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
	print(Lang.ResultSearchT)
	for key, value in SearchBook.items():
		print("{}. {}".format(key, value))
	return SearchBook

#c1 = Contact("Иван","Иванов","12-23-34","ул. Ленина, 14")
#c2 = Contact("Пётр","Максимов","23-34-45","ул. Радищева, 10")
#c3 = Contact("Семён","Степанов","11-22-33","ул. Ленина, 26")
#c4 = Contact("Василий","Игорев","8-800-555-35-35","ул. Дубровинского, 5")
#c5 = Contact("Иван","Зимов","112","ул. Маяковского, 44")
#Book = [c1,c2,c3,c4,c5] #тестовый

#Book = [] #основной

Lang = RuLang

f = open('Contacts.data', 'rb')
Book = pickle.load(f) # загружаем объект из файла

print(Lang.InterfaceT)
Comand = input(Lang.ComandT)

while Comand != 'В':
	
	if Comand == 'П':	#вывод списка контактов
		Book = sorted(Book, key=lambda contact: contact.FirstName)
		for counter, value in enumerate(Book, 1):
			print("{}. {}".format(counter, value))
	
	elif Comand == 'И':		#поиск контактов
		Search = input(Lang.SearchT)
		SearchBook = SearchContact(Book, Search)

	elif Comand == 'Д':		#добавление контактов
		FN = input(Lang.FirstNameT)
		LN = input(Lang.LastNameT)
		T = input(Lang.TelephoneT)
		A = input(Lang.AddressT)
		contact = Contact(FN,LN,T,A)
		Book.append(contact)

	elif Comand == 'У':		#удаление контактов
		Delete = input(Lang.DeleteT)
		DeleteBook = SearchContact(Book, Delete)
		DeleteInd = input(Lang.DeleteIndT)
		DeleteObj = DeleteBook[int(DeleteInd)]
		Book.remove(DeleteObj)
		
	elif Comand == 'Я' or Comand == 'L':	#смена языка
		Switch = input(Lang.SwitchT)
		if Switch == 'ru':
			Lang = RuLang
		elif Switch == 'en':
			Lang = EnLang
		print(Lang.InterfaceT)

	elif Comand == 'С': #сохранение
		f = open('Contacts.data', 'wb')
		pickle.dump(Book, f)
		f.close()
		print(Lang.SaveT)

	else:	#ошибка введения команды
		print(Lang.ErrComandT)
		Comand = input(Lang.ComandT)
		continue

	Comand = input(Lang.ComandT)

else:
	exit() #проверить


	

