# higher-lower the game

import random
import os
from gamedata import data
from gamelogo import logo

def random_selection():
    return random.choice(data)

def clear():
    os.system('cls')
    os.system('clear')


def game():
    option_a = random_selection()
    option_b = random_selection()
    user_score = 0
    confirmation = ""
    end_of_game = False
    while end_of_game == False and option_a != option_b:
        clear()
        print(logo)
        print(f"\n{confirmation} your score is {user_score}")
        user_selection = input(f"\nWho has more followers?\na) {option_a['name']}, a {option_a['description']} from {option_a['country']}\nb) {option_b['name']}, a {option_b['description']} from {option_b['country']}\n --: ").lower()

        if user_selection == 'a':
            if option_a['follower_count'] > option_b['follower_count']:
                user_score += 10
                confirmation = "You are right!!"
                option_a = option_b
                option_b = random_selection()
            else:
                print(f"\nYou are wrong!! Your final score is {user_score}")
                end_of_game = True
        else:
            if option_b['follower_count'] > option_a['follower_count']:
                user_score += 10
                confirmation = "You are right!!"
                option_a = option_b
                option_b = random_selection()
            else:
                print(f"\nYou are wrong!! Your final score is {user_score}")
                end_of_game = True
                
    answer = input("\nWould you like to play again? Type 'y' for Yes or 'n' for No: ").lower()
    if answer == 'y':
        game()
    else:
        return


game()
print("\nThank you for playing! Cheers!!\n\n")

