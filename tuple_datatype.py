
#TUPLE DATATYPE

#Similar to lists
#Differences : Enclosed in ()
#              Not possible to modify elements in a tuple
#              Treated as only read only list

tpl = (1,2,3,4,'Sid',"Sam"," ")
print (tpl)
print(tpl[1])
print(tpl[1:-2])
print(tpl[-2])
print(tpl*2)

x=bytes(tpl)
print(x)