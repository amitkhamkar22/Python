def main():
    greeting = input("type your greeting here: ")

    print(cramer(greeting))

def cramer(greeting):

    greeting = greeting.lower().strip()

    if "hello" in greeting:
        return("$0")

    elif "h" in greeting[0]:
         return("$20")

    else:
         return("$100")

if __name__ == "__main__":
        main()

