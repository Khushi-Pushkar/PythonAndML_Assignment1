#Write a program that takes a string input from the user and writes it to a text file.
#Take a string input from the user
str=input("Enter a string : ")
file1=open(R"C:/Ml assignment/prog5.txt","w")
print(str,file=file1)
print("Message has been stored in file",end="\n")
file1.close