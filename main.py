#  import the module to use to simulate the computer’s choices
import random


# defining a function
def rps():
    # while loop
    while True:
        # creating a list of options
        options = ["R", "P", "S"]

        # Making the Computer Choose
        comp = random.choice(options)

        player_choice = None

        while player_choice not in options:
            # Taking User Input
            player_choice = input("Please pick an option \n R, P, S ? : ").upper()

        # Determining a Winner using if else statement

        if player_choice == comp:
            print(f"\nPlayer ({player_choice}) : CPU ({comp}).\n")
            print("Tie!")
            rps()
            break

        elif player_choice == "R":
            if comp == "P":
                print(f"\nPlayer ({player_choice}) : CPU ({comp}).\n")
                print("computer win!")
                break

            else:
                print(f"\nPlayer ({player_choice}) : CPU ({comp}).\n")
                print("you win!")
                break

        elif player_choice == "S":
            if comp == "R":
                print(f"\nPlayer ({player_choice}) : CPU ({comp}).\n")
                print("computer win!")
                break

            else:
                print(f"\nPlayer ({player_choice}) : CPU ({comp}).\n")
                print("you win!")
                break

        elif player_choice == "P":
            if comp == "S":
                print(f"\nPlayer ({player_choice}) : CPU ({comp}).\n")
                print("computer win!")
                break

            else:
                print(f"\nPlayer ({player_choice}) : CPU ({comp}).\n")
                print("you win!")
                break


# calling back the function
rps()
