'''
Among the fonts supported by FIGlet are those at figlet.org/examples.html.
FIGlet has since been ported to Python as a module called pyfiglet.
In a file called figlet.py, implement a program that:

    Expects zero or two command-line arguments:
        Zero if the user would like to output text in a random font.
        Two if the user would like to output text in a specific font,
        in which case the first of the two should be -f or --font,
        and the second of the two should be the name of the font.
    Prompts the user for a str of text.
    Outputs that text in the desired font.

If the user provides two command-line arguments and the first is not -f or --font
or the second is not the name of a font, the program should exit via sys.exit with an error message.
'''
##program starts here

import sys
from sys import argv
import pyfiglet

def main():
    try:

        if argv[1] == "-f" or argv[1] == "--f" or argv[1] == "font":
            if argv[2] == "slant" or argv[2] == "rectangles" or argv[2] == "alphabet":
                inp = input("Input: ")
                result = pyfiglet.figlet_format(inp, argv[2])
                print(result)

            else:
                sys.exit("incorrect arguments")
        else:
            sys.exit("incorrect arguments")

    except IndexError:
        sys.exit("incorrect arguments")

if __name__ == "__main__":
    main()