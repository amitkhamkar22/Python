"""
In a file called fuel.py, implement a program that prompts the user for a fraction,
formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage
rounded to the nearest integer, how much fuel is in the tank.
If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

/workspaces/76134826/extensionsIf, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
(It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError
or ZeroDivisionError.
"""

import operator # import operator helps perform devision (operator.truediv(number))
import sys

def main():

     while True:
        gas = input("Fraction: ").strip().lower()

        if "/" in gas:

            level = convert(gas)

            if level:

                indicator = gauge(level)
                if indicator == "E" or indicator == "F":
                    print(f"{indicator}")
                    sys.exit()

                else:
                    print(f"{indicator}%")
                    sys.exit()

        else:
            pass


def convert(fraction):

    try:
        num, den = fraction.split("/")

        num = int(num)
        den = int(den)

        if num <= den:

            return (operator.truediv(num,den)*100)

        else:
            return False


    except ZeroDivisionError:
        return False

    except ValueError:
        return False


def gauge(percentage):

    if round(percentage) >= 99:
        return("F")

    elif round(percentage) <= 1:
        return("E")

    else:
        return (round(percentage))

if __name__ == "__main__":
    main()