#Write a python program that calculates the factorial of a given number
#Taking input numbers from user
n=int(input("Enter a number"))

#Calculates the factorial
factorial = 1
if n >= 1:
    for i in range (1, n+1):
        factorial=factorial *i
print(factorial,end=" ")
    