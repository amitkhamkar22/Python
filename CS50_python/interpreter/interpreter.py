def main():

#print statement below prints float value with 1 decimal point precision
    print("{:.1f}".format(math(input("which expression do you want to solve? ").strip())))


#math() function extracts and interpret operator and operands from the input string
#and the appropriate mathematical solution is returned.

def math(str):

    import operator

    '''
    ops = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv,  # use operator.div for Python 2
        '%' : operator.mod,
        '^' : operator.xor,
    }
    '''

    str_1, str_2, str_3 = str.split(" ",3)

    match str_2:

        case "+":
            return (operator.add(int(str_1), int(str_3)))

        case "-":
            return (operator.sub(int(str_1), int(str_3)))

        case "*":
            return (operator.mul(int(str_1), int(str_3)))

        case "/":
            return (operator.truediv(int(str_1), int(str_3)))

        case "%":
            return (operator.mod(int(str_1), int(str_3)))

        case "^":
            return (operator.xor(int(str_1), int(str_3)))

        case _:
            return ("not a valid expression")

if __name__ == "__main__":
    main()