'''
In a file called scourgify.py, implement a program that:
    Expects the user to provide two command-line arguments:
        the name of an existing CSV file to read as input, whose columns are assumed to be,
        in order, name and house, and the name of a new CSV to write as output, whose columns
        should be, in order, first, last, and house.
    Converts that input to that output, splitting each name into a first name and last name.
    Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the first cannot be read,
the program should exit via sys.exit with an error message.
'''
import sys
import csv

def main():
    #Check whether exactly 1 arguments passed through command line
    #Check file name contains ".csv" extension
    if 4 > len(sys.argv) > 2 and '.csv' in sys.argv[1] and '.csv' in sys.argv[2]:

        write_new_csv(sys.argv[1])

    else:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif '.csv' not in sys.argv[1] or '.csv' not in sys.argv[2]:
            sys.exit("Not a CSV file")


def write_new_csv(file_name):

   try:
        lines = []

        with open(file_name) as csvfile:

            reader = csv.DictReader(csvfile)
            for line in reader:
                #split the name column from before.csv into first name and last name
                lastName, firstName = line["name"].split(",")
                lines.append({"first": firstName.strip(), "last":lastName.strip(), "house":line["house"].strip()})
            #print(lines)

        with open(sys.argv[2], "w", newline = "") as newcsvfile:
            writer = csv.DictWriter(newcsvfile, fieldnames = ["first", "last", "house"])
            # writing headers (field names)
            writer.writeheader()
            # writing data rows
            writer.writerows(lines)

    #Exit if fine does not exist
   except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()