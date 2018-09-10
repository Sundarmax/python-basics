'''Python Operators'''
import math
a=input('Enter value 1 :')
b=input('Enter value 2 :')
f=c=int(a)
d=int(b)
print('Add',c+d)
print('Sub',c-d)
print('Div',c/d)
print('RDiv',c//d)
print('Mod',c%d)
if(c==d):
    print('values are equal')
elif(a>b):
    print('A is greater')
elif(a<b):
    print('B is greater')
#boolean operators
x=True
y=False
if(x and y):
    print('True')
elif(x or y):
    print('True')
c=False
print(not c)
f*=5
print('f value is ',f)
#identity operators is /is not
#membership operators in/not in
x=5
y=5
a=(1,2,3,4,5)
if(x is y):
    print('values are in same memory locations')
if(3 in a):
    print('Value is found')