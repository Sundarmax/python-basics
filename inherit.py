# Python Inheritance 
class Collection:
	Vehicles = []
	def __init__(self,Vehicles):
		self.Vehicles=Vehicles
class Vehicles:
	def __init__(self,fname,lname,mobile):
		self.fname=fname
		self.lname=lname
		self.mob=mobile
	def Vehicle_list(self):
		print('Bike\nCars\nBuses\nTrucks')
class Bike(Vehicles):
	def specify(self,brand,model):
		print('Bike Owner name is {}{}'.format(self.fname,self.lname))
		print('Bike brand is {}, Bike model is {}'.format(brand,model))
class Car(Vehicles):
	def specify(self,brand,model):
		print('Car Owner name is {}{}'.format(self.fname,self.lname))
		print('Bike brand is {}, Bike model No is {}'.format(brand,model))

Vehicles_collection = [
	Car('Sundar','Rajan','9500490424'),
	Bike('Rose','Mary','125472525')
]
#obj1=Vehicles('Sundar','Rajan','9500490424')
obj1 = Car('Sundar','Rajan','9500490424')
obj1.specify('Swift','S21')

obj2 = Bike('Rose','Mary','125472525')
obj2.specify('Suzuki','MAx100')
obj2.Vehicle_list()
print (isinstance(obj1,Vehicles))

#instantiate the vehicle collection class 
obj_collection=Collection(Vehicles_collection)
print(len(obj_collection.Vehicles))
for item in obj_collection.Vehicles:
	print('{}-{}-{}'.format(item.fname,item.lname,item.mob))
#print(' i have {} Vehicles. '.format(len(obj_collection.Vehicles))
