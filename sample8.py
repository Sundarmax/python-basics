# Python List & operations
a=int(input('How many numbers you want to add ?'))
numList=[]
while a>0:
	b=int(input('Enter the number : '))
	numList.append(b)
	a=a-1
def opr():
	print('<------------>')
	print('Choose any one : ')
	print('1.Push')
	print('2.Pop')
	print('3.Dispaly')
	print('4.Exit')
def push():
		x=input('Enter No')
		numList.append(x)
		print('Number added in list')
def disp():
		for value in numList:
			print(value)			
def pop():
		d=int(input('Enter element : '))
		numList.remove(d)
		print('Element is Removed ')
while  True:
	opr()
	c=int(input('Enter Your choice : '))
	if(c==1):
		push()
	elif(c==2):
		pop()
	elif(c==3):
		disp()
	elif(c==4):
		break
