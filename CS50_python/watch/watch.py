'''
In a file called watch.py, implement a function called parse that expects a str of HTML as input,
extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, and returns
its shorter, shareable youtu.be equivalent as a str. Expect that any such URL will be in one of the
formats below. Assume that the value of src will be surrounded by double quotes. And assume that the
input will contain no more than one such URL. If the input does not contain any such URL at all,
return None.

    http://youtube.com/embed/xvFZjo5PgG0
    https://youtube.com/embed/xvFZjo5PgG0
    https://www.youtube.com/embed/xvFZjo5PgG0
'''
import re
import sys

def main():

    #accept input from user and call parse function
    print(parse(input("HTML: ")))

def parse(url):

    try:

        #impliment Regex to parse YouTube URL
        string = re.search(r'\/embed\/(\w*)"><\/.*', url)

        if string:
            return("https://youtu.be/{}".format(string.group(1)))
        else:
            return None

    except AttributeError:
        sys.exit()

if __name__ == "__main__":
    main()