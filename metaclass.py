#!/usr/local/bin/python3

class MyBaseClass:
    x = 170
    def baseFunction(self,lst,index):
        try:
            print(lst[index])
        except:
            pass

variableHoldingADerivedClass = type("MyDerivedClassName",(MyBaseClass,),dict(y=100,derivedFunction=lambda self,lst,start,end: print(lst[start:end]))) # Class name, class 'parents' and class body as a dictionary

x = MyBaseClass()
y = variableHoldingADerivedClass()

print(x.x+5)
print(y.x+5)
print(y.y+5)

# Should be 175 175 105

x.baseFunction([1,2,3],0)
y.baseFunction([4,5,6],1)
y.derivedFunction([7,8,9,10,11,12],2,5)
