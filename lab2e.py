MIN_VALUE=0
MAX_VALUE=5

class Student:

	def __init__(self,surname,name,record_book_number,*grades):
		self.name=name
		self.surname=surname
		self.record_book_number=record_book_number
		self.grades=grades

	def __str__(self):
		return self.surname+', '+self.name+', '+str(self.record_book_number)+', grades:'+','.join(str(i) for i in
		 self.grades)+'; avarage score='+str(self.get_average_score())

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self,name):
		if not isinstance(name,str):
			raise TypeError
		self.__name = name

	@property
	def surname(self):
		return self.__surname

	@surname.setter
	def surname(self,surname):
		if not isinstance(surname,str):
			raise TypeError
		self.__surname = surname

	@property
	def record_book_number(self):
		return self.__record_book_number

	@record_book_number.setter
	def record_book_number(self,record_book_number):
		if not isinstance(record_book_number,int):
			if record_book_number.isdigit():
				record_book_number=int(record_book_number)
			else:
				raise TypeError
		if record_book_number<MIN_VALUE:
			raise RuntimeError
		self.__record_book_number = record_book_number

	@property
	def grades(self):
		return self.__grades

	@grades.setter
	def grades(self,grades):
		if not isinstance(grades,tuple):
				raise TypeError
		for i in range(len(grades)):
			if not isinstance(grades[i],float) and not isinstance(grades[i],int):
				if grades[i].isdigit():
					grades[i]=float(grades[i])
				else:
					raise TypeError
			if grades[i] < MIN_VALUE or grades[i] > MAX_VALUE:
				raise RuntimeError
		self.__grades = grades

	def get_average_score(self):
	""" returns student avarage grade """

		return sum(self.grades)/len(self.grades)

MIN_STUDENTS=5
MAX_STUDENTS=20

class Group:

	def __init__(self,*students):
		self.students=students
		self.best_students=[['','',0],['','',0],['','',0],['','',0],['','',0]]

	def __str__(self):
		return '\n'.join(str(i) for i in self.students)

	@property
	def students(self):
		return self.__students

	@students.setter
	def students(self,students):
		if not isinstance(students,tuple):
				raise TypeError
		if len(students)>MAX_STUDENTS and len(students)<MIN_STUDENTS:
			raise RuntimeError
		for i in range(len(students)):
			if not isinstance(students[i],Student):
				raise TypeError
			for j in range(len(students)):
				if (students[i].name==students[j].name and students[i].surname==students[j].surname or
				 students[i].record_book_number==students[j].record_book_number) and i!=j:
					raise RuntimeError
		self.__students = students

	def show_best_students(self):
	""" returns information about 5 best students that were sorted before """

		for i in range(len(self.students)):
			index=0
			previous_student=['','',0]
			for j in range(len(self.best_students)):
				if self.students[i].get_average_score()>self.best_students[j][2] and index==0:
					self.best_students[j], previous_student=previous_student,self.best_students[j]
					self.best_students[j][0]=self.students[i].surname
					self.best_students[j][1]=self.students[i].name
					self.best_students[j][2]=self.students[i].get_average_score()
					index=1
				elif index==1:
					self.best_students[j], previous_student=previous_student,self.best_students[j]
		return '\n'.join(','.join(str(item) for item in group) for group in self.best_students)+'\n'


student1 = Student("Kolos", "Vlad", 1, 1, 4, 4, 4, 5)
student2 = Student("Kolosov", "Vladik", "2", 5, 5, 5, 5, 5)
student3 = Student("Kol", "Vladislav", "3", 2, 4, 3, 4, 5)
student4 = Student("Kolos", "Slava", "4", 5, 5, 4, 2, 5)
student5 = Student("Kolosov", "Slavik", "5", 2, 3, 3, 2, 3)
student6 = Student("Kol", "Vyacheslav", "6", 5, 4, 3, 3, 4)
student7 = Student("Kolos", "Katia", "7", 5, 3, 3, 4, 5)
student8 = Student("Kolosov", "Kater", "8", 2, 3, 2, 1, 5)
student9 = Student("Kol", "Katerina", "9", 4, 2, 4, 4, 5)
student10 = Student("Kolos", "Diana", "10", 5, 3, 3, 4, 5)
student11 = Student("Kolosov", "Dionisis", "11", 5, 5, 5, 5, 5)
student12 = Student("Kol", "Diana", "12", 4, 3, 4, 4, 5)
student13 = Student("Kolos", "Dima", "13", 4, 4, 5, 2, 5)
student14 = Student("Kolosov", "Dima", "14", 4, 5, 3, 4, 5)
student15 = Student("Kol", "Dima", "15", 4, 4, 5, 4, 5)
student16 = Student("Kolos", "Maks", "16", 2, 4, 4, 4, 5)
student17 = Student("Kolosov", "Mask", "17", 3, 4, 4, 4, 5)
student18 = Student("Kol", "Maks", "18", 4, 4, 4, 4, 5)
student19 = Student("Kolos", "Vladik", "19", 4, 4, 5, 4, 5)
student20 = Student("Kolosov", "Vladislav", "20", 4, 4, 2, 4, 5)
student21 = Student("Kol", "Vlad", "21", 4, 4, 1, 4, 5)
student22 = Student("Kolos", "Emil", "22", 3, 3, 5, 4, 2)
group = Group(student1, student2, student3, student4, student5, student6, student7, student8, student9, student10, 
	student11, student12, student13, student14, student15, student16, student17, student18, student19, student20)
print("Top 5 students:\n"+group.show_best_students())
print("All students:\n"+str(group))