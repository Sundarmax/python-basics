#dictionaries in python
d={'name':'sundar','Age':'25'}
d['mob']='11234'
print(d.keys())
print(d.values())
for i in d:
	print("{0}'-'{1}".format(i, d[i]))
print(d.get('Age'))

#nested dictionary
nest_dict={
	1: {'name':'sundar','Age':'25'},
	2: {'name': ' Mary','Age':'18'}
}
for i in nest_dict:
	print(nest_dict[i])
#print(nest_dict)