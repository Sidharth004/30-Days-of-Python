# To display even numbers between 'm' and 'm'
"""m=int(input("enter m "))
n=int(input("enter n"))
x=m #start from m onwards
if x%2!=0: #if x is not even goto next number
    x=x+1
while x>=m and x<=n :
    if(x%2==0):
        print(x)
        x=x+2
print("End")"""

#for loop can work with sequence like string , list ,tuple , range ,array .

#to dislpay each character from a string
str='hello'
for ch in str:
    print(ch)
"""""
str=input("enter a string")
for ch in str:
    print(ch)

str=input("enter another string") # here I want to print the string if it contains the charchters i've mentioned below
for x in str:

    if str[x]=='q'and str[x]=='l': #TypeError: string indices must be integers
        print(x)
      
    #NEED A FIX FOR THIS !
"""
####################################################################################################################################
5/6/22

#program to display characters of a string using sequence index
str='hello'
n=len(str)
print (n)
for i in range(n): #from n to n-1
    print(str[i])
#this will help me to fix the above written code

#eg range(10) ....will return numbers from '0' to 9.
#we can also specify the staring number and end number , as : range(5,10) ->from 5 to 9
#can also specify the step size (1,10,2) ..to increment the value of the number at each step. ->1,3,5,7,9

for i in range(1,10,2):
    print(i)
"""""
x=int(input("enter a number"))
n=range(x)
for i in n :
    
    print(i+2)
    i=i+2
"""
#to display in descending order
#for x in range(10,0,-1):
 #   print(x)  
"""x=int(input("enter range"))
while x in range (10,0,2):
    print(range) """

"""#for loop to access elements of list
list=[x for x in input("enter the string groups").split(',')]
print("you entered :",list)   #to print the list
for elements in list:
    print(elements) # to print the elements of the list individually """

"""list1=[1,2,34,4] #list can have elements of multiple datatypes
sum=0
for element in list1 :
    #print(element)
    sum +=element
print("SUM :",sum) # next statement after the loop """

#same as above , but taking input from user
'''list1=[element for element in input("enter the list items").split(',')]
for element in list1:
    print (list1)
sum=0
for element in list1:
    print(element)
    sum+=list1[element]# error :list indices must be integers or slices, not str
print('SUM :',sum)'''

'''list=[10,20,30,40]
sum=0
for i in list:
    print(i)
    sum+=i
print(sum)'''

#infinite loop
"""i=1
while i<=10:
    print(i)"""

#while(True):
 #   print("HAI")

#NESTED LOOPS / pattern progrmans
for k in range(1,11):
    for i in range (1,k+3):
        print("*",end='')
    print()

for k in range (0,4):
    for i in range(0,4):
        print('@',end=" ")
    print()

for k in range(0,5):
    for i in range(k-1,4):
        print('!',end="")
        for p in range(0,k+1):
         print('2',end=" ")
    print()#check this prog
    



    

