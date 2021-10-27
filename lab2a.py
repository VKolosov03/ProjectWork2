MIN_VALUE=0
MAX_VALUE=20

class Rectangle:

	def __init__(self,width=1,length=1):
		self.__width = width
		self.__length = length

	def perimeter(self):
		return 2*(self.__width+self.__length)

	def area(self):
		return self.__width*self.__length

	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self,width):
		if not isinstance(width,float) and not isinstance(width,int):
			raise TypeError
		if width<MIN_VALUE or width >MAX_VALUE:
			raise RuntimeError
		self.__width = width

	@property
	def length(self):
		return self.__length

	@length.setter
	def length(self,length):
		if not isinstance(length,float) and not isinstance(length,int):
			raise TypeError
		if length<MIN_VALUE or length >MAX_VALUE:
			raise RuntimeError
		self.__length = length

square=Rectangle()
square.width=2
square.length=1
print("width and length:",str(square.width)+' '+str(square.length),"\nperimeter: ",square.perimeter(),"\narea: ",square.area())

