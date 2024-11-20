def main():

    str = input("Input your string here: ")

    print(convert(str))

def convert(sentence):

    if ":)" or ":(" in sentence:
        sentence = sentence.replace(':)', '\N{slightly smiling face}')
        sentence = sentence.replace(':(', '\N{slightly frowning face}')

        return sentence

    else:
        return sentence

if __name__ == "__main__":
    main()