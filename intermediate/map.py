
from functools import reduce

# Use cases of Map function 
# example 1 
items = [1,2,3,4,5,6]
squared = list(map(lambda x: x*2,items))
print(squared)

# example 2 
def multiply(x):
    return (x*x)

def add(x):
    return (x+x)

funcs = [multiply,add]
for i in range(5):
    value = list(map(lambda x: x(i),funcs))
    print(value)

# Filter example. 
number_list = range(-5,5)
less_than_zero = list(filter(lambda x: x<0,number_list))
print(less_than_zero)
# Reduce example.
input_list = [1,2,3,4,5]
output = reduce(lambda x,y: x*y,input_list)
print(output)