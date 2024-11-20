'''
In a file called outdated.py, implement a program that prompts the user for a date,
anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
wherein the month in the latter might be any of the values in the list below:
 months = [ "January", "February", "March", "April","May", "June", "July", "August", "September",
        "October", "November", "December" ]
Then output that same date in YYYY-MM-DD format.
If the user’s input is not a valid date in either format, prompt the user again.
Assume that every month has no more than 31 days;
no need to validate whether a month has 28, 29, 30, or 31 days.
'''
## program starts here

import sys
import re

def main():

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]

    #while loop to reject inputs in the undesired formats and prompt the user
    while True:
            tarikh = input("Date: ").title().strip()


            month, day, year = date_convert(tarikh, months)

            if month == 0 and day == 0 and year == 0:
                continue

            else:
                #print in yyyy-mm-dd format
                print(f"{'%04d' % year}-{'%02d' % month}-{'%02d' % day}")
                sys.exit()

#function to split user input in month, day, year
def date_convert(date, months):
    if "," in date:
        try:
            date_new = re.search(r"^(.+) ?(..), ?(....)$", date,re.IGNORECASE)
            month, day, year = date_new.groups()
            month = month.strip()
            if month in months:
                for i in range(len(months)):
                    if months[i] == month:
                        month = i+1
                        #print(month)
            m, d, y = check(month, day, year)
            return(m, d, y)
        except AttributeError:
            print("here")
            return(0, 0, 0)

    elif "/" in date:
        date_new = date.replace("/", " ")
        month, day, year = date_new.split(" ")

        #if month in months:
            #for i in range(len(months)):
                #if months[i] == month:
                    #month = i+1
        if month not in months:
            m, d, y = check(month, day, year)
        else:
            return(0, 0, 0)

        return(m, d, y)

    else:
        return(0, 0, 0)

#function to verify day and month is not out of bound
def check(month, day, year):
    try:
        month = int(month)
        day = int(day)
        year = int(year)

        if month > 12 or day >31 or year > 9999:
            return(0, 0, 0)

        else:
           return (month, day, year)

    except ValueError:
        return(0, 0, 0)

if __name__ == "__main__":
    main()