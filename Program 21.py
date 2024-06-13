#Write a python program that counts the occurrences of a specific element in a list:")
List=[1,2,3,4,5,6,4,3,2,6,7,5,4,32,2,'a','b','c',1.3,2.4]
print("List given-",List)
l=[]
for i in List:
    l.append(str(i))
x=input("Enter the specific element-")
print("Count of",x,"is:",l.count(x),end="\n")