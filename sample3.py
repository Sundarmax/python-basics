'''input & output '''
#Output Formating 
import math
x=12
y=15
print('x type is {0} y type is {1}'.format(type(x),type(y)))
print('x value is {0}, y value is {1}'.format(x,y))
print('x value is %d '%x)
print('y value is %d'%y)
print ('x value is {color_one} y value is {color_two}'.format(color_one='white',color_two='yellow'))
print('---------------')
print(1,2,3,4,sep='*',end="\n")
a=input('Enter Number ')
b=input('Enter One more No ')
print('sum is {0}'.format(int(a)+int(b)))
print('PI value is {0}'.format(math.pi))
