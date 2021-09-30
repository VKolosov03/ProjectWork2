class Rational:
	__numerator=1
	__denominator=1

	def __init__(self,numerator,denominator):
		i=1
		for i in range(numerator):
			if not numerator % i and not denominator % i:
				numerator=numerator/i
				denominator=denominator/i
		self.numerator=numerator
		self.denominator=denominator
	def show_standart(self):
		return (numerator+"/"+denominator)

	def show_float(self):
		return numerator/denominator

rati=Rational(2,4)
rati.show_standart()
rati.show_float()