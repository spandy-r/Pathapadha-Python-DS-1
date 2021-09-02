#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
s=input("Enter string")
le=len(s)
str=""
if le>=3:
    z=s[le-3]+s[le-2]+s[le-1]
    if z=="ing":
        x=0
        while x!=le-3:
            str=str+s[x]
            x+=1
        print(str+"ly")
    else:
      print(s+"ing")
else:
    print(s)
