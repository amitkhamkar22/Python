
def main():
    deep = input("Wthat is the answer to the Great Question of Life, the Universe and Everything? ")
    print(answer(deep.lower().strip()))

def answer(deep):
    match deep:
        case "forty-two":
            return ("Yes")

        case "forty two":
            return ("Yes")

        case "42":
            return ("Yes")

        case _:
            return ("No")

if __name__ == "__main__":
    main()