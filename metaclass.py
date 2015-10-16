#!/usr/local/bin/python3

class MyBaseClass:
    x = 15

variableHoldingADerivedClass = type("MyDerivedClassName",(MyBaseClass,),dict(y=10)) # Class name, class 'parents' and class body as a dictionary

x = MyBaseClass()
y = variableHoldingADerivedClass()

print(x.x+5)
print(y.x+5)
print(y.y+5)

# Should be 20 20 15
