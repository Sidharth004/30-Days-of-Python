#RANGE DATATYPE

#represents sequence of numbers
#numbers in the range are not modifiable
#generally,used for repeating a for loop ....a no. of times
r= range (10)
for i in r : print(i)

#can use a : STARTING NUMBER ...an ENDING NUMBER ..& STEP VALUE in the range object , too.

z=range(2,30,2)
for j in z :print(j)

ls=list(range(10))
print(ls)

#for  i in ls : print(ls) #prints the entire list X range times ...lol

for i in ls :
    if ls[0]==3:
        print('ok')
       
    else:
        print(ls)