'''
An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate
on the internet, akin to a postal address in the real world, typically formatted in dot-decimal
notation as #.#.#.#. But each # should be a number between 0 and 255, inclusive. Suffice it to say
275 is not in that range! If only NUMB3RS had validated the address in that scene!

In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input as
a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.

Either before or after you implement validate in numb3rs.py, additionally implement, in a file called
test_numb3rs.py, two or more functions that collectively test your implementation of validate thoroughly,
each of whose names should begin with test_ so that you can execute your tests with:
'''

import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    '''
    Regex looks for the 250-5 case, after that it ORs all the possible cases for 200-249 100-199 10-99.
    Notice that the |) ORs the 0-9 range.
    '''
    if re.search(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}$", ip):
       return True
    else:
       return False


if __name__ == "__main__":
    main()
