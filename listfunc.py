
def TestListMethods():
    a = []
    # example 
    # [1, 2, 3, 5, 4]
    # insert 
    a.append(1)
    print("After insert one element : ",a)
    # multiple insert 
    a.extend([2,3,4])
    print("extend an exist list : ", a)
    # insert at position 
    a.insert(3,5)
    print("insert element at pos",a)
    # Negative indexing 
    print("Negative indexing",a[-4:-2])
    # Repeat item in list 
    print("Repeating an itme",str(a[0])*4)
    # sort the list 
    #print("list after sorting",a.sort())
    # print(a.sort())
    # print("reverse the list",a.reverse())
    b = a.copy()
    print("shallow-copy",b) # independent object 
    # check object id 
    print(id(a))
    print(id(b))
    # print("count-element-in-list",count(a))
    # remove an element 
    item = 5
    if item in a:
        a.remove(item)
        print('Item removed')
    # remove element at index
    ind = 2
    a.pop(2)
    print("After pop operation : ",a)
    # delete an entire list 
    del a 
    # print(a)
#def __main__():
TestListMethods()