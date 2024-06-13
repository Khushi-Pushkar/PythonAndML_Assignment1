#Write a program in python that converts a string into a list of its characters
# Take input string
str = input("Enter a string: ")

# Convert string to list of characters
list = []
for i in str:
    list.append(i)

# Print the list of characters
print("The list of characters is:", list)