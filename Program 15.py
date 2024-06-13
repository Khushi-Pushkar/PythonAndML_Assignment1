#Write a program that reads data from a CSV file(C1) and prints it to the console
import csv
filename="C:\Ml assignment\C1.csv"
def read_csv_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

read_csv_file('C1.csv')


