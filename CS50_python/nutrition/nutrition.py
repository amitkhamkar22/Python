'''
In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively)
and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text.
Capitalization aside, assume that users will input fruits exactly as written in the poster
(e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.
'''


def main():
    print(nutrition(input("Item: ").lower()))

def nutrition(item):

    match item:
        case 'apple':
            return("Calories: 130")

        case 'avocado':
            return("Calories: 50")

        case 'banana':
            return("Calories: 110")

        case 'cantaloupe':
            return("Calories: 50")

        case 'grapefruit':
            return("Calories: 60")

        case 'graps':
            return("Calories: 90")

        case 'graps':
            return("Calories: 90")

        case 'honeydew':
            return("Calories: 50")

        case 'kiwifruit':
            return("Calories: 90")

        case 'lemon':
            return("Calories: 15")

        case 'lime':
            return("Calories: 20")

        case 'nectarine':
            return("Calories: 60")

        case 'orange':
            return("Calories: 80")

        case 'peach':
            return("Calories: 60")

        case 'pear':
            return("Calories: 100")

        case 'pineapple':
            return("Calories: 50")

        case 'plums':
            return("Calories: 70")

        case 'strawberries':
            return("Calories: 50")

        case 'sweet cherries':
            return("Calories: 100")

        case 'tangerine':
            return("Calories: 50")

        case 'watermelon':
            return("Calories: 80")

        case _:
            return("")

if __name__ == "__main__":
    main()