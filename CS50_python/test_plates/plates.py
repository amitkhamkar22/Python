'''
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car,
with your choice of letters and numbers instead of random ones. Among the requirements, though, are:
    “All vanity plates must start with at least two letters.”
    “…vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    “Numbers cannot be used in the middle of a plate; they must come at the end.
    For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
    The first number used cannot be a ‘0’.”
    “No periods, spaces, or punctuation marks are allowed.

    ”In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements
    or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below,
    wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str.
    You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
'''
import string

def main():
    plate = input("Plate: ").upper()

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    s = str(s)

    # check min 2 and max 6 characters
    if 1 < len(s) < 7:

        # check whether plates start with at least two letters
        for l in range(2):
            if s[l] not in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
                return(False)

        #Numbers cannot be used in the middle of a plate; they must come at the end
        count = 0
        for l in range(len(s)):
            if s[l] in ['0','1','2','3','4','5','6','7','8','9']:
                count += 1
                #The first number used cannot be a ‘0’
                if count == 1 and s[l] == '0':
                    return(False)

        new_s = s[::-1]
        for i in range(count):
            if new_s[i] in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
                return(False)


        #No periods, spaces, or punctuation marks are allowed
        for l in range(len(s)):
            if l < len(s):
                if s[l] in string.punctuation:
                    return(False)

        return(True)

    else:
        return(False)

if __name__ == "__main__":
    main()