
# Using of *arg and **kwarg . 
# Asterisk matter name doesn't. 
import pdb

def make_bread():
    a = 5
    pdb.set_trace()
    return "I don't have time"

def test_var_args(var,*vars):
    print("Normal Argument",var)
    for item in vars:
        print("Variable Argument",item)

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

#greet_me(name="yasoob",age = "26")
#dataset = {"name":"sundar","age" :"26","profession":"Sofware Engineer"}
#greet_me(**dataset)
#name = yasoob
#test_var_args("11","1","2","3")
print(make_bread())