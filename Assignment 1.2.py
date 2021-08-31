import math
a=int(input("Enter x cordinate of 1st point"))
b=int(input("Enter y cordinate of 1st point"))
c=int(input("Enter x cordinate of 2nd point"))
d=int(input("Enter y cordinate of 2nd point"))
dist=math.sqrt((a-c)**2 +(b-d)**2)
print("Distance between the given points is",dist)
