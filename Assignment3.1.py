#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, print 'empty string' 
s=input("Enter string")
if len(s)>=2:
    str1=s[0]+s[1]+s[len(s)-2]+s[len(s)-1]
    print(str1)
else:
    print("empty string")
