def AddBinary(A,B):
    if len(A) != len(B):
        print("Arrays must be of equal length.")
        return
    C = []
    carry = 0
    for i in range(0,len(A)):
        C.insert(i, (A[i] + B[i] + carry) % 2)
        carry = (A[i] + B[i] + carry) / 2
    C.insert(len(C)-1,carry)
    return C

A = [1,1,1,1,1,0,1]
B = [1,1,0,1,1,1,1]

def MyAddBinary(A,B):
    if len(A) != len(B):
        print("Arrays must be of equal length.")
        return
    C = []
    for i in range(0,len(A)+1):
        C.append(0)
    for i in range(0,len(A)):
        oldVal = C[i]
        C.pop(i)
        C.insert(i,oldVal+A[i]+B[i])
        if C[i] == 2:
            C.pop(i)
            C.insert(i,0)
            C.pop(i+1)
            C.insert(i+1,1)
        if C[i] == 3:
            C.pop(i)
            C.insert(i,1)
            C.pop(i+1)
            C.insert(i+1,1)
    return C

print("C: " + str(AddBinary(A,B)))
print("My C: " + str(MyAddBinary(A,B)))
