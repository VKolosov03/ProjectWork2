class Rectangle:

	def __init__(self):
		self.width=self.length=0

	def perimeter(self):
		return 2*(self.width+self.length)

	def area(self):
		return self.width*self.length

	def setter(self,width,length):
		if not isinstance(width,float) or not isinstance(length,float):
			raise TypeError
		if width<0 or length <0 or length >20 or width>20:
			raise RuntimeError
		self.width = width
		self.length = length

	def getter(self):
		return (self.width,self.length)

square=Rectangle()

square.setter(0.1,2.)
print("width and length: ",square.getter(),"\nperimeter: ",square.perimeter(),"\narea: ",square.area())

