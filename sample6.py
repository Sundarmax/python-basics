#Python Loops 
#Nested if 
a=float(input('Enter a Number'))
if(a>=0):
	if(a==0):
		print('A is zero')
	else:
		print('A is +ive Number')
else:
	print('A is -ive Number')

#For loops
nameList=['sundar','mary']
for value in nameList:
	print(value)
print(range(0,10))
print(list(range(0,10,2)))

#get size of list using len() function

numList=[1,2,3,4,5]
for i in range(len(numList)):
	if(numList[i]==4):
		break
	elif(numList[i]==2):
		continue
	print('index value is {0}, item value is {1}'.format(i,numList[i]))	

#while loops
sum=0
i=10;
while i>0:
	sum=sum+i
	i=i-1
print('Sum of first 10 Number is ',sum)
