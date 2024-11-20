'''
in a file called adieu.py, implement a program that prompts the user for names,
one per line, until the user inputs control-d. Assume that the user will input at least one name.
Then bid adieu to those names, separating two names with one and, three names with two commas
and one and, and names with commas and one and, as in the below:

    Adieu, adieu, to Liesl
    Adieu, adieu, to Liesl and Friedrich
    Adieu, adieu, to Liesl, Friedrich, and Louisa
    Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
'''

#Program starts here

import inflect
import sys

def main():

    mylist = []
    p = inflect.engine()

    try:
        while True:
            name = input("Name: ")
            mylist.append(name)

    except EOFError:
        print("Adieu, adieu, to " + p.join(mylist))

if __name__ == "__main__":
    main()