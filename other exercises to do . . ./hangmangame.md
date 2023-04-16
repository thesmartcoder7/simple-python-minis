# Hangman Game
### Build a Python Script for the Popular Hangman Game
In this project you will create a python project implementing the hangman game enabling the player to attempt guessing a hidden word. If you are not farmiliar with the game, check out [the graphical online game here](https://www.hangmanwords.com/play).

In summary the user has attempts at guessing a word represented in a row of dashes and if a player guesses a letter which exists in the word, the program writes it in all correct positions, these attempts are reduced for every wrong character guess the player makes, once all are exhausted, without a matching word having been guessed, the monster eats up the player.

### Here are the steps to follow:
- Choose some good hangman words for your program. You can go to [this website](https://www.hangmanwords.com/words) and create a list of words for your game.
- At the start of the game, use the random library to choose a random word from your hangman words and display the word's letters as dashes rather than letters.
- Now, apply the input function to allow the user to make letter guesses. Use try... except and if statements to make sure that only valid inputs work with your script i.e. a user can only choose one letter at a time, and a user cannot choose letters that have been chosen before.
- If the letter is in the word then it is printed in place of the corresponding dash. If the letter is not in the word, that is counted as a failed attempt, Limit the number of failed attempts for the user to 6 such that on the 6th fail, the game ends and the script prints the actual word and "You Lost". Make sure to tell the user they won if they guess all the correct letters in under 6 failed attempts.
- If you want to take the project a notch higher, you can use the Python Turtle Library to visualize the hanging like in [this website](https://www.hangmanwords.com/play). This is optional!
