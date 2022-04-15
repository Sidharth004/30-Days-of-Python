#byte datatype

#can store numbers in range : 0 - 255
#represents group of byte numbers
#cannot store negative numbers

elements=[0,12,32,244] #list of byte numbers
x=bytes(elements)#converts list into byte array
print(x[0-3])
#print(x[4])
print(x[2])
print(x[1:2])

#program to create a byte type array , read and display the elements of the array
elements1=[1,12,23,4,56,67,89,122]
sum= 0
y=bytes(elements1)
#for i in y : print(i) 
for i in elements1 :
    #sum=sum + elements1
    sum=sum + i
print(sum)

#RANGE FUNCTION() :
#it can generate a sequence of numbers using ...range functions
#we can also define the start-step-size ...as (start,stop,step-size)
#IMP:it is not an iterator
#to force the this function to output all it's items , wwe can us e the function "list()"

print(range(10))
print(range(2,8))
print(range(2,8,2))

print(list(range(10)))
print(list(range(2,8)))
print(list(range(2,8,2)))


