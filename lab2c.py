class Product:

	def __init__(self,price,description,**dimensions):
		self.price=price
		self.description=description
		self.dimensions=dimensions

	def __str__(self):
		return str(self.price)+','+self.description+','+','.join('='.join(str(item) for item in group) 
			for group in self.dimensions.items())

	@property
	def price(self):
		return self.__price

	@price.setter
	def price(self,price):
		if not isinstance(price,float) and not isinstance(price,int):
			if price.isdigit():
				price=float(price)
			else:
				raise TypeError
		self.__price = price

	@property
	def description(self):
		return self.__description

	@description.setter
	def description(self,description):
		if not isinstance(description,str):
			raise TypeError
		self.__description = description

	@property
	def dimensions(self):
		return self.__dimensions

	@dimensions.setter
	def dimensions(self,dimensions):
		if not isinstance(dimensions,dict):
			raise TypeError
		self.__dimensions = dimensions

class Customer:

	def __init__(self,surname,name,patronymic,mobile_phone):
		self.surname=surname
		self.name=name
		self.patronymic=patronymic
		self.mobile_phone=mobile_phone

	def __str__(self):
		return self.surname+','+self.name+','+self.patronymic+','+str(self.mobile_phone)

	@property
	def surname(self):
		return self.__surname

	@surname.setter
	def surname(self,surname):
		if not isinstance(surname,str):
			raise TypeError
		self.__surname = surname

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self,name):
		if not isinstance(name,str):
			raise TypeError
		self.__name = name

	@property
	def patronymic(self):
		return self.__patronymic

	@patronymic.setter
	def patronymic(self,patronymic):
		if not isinstance(patronymic,str):
			raise TypeError
		self.__patronymic = patronymic

	@property
	def mobile_phone(self):
		return self.__mobile_phone

	@mobile_phone.setter
	def mobile_phone(self,mobile_phone):
		if not isinstance(mobile_phone,int):
			if mobile_phone.isdigit():
				mobile_phone=int(mobile_phone)
			else:
				raise TypeError
		self.__mobile_phone = mobile_phone

class Order:

	def __init__(self,customer,**products):
		self.customer=customer
		self.products=products
		self.total_value=0

	def __str__(self):
		return str(self.customer)+'\n'+'\n'.join(str(key) for key in self.products.values())

	@property
	def customer(self):
		return self.__customer

	@customer.setter
	def customer(self, customer):
		if not isinstance(customer,Customer):
			raise TypeError
		self.__customer = customer

	@property
	def products(self):
		return self.__products

	@products.setter
	def products(self, products):
		if not isinstance(products, dict):
			raise TypeError
		self.__products = products

	def show_value(self):
		for key_products in self.products:
			self.total_value=self.total_value+self.products[key_products].price
		return self.total_value

smartphone=Product(7000,'New Samsung model',length=16,weight=0.5,size='16 inches')
apples=Product('100','Bunch of red apples',length=3,weight=2,size='50 of these things')
book=Product(350.57,'Last Harry Potter chapter',length=30,weight='1.35',size='300 pages')
hat=Product(555,'Just a winter hat',length=15,weight=0.333,size='L')
first_customer=Customer('Kolosov','VLadislav','Dmytrovych',1234567890)
second_customer=Customer('Sardaryan','Arsen','Artakovych','1234567890')
first_order=Order(first_customer,first_product=smartphone,second_product=apples,third_product=hat)
second_order=Order(second_customer,first_product=smartphone,second_product=book)
print('Info:\n'+str(first_order)+
	'\nTotal Value: '+str(first_order.show_value())+'\n')
print('Info:\n'+str(second_order)+
	'\nTotal Value: '+str(second_order.show_value()))