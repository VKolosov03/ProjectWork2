class Rational:

	def __init__(self,numerator,denominator):
		if denominator!=0 and type(numerator)==int and type(denominator)==int:
			i=1
			while i <= numerator or i<= denominator:
				if not numerator % i and not denominator % i:
					numerator=numerator/i
					denominator=denominator/i
					i=1
				i=i+1
			self.numerator=int(numerator)
			self.denominator=int(denominator)
		else:
			self.numerator=1
			self.denominator=1
	def show_standart(self):
		return str(self.numerator)+'/'+str(self.denominator)

	def show_float(self):
		return self.numerator/self.denominator

rati=Rational(20,0)
print(rati.show_standart())
print(rati.show_float())