'''
In a file called game.py, implement a program that
Prompts the user for a level.
If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and n, inclusive, using the random module.
Prompts the user to guess that integer.
If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
'''
import random
import sys

def main():

    level = 0
    guess = 0

    while True:

        try:
            level = int(input("Level: "))

            if level < 1:
                pass
            else:
                break

        except ValueError:
            pass

    rand = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))

            if guess > 0 and guess < level:
                if rand < guess:
                    print("Too large!")
                elif rand > guess:
                    print("Too small!")
                else:
                    print("Just right!")
                    break
            else:
                pass

        except ValueError:
            pass

if __name__ == "__main__":
    main()