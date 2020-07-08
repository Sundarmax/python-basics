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

test = Department("sundar","21","934849834")
test.getStudentName()

