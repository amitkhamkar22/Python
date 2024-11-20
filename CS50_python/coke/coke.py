'''
implement a program that prompts the user to insert a coin, one at a time,
each time informing the user of the amount due. Once the user has inputted at least 50 cents,
output how many cents in change the user is owed. Assume that the user will only input integers,
and ignore any integer that isn’t an accepted denomination.
'''
def main():

    reminder = coke_price = 50


    while reminder != 0:


       amount = int(input("Insert Coin: "))

       if amount in [50, 25, 10, 5]:

            reminder = (price(amount, reminder))

            if reminder > 0:
                print(f"Amount Due: {reminder}" )

            elif reminder <= 0:
                print(f"Change Owed: {reminder * -1}" )
                reminder = 0

       else:
            print(f"Amount Due: {reminder}" )


def price(coin, new_price):

    return (int(new_price) - int(coin))


if __name__ == "__main__":
    main()

