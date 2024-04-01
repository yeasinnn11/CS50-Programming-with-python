from sys import argv,exit
import csv

def main():
    if len(argv) <3:
        exit("Too few command-line arguments")
    elif len(argv) >3:
        exit("Too many command-line arguments")
    try:
        with open(argv[1],'r') as file:
            reader = csv.DictReader(file)
            with open(argv[2],'w') as file:
                 fieldnames= ['first','last','house']
                 writer = csv.DictWriter(file, fieldnames=fieldnames)
                 writer.writeheader()
                 for row in reader:
                    last, first = row['name'].split(", ")
                    row['name'] = {'first' : first, 'last' : last}
                    writer.writerow({'first': row['name']['first'],'last':
                                     row['name']['last'], 'house' : row['house']})
    except FileNotFoundError:
        exit('Could not read invalid_file.csv')

if __name__ == "__main__":
    main()
