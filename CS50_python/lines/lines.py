'''
file called lines.py, implement a program that expects exactly one command-line argument,
the name (or path) of a Python file, and outputs the number of lines of code in that file,
excluding comments and blank lines. If the user does not specify exactly one command-line argument,
or if the specified file’s name does not end in .py, or if the specified file does not exist,
the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment.
(A docstring should not be considered a comment.) Assume that any line that only contains
whitespace is blank.
'''

import sys

def main():
    #Check whether exactly 2 arguments passed through command line
    #Check file name contains ".py" extension
    if 3 > len(sys.argv) > 1 and '.py' in sys.argv[1]:
        print(LineCounter(sys.argv[1]))
    else:
        sys.exit("Inaccurate arguments")


def LineCounter(file_name):

    lineCount = 0

    try:
        with open(file_name) as file:
            for line in file:
                #Check whether line is a comment or empty
                if line.strip().startswith("#") or len(line.strip()) == 0:
                    pass
                else:
                    lineCount += 1
            return lineCount

    #Exit if fine does not exist
    except FileNotFoundError:
        sys.exit("Fine not found")

if __name__ == "__main__":
    main()