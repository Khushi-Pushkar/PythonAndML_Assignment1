# Write a python program that takes a list of numbers and returns their sum
def sum():
    cal = 0
    num = int(input("How many numbers do you want to add? "))
    for i in range(num):
        num = float(input(f"Enter number {i+1}: "))
        cal += num
    print("The sum of the numbers is:", cal)

sum()