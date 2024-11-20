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
# import operator helps perform devision (operator.truediv(number))
# sys is used to exit program
import operator
import sys

def main():

    #while allows prompting user repeatedly until correct input is provided
     while True:
        gas = input("Fraction: ").strip().lower()

        #checking whether fraction is in a corrct format
        if "/" in gas:
            indicator = gauge(convert(gas))

            #if return value from gauge() is False input is rejected and user is prompted for new input
            if indicator:
                print(indicator)
                sys.exit()
            else:
                pass
        else:
            pass

# Convert function eveluates whther or not input fraction is appropriate and returns fraction to main
def convert(fraction):
    try:
        num, den = fraction.split("/")

        num = int(num)
        den = int(den)

        if num <= den:
            return (operator.truediv(num,den)*100)

         #if numerator of the fraction is greater than denominator this is more than 100% tank capacity
         # so returning x to reject input and prompt the user
        else:
            return None

    #if user provides non numaric input returning x to reject input and prompt the user
    except ValueError:
        return None

    #if user provides zero numaric input for denominator returning x to reject input and prompt the user
    except ZeroDivisionError:
        return None

#Gage function converts % numeric value into Full, Empty,
# or returns numeric % rounded to the nearest integer
def gauge(percentage):
    #returning False to reject input and prompt user
    if (percentage) == None:
        return False

    elif round(percentage) >= 99:
        return("F")

    elif round(percentage) <= 1:
        return("E")

    else:
        return(f"{round(percentage)}%")

if __name__ == "__main__":
    main()