#29/05/2022
#INPUT / OUTPUT

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
