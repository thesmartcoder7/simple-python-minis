# the number guessing game
import random
from replit import clear


logo = """

888b    888                        888                        .d8888b.  
8888b   888                        888                       d88P  Y88b 
88888b  888                        888                            .d88P 
888Y88b 888 888  888 88888b.d88b.  88888b.   .d88b.  888d888    .d88P"  
888 Y88b888 888  888 888 "888 "88b 888 "88b d8P  Y8b 888P"      888"    
888  Y88888 888  888 888  888  888 888  888 88888888 888        888     
888   Y8888 Y88b 888 888  888  888 888 d88P Y8b.     888                
888    Y888  "Y88888 888  888  888 88888P"   "Y8888  888        888     
                                                                        
                                       
"""

random_guess = random.randint(1,100)
difficulty = ""
end = False
user_guess = 0

while end == False:
    clear()
    print(logo)
    attempts = 0
    difficulty = input("I am thinking of a number between 1 and 100.\nChoose a difficulty. Type 'e' for easy or 'h' for hard: ")

    if difficulty == 'h':
        attempts = 5
    else:
        attempts = 10

    while attempts != 0 and user_guess != random_guess:
        print(f"\nYou have {attempts} attempts left.")
        user_guess = int(input("Make a guess: "))
        if user_guess == random_guess:
            print("\nYes!! You have guessed the right number. You win!!\n")
        elif user_guess > random_guess:
            print("\nThat's too high.")
            attempts -= 1
            if attempts == 0:
                print("\nYou have ran out of attempts. You lose")
            else:
                print("\nGive it another go . . .")
        else:
            print("\nThat's too low.")
            attempts -= 1
            if attempts == 0:
                print("\nYou have ran out of attempts. You lose")
            else:
                print("\nGive it another go . . .")

            
    response = input("\nWould you like to play again? type 'y' for yes or 'n' for no")
    if response == 'y':
        end = False
    else:
        end = True

