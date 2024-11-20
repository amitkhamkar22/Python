'''
When texting or tweeting, it’s not uncommon to shorten words to save time or space,
as by omitting vowels, much like Twitter was originally called twttr.
In a file called twttr.py, implement a program that prompts the user for a str of text
and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.
'''

def main():

    string  =  input("input your twitte: ")

    print(shorten(string))

def shorten(sentence):

    new_sentence = ""

    for s in range(len(sentence)):

        if sentence[s] not in ['a', 'e', 'i', 'o', 'u']:

            new_sentence += sentence[s]

        else:
            new_sentence += ""

    return new_sentence

if __name__ == "__main__":
    main()