'''
In a file called grocery.py, implement a program that prompts the user for items,
one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).
Then output the user’s grocery list in all uppercase, sorted alphabetically by item,
prefixing each line with the number of times the user inputted that item.
No need to pluralize the items. Treat the user’s input case-insensitively.
'''
import sys ##sys module helps with exiting at ctl+d

def main():

    mylist = []
    mydict = []

    try:
        while True:
              mylist.append(input().strip().upper())


    except EOFError:
        print("\n")

        unique_list = set(mylist) #creates list of unique items from user provided list

        #sort and count number of unique items in user input and save in dictionary
        for item in sorted(unique_list):
            count = 0
            for grocery in mylist:
                if grocery == item:
                    count += 1
            mydict.append({"qty": count, "itm":item})

        # print unique item names and quantity
        for j in mydict:
            print(j['qty'], j['itm'])

        sys.exit()

if __name__  ==  "__main__":
    main()