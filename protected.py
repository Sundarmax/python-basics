class StudentProfile:
    # Protected member variables.
    _name = None
    _age  = None
    _phone = None
    
    def __init__(self,name,age,phone):
        '''constructor'''
        self._name = name
        self._age  = age
        self._phone = phone

    # Protected member function
    def _getStudentProfile(self):
        print("Student Name ",self._name)
        print("Student Age ",self._age)
        print("Studnet Phone",self._phone)


class Department(StudentProfile):

    def __init__(self,name,age,phone):
        super().__init__(name,age,phone)

    # accessing protected data members of super class 
    def getStudentName(self):
        print(self._name)
    # accessing protected member functions of super class 
        self._getStudentProfile()

"""
 Desc:
  Python program to demonstrate the diamond problem
  (a.k.a. Multiple Inheritance)
"""

# Parent class 1
class TeamMember(object):                   
   def __init__(self, name, uid): 
      self.name = name 
      self.uid = uid 
  
# Parent class 2
class Worker(object):                 
   def __init__(self, pay, jobtitle): 
      self.pay = pay 
      self.jobtitle = jobtitle 
  
# Deriving a child class from the two parent classes
class TeamLeader(TeamMember, Worker):         
   def __init__(self, name, uid, pay, jobtitle, exp): 
      self.exp = exp 
      TeamMember.__init__(self, name, uid) 
      Worker.__init__(self, pay, jobtitle)
      print("Name: {}, Pay: {}, Exp: {}".format(self.name, self.pay, self.exp))

TL = TeamLeader('Jake', 10001, 250000, 'Scrum Master', 5)
#test = Department("sundar","21","934849834")
#test.getStudentName()

