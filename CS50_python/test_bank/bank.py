def main():
    greeting = input("type your greeting here: ")

    print(value(greeting))

def value(greeting):
    greeting = greeting.lower().strip()

    if greeting.startswith('h') and "hello" not in greeting:
        return(20)

    elif "hello" in greeting:
        return(0)

    elif "" in greeting:
        return(100)

    else:
        return(100)


if __name__ == "__main__":
        main()