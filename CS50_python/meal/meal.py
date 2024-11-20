def main():

    time = input("what time is it? ").strip() #user input with no white spaces

    meal = convert(time)

    if meal >= 7.00 and meal <= 8.00:
        print("breakfast time")

    elif meal >= 12.00 and meal <= 14.00:
        print("lunch time")

    elif meal >= 18.00 and meal <= 20.00:
        print("dinner time")

    else:
        print("")

#conert function accepts time in str format and outputs time in float with 2 decimal number precision
def convert(time):

    hours, minutes = time.split(":")

    minutes = '.' + minutes

    hours = "%.2f" %(float(hours))
    minutes = "%.2f" %(float(minutes)/0.6)

    return(float(hours) + (float(minutes)))


if __name__ == "__main__":
    main()
