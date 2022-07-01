


from random import choice, random


def get_choice(choice):
    if choice == "R":
        return("Rock")
    elif choice == "P":
        return("Paper")
    elif choice == "S":
        return("Sissor")
    else:
        return("Your choice is not available")


def main():
    print("Wellcome to Rock, Paper, Sissor Game")
    print("[R] = Rock, [P] =Paper, [S]=Scissor and [Q] = Quit")
    choices = ["R", "P", "S"]
    game_on = True
    counter = 1
    
    




    while game_on:
        user_choice = input(f"Game #{counter}. please enter your choice :")
        user_choice = user_choice.upper()
        computer_choice = choice(choices)
        print(f"Your choice is: {get_choice(user_choice)}")
        print(f"Computer choice is: {get_choice(computer_choice)}")

        if user_choice == "Q":
            print("Thank you fo join the game,hope you have fun, Have nice day!")
            game_on = False
        else:
            if user_choice in choices:
                if user_choice == computer_choice:
                    print("you won")
                elif user_choice == "R" and computer_choice == "P":
                    print("you lose")
                elif user_choice == "P" and computer_choice == "S":
                    print("you lose")
                elif user_choice == "S" and computer_choice == "R":
                    print("you lose")
                else:
                    print("you Win")
                counter = counter + 1
                print("-"*40)
                continue
            else:
                print("Please enter r,p or s Bro.")
                continue


        

        


if __name__ == "__main__":
    main()