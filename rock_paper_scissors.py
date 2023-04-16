# Rock, Paper, Scissors game
print("\n------- Welcome to the game of Rock, Paper, Scissors! -------")
import random

rock = 'Rock ' + ' 🪨'
paper = 'Paper ' + ' 📃'
scissors = 'Scissors ' + ' ✂️'

choices = [rock, paper, scissors]


number = random.randint(0, 10000)
random.seed(number)

while True:
    
    print("\n\nTo play against the machine, take your pick: \n")
    user_choice = input("Type 'r' for rock, 'p' for paper, and 's' for scissors. Go! \n -- ")

    computer_choice = random.randint(0,2)

    if user_choice == 'r':
        user_choice = 0
    elif user_choice == 'p':
        user_choice = 1
    else:
        user_choice = 2


    # rules
    # rock beats scissors
    # scissors beats paper
    # paper beats rock

    user_choice = choices[user_choice]
    computer_choice = choices[computer_choice]

    if user_choice == rock and computer_choice == rock:
        print(f"\n You have chosen: {user_choice}")
        print(f"\n The machine has chosen: {computer_choice}")
        print(f"\n This is a tie. Run it again.")
    elif user_choice == rock and computer_choice == paper:
        print(f"\n You have chosen: {user_choice}")
        print(f"\n The machine has chosen: {computer_choice}")
        print(f"\n Paper covers Rock. You lose! Game Over.")
    elif user_choice == rock and computer_choice == scissors:
        print(f"\n You have chosen: {user_choice}")
        print(f"\n The machine has chosen: {computer_choice}")
        print(f"\n Rock crushes Scissors. You Win!")
    elif user_choice == paper and computer_choice == paper:
        print(f"\n You have chosen: {user_choice}")
        print(f"\n The machine has chosen: {computer_choice}")
        print(f"\n This is a tie. Run it again.")
    elif user_choice == paper and computer_choice == scissors:
        print(f"\n You have chosen: {user_choice}")
        print(f"\n The machine has chosen: {computer_choice}")
        print(f"\n Scissors cut paper. You lose! Game Over.")
    elif user_choice == paper and computer_choice == rock:
        print(f"\n You have chosen: {user_choice}")
        print(f"\n The machine has chosen: {computer_choice}")
        print(f"\n Paper covers Rock. You Win!")
    elif user_choice == scissors and computer_choice == rock:
        print(f"\n You have chosen: {user_choice}")
        print(f"\n The machine has chosen: {computer_choice}")
        print(f"\n Rock crushes Scissors. You lose! Game Over")
    elif user_choice == scissors and computer_choice == paper:
        print(f"\n You have chosen: {user_choice}")
        print(f"\n The machine has chosen: {computer_choice}")
        print(f"\n Scissors cut paper. You Win!")
    else: # user_choice == scissors and computer_choice == scissors:
        print(f"\n You have chosen: {user_choice}")
        print(f"\n The machine has chosen: {computer_choice}")
        print(f"\n This is a tie. Run it again.")

    print("\n\n------------------------ The End ----------------------------\n")