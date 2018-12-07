class Person:
	def __init__(self,name,age):
		self.username=name
		self.userage=age
	def print_message(self):
		print(self.username+"----"+self.userage)
p = Person("张三","18")
p.print_message()