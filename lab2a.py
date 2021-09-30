class Rectangle:
	width=0
	length=0

	def perimeter(self):
		return 2*(self.width+self.length)

	def area(self):
		return self.width*self.length

	def setter(self):
		error_index=1
		while error_index or self.width<0 or self.length <0 or self.length >20 or self.width>20:
			try:
				error_index=0
				self.width = float(input("Width of rectangle: "))
				self.length = float(input("Length of rectangle: "))
			except ValueError:
				error_index=1

	def getter(self):
		return (self.width,self.length)

square=Rectangle()

square.setter()
print("width and length: ",square.getter(),"\nperimeter: ",square.perimeter(),"\narea: ",square.area())


