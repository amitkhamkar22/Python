'''
Assuming there are 365 days in a year, there are minutes in that same year (because there are 24 hours
in a day and 60 minutes in an hour). But how many minutes are there in two or more years? Well, it depends
on how many of those are leap years with 366 days, per the Gregorian calendar, as some of them could have
additional minutes. In fact, how many minutes has it been since you were born? Well, that, too, depends
on how many leap years there have been since! There is an algorithm for such, but let’s not reinvent that
wheel. Let’s use a library instead. Fortunately, Python comes with a datetime module that has a class
called date that can help, per docs.python.org/3/library/datetime.html#date-objects.

In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM
-DD format and then sings prints how old they are in minutes, rounded to the nearest integer, using English
words instead of numerals, just like the song from Rent, without any and between words. Since a user might
not know the time at which they were born, assume, for simplicity, that the user was born at midnight
(i.e., 00:00:00) on that date. And assume that the current time is also midnight.In other words, even if the
user runs the program at noon, assume that it’s actually midnight, on the same date. Use datetime.date.today
to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.
'''

import datetime
from datetime import date
import sys
import re
import inflect

def main():

    tem = time_in_minutes(input("Date of Birth: "))
    print(tem)

def time_in_minutes(tem):

    try:
        #regex to capture year, month, day form the birth date provided by user in yyyy-mm-dd format
        samay = re.search(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", tem)

        #converting strings to int
        birthYear = int(samay.group(1))
        birthMonth = int(samay.group(2))
        birthDay = int(samay.group(3))

        #capture today's date
        now = date.today()

        #catch if date input is incorrect
        try:
            birthday = datetime.date(birthYear, birthMonth, birthDay)

        except ValueError:
            sys.exit("Invalid date")

        #using datetime library method finding age by subtracting birth date form current date
        delta = (now - birthday)

        if  delta.days > 0:
            p = inflect.engine()
            return(p.number_to_words(delta.days*24*60, andword = '') + " " +"minutes").capitalize()

        else:
            sys.exit("Invalid date")

    except AttributeError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()