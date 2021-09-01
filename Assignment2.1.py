n=int(input("Enter no."))
temp=n
c=0;
while temp!=0:
    z=temp%10
    y=z**3
    c=c+y
    temp//=10

if c==n:
    print("Armstrong no.")
else:
    print("not armstrong no.")
    
