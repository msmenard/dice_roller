import random


def dice (die: int):
    return random.randint(1, die)

def main ():
    print("Which die do you want to roll?")
    die_choice = int(input("Choose your die: (4, 6, 8, 10, 12, 20, 100\n" ))
    print(dice(die_choice))




if __name__ == "__main__":
    main()
