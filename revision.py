s1="13123"
n=int(s1,8)
print(n)

print("""this is 'python' nice""")

elements=[10,20,4,50,100]
x=bytearray(elements)
for i in x: print(i)


string ='A'
print(type(string))

charprint = "abcdeg"
for i in charprint:
            charprint[0].isupper()#looks ike char in charprin does'nt work out :-(
        
#
#in python defining constants is not possible
#can indicate a name as a constant  by writng its name in all capital letters ....but it's value can be changed.

#
#Identifier is a name given to variable or a function
# remember that pyhton is a case sensitive programming lang.
#NAMING CONVENTIONS IN PYTHON :
#1.PACKAGE  name should always be written in lower case letters , multiple words seperated by underscore '_'.
#2.MODULES - same as packages.
#3.CLASSES - each word of a class name should start with capital letter ....rule applicabe to only classes created by us .
#          - when a claass represents exception , then its name should end with word 'error'.
#GLOBAL VARIABLES - lowercase.
#METHOD ARGUMENTS -In case of instance methods, ther first argument name should be self
#                  - In class methods , their firlst argument name should be cls.
#CONSTANTS - already studied 'bout it.

#FUNFACT - PYTHON HAS ONLY SINGLE LINE COMMENTS '#' ....lol
#WORD OF CAUTION - Python does not have increment operator(++) or a decrement operator(--)

n=10
print(n)

n=10
print(-n)

n=-10
print(-n)

b=20
print(n>b)

if(n<b):
    print("YES")
else:
    print("NO")

#relational operators can be chained !
x=22
18<x<0

1<2<3<4

x=25
y=12
id(x)
print(x and y)
print('~x =',~x)
 
postal = {'delhi':1110 , 'bombay':1111 , 'pune':1112}
for city in postal :
                    print(city)


                    postal = {'delhi':1110 , 'bombay':1111 , 'pune':1112}
for city in postal :
                    print(city , postal[city])

a=24  #in python everything is considered as an object
id(a)

#the 'is' and 'not is' compare the memory locations of the objects and not it's values.

a= 25
#b=25
b=24 
if(a is b):
    print("a and b have same identity")
else:
    print("do not have same identity")

a=[1,2,3,4]
b=[1,2,3,4]
if(a is b):
    print("both have same identity")
else:                                       # since both these lists are created at different memory locations their identity are diff.
    print("do not have same identity")

if(a==b):                                     #is operator does not comare values ....'==' can .
    print("comparison satidfied")


#OPERATOR PRECEDENCE :
#1) Paranthesis
#2) Exponential
#3) Unary Minus , Bitwise complement
#4) Multiplication , Division , Floor Divivsion , Modulus
#5)Addition , Subtraction
#6)Bitwise left/right shift
#7)Bitwise AND
#8)Bitwise XOR
#9)Bitwise OR
#10)Relational Operators(>,<,>=,<=,==,!=)
#11)Assignment Operators(=,+=,-=,/=,%=,*=,**=)
#12)IDENTITY OPERATORS Is , Is not
#13)MEMBERSHIP OPERATORS In , Not in
#14)Logical NOT
#15)logical AND
#16)logival OR

#Associativity => Left to Right .


print(id(a))




