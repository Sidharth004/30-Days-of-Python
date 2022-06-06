#29/05/2022
#INPUT / OUTPUT

from tkinter import X, Variable


print("hello")
print('hello') #both same 

print("hello \n nxtl line")
print("hello \\n not next line") # to escape the efect of escape sequence
print("hello \t next line here") # tab spacing
print(3*"hello") #repetition operator to repeat the strings in output.
print(3*"\t hello")

print("hello"+"how are you?") # '+' to join two strings without spacing .
print("hello","how are you") # with space in between

a=10
b=20
print(a,b) #observe that the values are printed with space in betwween them by default.
print(a,b,sep=",") # to seperate output by a comma ','.
print(a,b,sep=':')
print(a,b,sep='----')

#we can ask the print() function not to throw the cursor in the next line ,  but display the o/p on the same line.
#usefull when printing multiple to display output.
#end attribute

print("hello",end='')
print("how are you",end='')
print('\n')
print("helo",end=',')
print("how are you")

# to print object
# we can pass objects such as lists , tuples or dictionaries to the print() TO display the ELEMENTS OF THOSE OBJECTS.
list=[1,'a',2,'c',3]
print(list,end='') 
list2=[4,'d',4,'e',5]
print(list2)

#print formatted string
#output  displayed by the print function() can be formatted as we like
#'%' special operator can be used for this purpose.
#it's join a string with a variable or value in a specific format ...studied below.
a=10
print('a=%i'%a) # %i or %d to represent decimal integer numbers
b=22.4
print('b=%f'%b) # %f to represent float values
print('list is %s'% list)# %s to represent string !
print('list is(%200s)'%list) #it will alot 200 spaces and then the list is displayed.
a=10
list=[1,'a',2,'c',3]
print('combined %i example %s'%(a,list)) 
print('combined',a,'example',list)   #whats the difference ??
print('individual character %c , %c'% (list[1],list[0])) #%c to dislpay a single character 
string ="abcd"
print('slice %s'%string[0:2]) #using slicing operator on a string to display required characters
print('b=%.2f'% b) #the float value is displayed with 2 fraction digits , spcified after point

#Input Statements
str = input('enter gas fee')
x=int(str)
print(x) 

x=int(input('enter a number')) #using int() function before the input() function to accept an integer fromthe keyboard

print(x)

#similarly , to accept a float value
y=float(input('enter float value'))

print(y)

str=input('enter a sentence') #no need to type cast string here , returns error
print(str)

#to accept a single character from keyboard
ch=input('enter a char')
print("u entered :",ch[0])

#accept two integer from keyboard
x=int(input("enter number a"))
y=int(input("enter number b"))
print("number a is:",x)
print("number b is :",y)
print("the numbers are:",x,y)
print("the numbers are",x,y,sep=',')#to seperate the numbers by ','
print("the numbers are %d,%d" %(x,y))#perfect !

#to accept two numbers and print their sum
num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=num1+num2
print("the sum is %d"%(num3))

#to convert numbrs from other systems into decimal number system
str=input("enter hexa decimal no. :")
x=int(str,16)
print("hexadecimal no. entered is",x)

str1=int(input("enter octal nu. :"),8)
print("octal number entere is :%i"%str1)

str3=input("enter binary number")
x=int(str3,2)
print("decimal number entere is :%i"%x)

#to accept more than one input from the same line
a,b=[int(x)for x in input("enter two numbers:").split()]

#a,b={int(x)for x in input("enter again two numbers").split()}

var1,var2,var3=[int(x)for x in input("enter the three numbers").split()] # split necessary 
#to acept three integers using ',' and find their sum
x,y,z =[int(x)for x in input("enter numbers for sum").split(',')]
sum=x+y+z
print(sum , "is the answer")

#To accept groupof strings seperated by , ',' .
list=[x for x in input("enter the string groups").split(',')]
print("you entered :",list)

#COMMAND LINE ARGUMENTS:
#these are the values passed to the python program at the command prompt
#they are passed to the program from outside the program
#arguments entered via keyboard , seperated by SPACE.

#these arguments are stored in the form of strings ...by default
#stored in a list with the name 'argv' , which is available in sys-module.
#argv[0] represents the name of the program.
#argv[1] represents the first value ..and so on...
#to find number of command line arguments entered at command prompt ..use function - len() , as len(argv)

#program to display command line arguments
import sys
n=len(sys.argv)
args=sys.argv
print("no. of command line arguments=",n)
print("the args are",args)
for a in args:
    print(a) #TAKING AUTOMATICALLY THE ARGUMENTS AS 1 ! 