# Hangman

import random
from hangman_wordlist import word_list
from hangman_art import stages
from hangman_art import logo

lives = 6

seed = random.randint(0, 10000)
random.seed(seed)

chosen_word = word_list[random.randint(0, len(word_list) - 1)]
revealed_word = []

for letter in chosen_word:
    revealed_word.append("_") 

print("\n - - - Welcome to Hangman! - - -")
print(f"{logo}\n\n")
print("To play, you need to guess the letters in some word of a specific length.\nEvery right guess will bring you closer to the mistery word and Every\n wrong one will lose you the number of tries you have.\n")

print(f"Hint! The length of the mistery word is: {len(chosen_word)}")
print(f"\n{revealed_word}\n")

while "_" in revealed_word:
    user_letter = input("Choose a random letter that you think is in the word.\n")
    user_letter.lower()
    print("")
    
    if user_letter in revealed_word:
        print("You have already used that letter before. Please choose another letter.\n")
    else:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if user_letter == letter:
                revealed_word[position] = letter

        if user_letter not in chosen_word:
            lives -= 1   
            print(stages[lives])

    
    print(f"{revealed_word} : {lives} Lives left!\n") 
      

    if lives == 0:
        break

chosen_word = "".join(chosen_word).capitalize()
if lives == 0:
    print(f"You Lose! The word you needed was '{chosen_word}' \n\n")
else:
    print(f"You Win! The word is '{chosen_word}'\n\n")



