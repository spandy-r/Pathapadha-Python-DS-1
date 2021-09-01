n=int(input("Enter no."))
temp=n
c=0
while temp!=0:
    c+=temp%10
    temp//=10
print("Sum of digits=",c)
