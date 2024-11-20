def main():

    print(einst(int(input("What is the amount of mass in kg? "))))

def einst(mass):

    speed_of_light = 300000000
    return (int(mass * speed_of_light * speed_of_light))

if __name__ == "__main__":
    main()