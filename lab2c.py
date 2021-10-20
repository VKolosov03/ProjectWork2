class Product:

	def __init__(self,price,description,**dimensions):
		if not isinstance(price,float) and not isinstance(price,int):
			if price.isdigit():
				price=float(price)
			else:
				raise TypeError
		self.price=price
		self.description=description
		self.dimensions=dimensions

class Customer:

	def __init__(self,surname,name,patronymic,mobile_phone):
		self.surname=surname
		self.name=name
		self.patronymic=patronymic
		self.mobile_phone=mobile_phone

class Order:

	def __init__(self):
		self.total_value=0
		self.products_data=self.customer_data=''

	def show_data(self,customer,**products):
		self.customer_data=str(customer.surname)+','+str(customer.name)+','+str(customer.patronymic)+','+str(customer.mobile_phone)
		for key_products in products:
			self.products_data=self.products_data+str(products[key_products].price)+','+str(products[key_products].description)
			for key_dimensions in products[key_products].dimensions:
				self.products_data=self.products_data+','+str(products[key_products].dimensions[key_dimensions])
			self.products_data=self.products_data+'\n'
		return self.customer_data+'\n'+self.products_data

	def show_value(self,**products):
		for key_products in products:
			self.total_value=self.total_value+products[key_products].price
		return str(self.total_value)

smartphone=Product(7000,'New Samsung model',length=16,weight=0.5,size='16 inches')
apples=Product('100','Bunch of red apples',length=3,weight=2,size='50 of these things')
book=Product(350.57,'Last Harry Potter chapter',length=30,weight='1.35',size='300 pages')
hat=Product(555,'Just a winter hat',length=15,weight=0.333,size='L')
first_customer=Customer('Kolosov','VLadislav','Dmytrovych',1234567890)
second_customer=Customer('Sardaryan','Arsen','Artakovych','1234567890')
first_order=Order()
second_order=Order()
print('Info: '+first_order.show_data(first_customer,first_product=smartphone,second_product=apples,third_product=hat)+
	'\nTotal Value: '+first_order.show_value(first_product=smartphone,second_product=apples,third_product=hat)+'\n')
print('Info: '+second_order.show_data(second_customer,first_product=smartphone,second_product=book)+
	'\nTotal Value: '+second_order.show_value(first_product=smartphone,second_product=book))