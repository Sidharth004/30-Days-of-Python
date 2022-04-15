#PYHTON program to convert hex / oct / bin number into DECIMAL Number system
 
 
#Octal
n1=0O17
#Binary
n2=0B11100100
#Hexadcimal
n3=0X1c2

n=int(n1)
print("n1 is converted ...now =", n )
n=int(n2)
print("n2 is converted ...now =", n )
n=int(n3)
print("n3 is converted ...now =", n )


#Convert a STRING into a INTEGER 
str= "1c2"  #string str contains hexadecimal no.
str2="1C2"
#str3="heyImSid" ##error :ValueError: invalid literal for int() with base 32: 'heyImSid'
#n=int(str3,16)
print(n)

#Convert numbers fromm different nubersystems into decimal number system
#v2.0

s1="110001010001"
s2="17"
s3="1cb2345e14f"

n1=int(s1,2)
print("binary 110001010001 is ..",n , "in integer")
n2=int(s2,8)
print("octal 17 is ",n,"in integer")
n3=int(s3,16)
print("hexa 1cb2345e14f is ...",n,'in integer')

b=bin(n1)
print("int of n1 converted back to Binary",b)
b=bin(n2)
print("int of n2 converted back to Binary",b)
b=bin(n3)
print("int of n3 converted back to Binary",b)

#same way can do with b=oct(n1)
#b=hex(n1)

