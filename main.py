import dice

# def modifier (roll: int):
#    pass
rolling = True


def main ():
    while rolling:
        print("Would you like to roll a die?")
        roll_choice = input('Type "Y" for Yes or "N" for No. \n').lower()
        if roll_choice == "y":
            print("Which die do you want to roll?")
            die_choice = (input("Choose your die: (4, 6, 8, 10, 12, 20, 100) \n" ))
            try:
                rolled_result = dice.dice_roll(die_choice)
                print(f"You rolled a {rolled_result}! \n")
            #except dice.InvalidDiceChoice as e:
            except Exception as e:
                print(e)
        elif roll_choice == "n":
            return False
        else:
            print("Your response did not make sense. \n ")




if __name__ == "__main__":
    main()
