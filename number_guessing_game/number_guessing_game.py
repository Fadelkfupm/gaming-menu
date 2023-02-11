import random
def play_number_guessing_game():
     print("--------- Number guessing ---------")
     computer_choice = random.randint(1,10)
     attempts = 3
     print("Guess the number (Between 1-10)")
     user_choice = int(input())
     while(user_choice != computer_choice and attempts != 0):
         print("Incorrect ):")
         attempts = attempts - 1
         if attempts == 0:
             break
         print("You have " + str(attempts) + " attempts left.")
         user_choice = int(input())
     if user_choice == computer_choice:
         print("Correct, Well done (:")




     print("--------- Number guessing ---------")