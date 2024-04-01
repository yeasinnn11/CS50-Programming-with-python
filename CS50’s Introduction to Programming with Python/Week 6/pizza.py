from sys import argv,exit
import csv
from tabulate import tabulate

if len(argv) < 2:
    exit("Too few command-line arguments")
elif len(argv) > 2:
    exit("Too many command-line arguments")
elif not argv[1].endswith(".csv"):
    exit("Not a CSV file")

table=[]

try:
    with open(argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)
        print(tabulate(table[1:],table[0],tablefmt="grid"))
except FileNotFoundError:
    exit("File does not exist")

