# Q25
print("Q25-Write a program that copies the contents of one text file to another:")
s1=open(r"C:/Ml assignment/prog5.txt",'r')
content=s1.read()
s1.close()
s2=open(r"C:/Ml assignment/prog5.txt",'w')
print(content,file=s2)
print("Content copied in demo2 from demo!!!",end="\n\n")
s2.close()
