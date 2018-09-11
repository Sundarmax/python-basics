#Python file operations

"""
f.write("Created by sundar")
"""
with open("file.txt",'w',encoding = 'utf-8') as f:
   f.write("This file\n\n")
   f.write("contains three lines\n")
f=open("file.txt",'r',encoding="utf-8")
for line in f:
	print(line)
