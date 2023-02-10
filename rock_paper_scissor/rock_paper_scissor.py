import random
def play_rock_paper_scissors():
    print("--------- Rock Paper Scissors ---------")
    computer_choice = random.randint(1,3)
    print("Select your action : \n"
    "[1]: Rock \n"
    "[2]: Paper \n"
    "[3]: Scissor \n")
    user_choice = int(input())
    if user_choice == computer_choice:
        print("Computer choose " + options(computer_choice) + ", It's a tie.")
    elif user_choice == 1:
        if computer_choice == 2:
            print("Computer choose "+ options(computer_choice) +", You lose.")
        elif computer_choice == 3:
            print("Computer choose "+ options(computer_choice) +", You win.")
    elif user_choice == 2:
        if computer_choice == 3:
            print("Computer choose "+ options(computer_choice) +", You lose.")
        elif computer_choice == 1:
            print("Computer choose "+ options(computer_choice) +", You win.")

    elif user_choice == 3:
        if computer_choice == 1:
            print("Computer choose "+ options(computer_choice) +", You lose.")
        elif computer_choice == 2:
            print("Computer choose "+ options(computer_choice) +", You win.")

    print("--------- Rock Paper Scissors ---------")
def options (x):
    if x == 1:
        return("Rock")
    elif x == 2:
        return("Paper")
    else :
        return("Scissor")

