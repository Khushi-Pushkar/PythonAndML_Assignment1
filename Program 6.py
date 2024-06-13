#Write a program that reads the content of a text file and prints it to the console.
samplefile1="C:/Ml assignment/prog5.txt"
with open(samplefile1,"r")as file:
    content=file.read()

print("Content of the file :",content)
