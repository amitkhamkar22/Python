'''
In a file called pizza.py, implement a program that expects exactly one command-line argument,
the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art
using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s
grid format. If the user does not specify exactly one command-line argument, or if the specified file’s
name does not end in .csv, or if the specified file does not exist, the program should instead exit
via sys.exit.
'''
import sys
import csv
from tabulate import tabulate

def main():
    #Check whether exactly 1 arguments passed through command line
    #Check file name contains ".csv" extension
    if 3 > len(sys.argv) > 1 and '.csv' in sys.argv[1]:

        print(ASCII_art(sys.argv[1]))

    else:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif '.csv' not in sys.argv[1]:
            sys.exit("Not a CSV file")


def ASCII_art(file_name):

    try:
        lines = []

        with open(file_name) as file:

            for line in file:
                lines.append(line.strip())
        
        return(tabulate(csv.reader(lines[1:]), headers = lines[0].split(','), tablefmt="grid"))

    #Exit if fine does not exist
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()