#Write a program in python that counts the frequency of each character ina string
#Enter string from user
x=input("Enter a string-")
y=""
for i in x:
    if y.find(i)==-1:
        print(i,"-",x.count(i))
        y+=i
