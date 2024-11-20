def main():

    playslow = []
    playslow = input("input your sentence: ")

    play = playback(playslow)

    for word in play:
        print(word, end = "")
    print(end = "\n")


def playback(pla):
    slow=[]

    for word in pla.split(" "):
        slow.append(word + "...")
    return slow

if __name__ == "__main__":
    main()

