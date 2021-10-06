import sys

class File:
	number_of_charachters=number_of_words=number_of_sentences=0

	def __init__(self,file):
		try:
			self.open_file=open(file, 'r')
		except (IOError,FileNotFoundError):
			print('Unable to open this file')
			self.open_file=close()
			sys.exit()
		self.text_file=self.open_file.read()

	def count_charachters(self):
		self.number_of_charachters=len(self.text_file)
		return self.number_of_charachters

	def count_words(self):
		self.text_file=self.text_file.replace(' , ',', ')
		self.text_file=self.text_file.replace(' . ','. ')
		self.text_file=self.text_file.replace(' ; ','; ')
		self.text_file=self.text_file.replace(' - ','- ')
		self.text_file=self.text_file.replace(' ! ','! ')
		self.text_file=self.text_file.replace(' ? ','? ')
		self.text_file=self.text_file.replace(' ... ','... ')
		self.number_of_words=len(self.text_file.split())
		return self.number_of_words

	def count_sentences(self):
		punctuation='.!?'
		recurring_symbol=''
		for line in self.text_file:
			if line in punctuation:
				if line!= recurring_symbol:
					self.number_of_sentences+=1
			recurring_symbol=line
		return self.number_of_sentences

statistic=File('words.txt')
print('Number of charachters: ',statistic.count_charachters(),'\nNumber of words: ',
	statistic.count_words(),'\nNumber of sentences: ',statistic.count_sentences())