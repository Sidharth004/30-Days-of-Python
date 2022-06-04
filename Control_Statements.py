# To display even numbers between 'm' and 'm'
m=int(input("enter m "))
n=int(input("enter n"))
x=m #start from m onwards
if x%2!=0: #if x is not even goto next number
    x=x+1
while x>=m and x<=n :
    if(x%2==0):
        print(x)
        x=x+2
    

print("End")