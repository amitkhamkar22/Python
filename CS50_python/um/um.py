'''
It’s not uncommon, in English, at least, to say “um” when trying to, um, think of a word.
The more you do it, though, the more noticeable it tends to be!

In a file called um.py, implement a function called count that expects a line of text as input as a str
and returns, as an int, the number of times that “um” appears in that text, case-insensitively,
as a word unto itself, not as a substring of some other word. For instance, given text like hello, um,
world, the function should return 1. Given text like yummy, though, the function should return 0.
'''

import re

def main():

    print(count(input("string: ")))

def count(string):
    #return(len(re.findall(r"\b(um)\b|\b(UM)\b|\b(Um)\b", string,re.IGNORECAS)))
    return(len(re.findall(r"\b(um)\b", string,re.IGNORECASE)))

if __name__ == "__main__":
    main()