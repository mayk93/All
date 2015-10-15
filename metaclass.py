#!/usr/local/bin/python3

class MyBaseClass:
    x = 10

variableHoldingADerivedClass = type("MyDerivedClassName",(MyBaseClass,),dict(y=5)) # Class name, class 'parents' and class body as a dictionary

x = MyBaseClass()
y = variableHoldingADerivedClass()

print(x.x)
print(y.x)
print(y.y)

# Should be 10 10 5
