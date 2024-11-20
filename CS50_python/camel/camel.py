def main():

    camelCase = input("provide camel case name? ")

    print(snake_case(camelCase))

def snake_case(camel):

    char = ""

    for i in range(len(camel)):

        if camel[i].isupper():
            char += ("_" + camel[i].lower())
        else:
            char += camel[i]

    return(char)

if __name__ == "__main__":
    main()