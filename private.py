class StudentProfile:
    # Private member variables.
    __name = None
    __age  = None
    __phone = None
    
    def __init__(self,name,age,phone):
        '''constructor'''
        self.__name = name
        self.__age  = age
        self.__phone = phone

    # Private member function
    def __getStudentProfile(self):
        print("Student Name ",self.__name)
        print("Student Age ",self.__age)
        print("Studnet Phone",self.__phone)
    
    # Public member function
    def accessPrivateFunction(self):
        self.__getStudentProfile()

test = StudentProfile("Sundar","26","1234567894")
test.accessPrivateFunction()