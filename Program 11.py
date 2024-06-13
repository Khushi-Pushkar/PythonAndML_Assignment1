#Write a python program that generates the first n numbers in the Fibonacci sequence
n = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0
if n <= 0:
    print("Please enter a positive integer")
# if there is only one term, return n1
elif n == 1:
    print("Fibonacci",n,":",end=" ")
    print(n1)
else:
    print("Fibonacci sequence:",end=" ")
    while count < n:
        print(n1)
        temp = n1 + n2
        n1 = n2
        n2 = temp
        count += 1
