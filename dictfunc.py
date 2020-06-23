def DictionaryMethods():
    student = {}
    # add key value pair
    student['name'] = 'sundar'
    student['age']  = 26
    print(student)
    # Get element 
    print('Student Name ',student.get('name'))
    print('Student Address ',student.get('address'))
    # shallow copy
    student_info = student.copy()
    student['name'] = 'jasmine'
    print(student_info)
    print('parent-dict',student)
    print('Dictkeys',student.keys()) # returns the keys
    print('DictItems', student.items()) # returns key and value pair
    # add new key
    student['phone'] = '1234567890'
    deleted = student.pop('add',None)
    print(deleted)
    print('DictValues',student.values())
    # sort a dictionary by keys. 
    print(list(sorted(student.keys())))
    print("length of dictionary is ",len(student))
    
DictionaryMethods()
