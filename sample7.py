#Anonymous function 
a=lambda x:x*2
print(a(10)) 
numList=[1,2,3,4,5,6,7]
new_List=list(filter(lambda x:(x%2==0),numList))
print(new_List)
#Map & Filters in python 
numList2=[1,2,3,4,5,6,7]
new_List2=list(map(lambda x:(x+2),numList))
print(new_List2)
