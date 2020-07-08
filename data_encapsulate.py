class Person:
  
  def __init__(self): 
    self.name = 'Manjula'
    self.__lastname = 'Dube'
    
  def PrintName(self):
    return self.name +' ' + self.__lastname
  
  def __LastName(self):
      print('hi this is sundar')

#Outside class    
P = Person()
print(P.name)
print(P.PrintName())
print(P.__LastName)
# print(P.__lastname)
#AttributeError: 'Person' object has no attribute '__lastname'
#print(P.__Person__LastName())