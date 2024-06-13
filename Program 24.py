#Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result
#Enter two number from user
a=int(input("Enter the first number of calculator:"))
b=int(input("Enter the second number of calculator:"))
x=input("Enter the operator(+,-,*,/) for calculator-")
if x=="+":
    print("Sum of",a,"and",b,"is:",a+b,end="\n")
elif x=="-":
    print("Difference of",a,"and",b,"is:",a-b,end="\n")
elif x=="*":
    print("Multiplication of",a,"and",b,"is:",a*b,end="\n")
elif x=="/":
    print("Division of",a,"by",b,"is:",a/b,end="\n")
else:
    print("Invalid operation")