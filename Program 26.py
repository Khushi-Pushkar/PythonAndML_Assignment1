#Write a program in python that checks if a string starts with a given prefix or ends with a given suffix
s=input("Enter a string: ")
pre=input("Given prefix-")
if s[0:len(pre)]==pre:
    print("Yes it starts with given prefix")
else:
    print("No it doesn't start with given prefix")
suf=input("Given suffix-")
if s[len(s)-len(suf):]==suf:
    print("Yes it ends with given prefix")
else:
    print("No it doesn't end with given suffix")
