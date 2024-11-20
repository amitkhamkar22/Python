'''
In a file called working.py, implement a function called convert that expects a str in either of the
12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect
that AM and PM will be capitalized (with no periods therein) and that there will be a space before each.
Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

    9:00 AM to 5:00 PM
    9 AM to 5 PM

Raise a ValueError instead if the input to convert is not in either of those formats or if either time
is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante
meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).
'''

import re
import sys


def main():

    try:
        print(convert(input("Hours: ")))

    except ValueError:
        sys.exit("ValueError")


def convert(string):

    string = re.search(r"(\d+):?(\d\d?)?( )?(\w{2}) ?(..)? (\d+):?(\d\d?)?( )?(\w{2})", string)

    '''
    print("1",string.group(1))
    print("2",string.group(2))
    print("3",string.group(3))
    print("4",string.group(4))
    print("5",string.group(5))
    print("6",string.group(6))
    print("7",string.group(7))
    print("8",string.group(8))
    print("9",string.group(9))
    '''

    #if input 60 for value of minutes (e.g 9:60 AM) raise ValueError
    #if input for minutes is not 2 digit value, raise ValueError
    if string.group(2) and string.group(7):
        if int(string.group(2)) > 59 or int(string.group(7)) > 59:
            raise ValueError
        elif len(string.group(2)) != 2 and len(string.group(7)) != 2:
            raise ValueError
        else:
            pass
    else:
        pass

    #if input any other character instead of "to" raise ValueError
    if string.group(5) != "to" or string.group(5) == None or string.group(8) == None:
        raise ValueError
    else:
        pass

    #if time is after 12:00 PM and before 12:00 AM, add 12 to convert to 24 hrs format
    #else add 0 hrs
    if string.group(4):
        if string.group(4) == "PM" and string.group(1) != "12":
            LHS_time = int(string.group(1)) + 12
        elif string.group(4) == "PM" and string.group(1) == "12":
            LHS_time = int(string.group(1))
        elif string.group(4) == "AM" and string.group(1) != "12":
            LHS_time = int(string.group(1))
        elif string.group(4) == "AM" and string.group(1) == "12":
            #print("here1")
            LHS_time = 0
        else:
            raise ValueError
    else:
        raise ValueError

    #if time is after 12:00 PM and before 12:00 AM, add 12 to convert to 24 hrs format
    #else add 0 hrs
    if string.group(9):
        if string.group(9) == "PM" and string.group(6) != "12":
            RHS_time = int(string.group(6)) + 12
        elif string.group(9) == "PM" and string.group(6) == "12":
            #print("here2")
            RHS_time = int(string.group(6))
        elif string.group(9) == "AM" and string.group(6) != "12":
            RHS_time = int(string.group(6))
        elif string.group(9) == "AM" and string.group(6) == "12":
            RHS_time = 0
        else:
            raise ValueError
    else:
        raise ValueError

    #return value to main() in appropriate format
    if string.group(2) and string.group(7):
        return (f"{LHS_time:02d}:{string.group(2)} {string.group(5)} {RHS_time:02d}:{string.group(7)}")
    else:
        return (f"{LHS_time:02d}:00 {string.group(5)} {RHS_time:02d}:00")

if __name__ == "__main__":
    main()