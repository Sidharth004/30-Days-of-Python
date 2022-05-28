#SET DATATYPE

#It's an unordered collecctionof elements.....i.e : order
#..of elements is not maintained in the sets
#does not accept duplicate elements

s={10,20,'sid',313,828}
print(s)

#can use set function to create a set :

s=set('Hello')
print(s)

#k=list(452)
#print(k) #error:'int' object is not iterable.
#instead:
ls=[1,2,3,3,4,5,5]
s=set(ls)
print(s) #O/P :{1, 2, 3, 4, 5}
