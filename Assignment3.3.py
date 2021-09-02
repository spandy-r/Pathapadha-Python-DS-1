#Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
s=input("Enter string")
l=len(s)
str=""
for i in range(1,l-1):
    str+=s[i]
print(s[l-1]+str+s[0])
