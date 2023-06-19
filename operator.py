x=4 
y=8
#Arithmetic operators
print("Addition: ",int(x+y))
print("Subtraction: ",int(x-y))
#Assignment operators
z=0
z+=8
print("result of z+=8:",z)
z-=4
print("result of z-=4:",z)
#Comparison operators
x<y
x>y
x==y
x!=y
#Logical Operators
a=True
b=False
print("a and b is: ", a and b)
print("a or b is: ",a or b)
print("not a is: ", not a) 
#Bitwise Operators
x>>3
print("x shifted to right by 3 bits")
y<<4
print("y shifted to right by 4 bits")
#Identity Operators
x is 4
y is not 8
#Membership Operators
c="siddhi"
d= 'd' in c
print("in: ",d)
e= 'm' not in c
print("not in: ",e)