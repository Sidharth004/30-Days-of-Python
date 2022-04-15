#BYTE ARRAY
#here , array can be modified 

elements=[1,2,3,4,5,6,7,8]
x=bytearray(elements)
print(x)
x[0]=0
print(x)
for i in x : print(i)