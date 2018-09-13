#classes & objects 
# Getter & Setter
class person:
	state="KR"
	def __init__(self,name,addr,mob):
		self.name=name
		self.addr=addr
		self.__mob=mob
	def profile(self):
		print('Welcome to {} ORG'.format(self.name))
		print('Address is {}'.format(self.addr))
		print('Mobile No is {}'.format(self.__mob))
	def contact(self):
		return 'contact address is ',format(self.addr)
	def mobN(self):
		return self.__mob
	def set_mob(self,mob):
		self.__mob=mob
	@classmethod
	def stateName(cls,state):
		cls.state=state
		return cls.state

obj1=person("CIT","CBE","15248752")
obj1.addr="MDU"
#print(obj1.contact())
#obj1.mob="12456" it can't work '' protected
obj1.set_mob('9500490424') 
obj1.profile()
print(person.stateName("TN"))
print(person.state)