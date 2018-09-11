#Python variable Scope :
def outer_fun():
	a=10
	b=40
	print('a value is ',a)

	def inner_fun():
		b=20
		print('b value is ',b)
	inner_fun()
outer_fun()

#Global variable
print('------------')
def outer_fun():
	a=10
	global b
	b=40
	print('a value is ',a)

	def inner_fun():
		global b
		b=20
		print('b value is ',b)
	inner_fun()
	print('b value is ',b)
outer_fun()
