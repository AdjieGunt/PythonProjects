class Employee:

	"""docstring for Employee"""
	
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last =  last
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

emp_1 = Employee('Adjie', 'Guntoro', 500000)

print(emp_1.fullname())

