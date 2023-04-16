# Snakes and Ladders Game
### Build a Python Script to play Snakes and Ladders versus two players.
In this project you will Implement a snakes and ladders game with two players. 
You will use a 10 by 10 table with ladders defined in positions as follows 

You can find the board here:

![shutterstock](https://image.shutterstock.com/image-vector/snakes-ladders-board-game-start-600w-163384724.jpg)

- You will use the random module to define the dice moves: typical dice has 1 to 6 combination of dots
- The position initially is zero and you will update it with the value of the dice roll function return using the following idea: 

-----
- For every players turn, for the dice roll be sure to print their current position and the dice roll return 
- Define the get_position function which will find the position of the player and place on the relevant snake and ladder combinations. 
- Define the dice roll function which takes the player, current position and updates this with the random dice roll result, returning the final position after roll 
- Define the snake and ladder function which depedning on the players positon moves them up and down with a message 
- Finally consolidate all into the play function which returns the result of the play. 

##### Rules of the games are as follows. 
------
            Welcome to Snake and Ladder Game.
            Version: 1.0.0  *Feel Free to use anything* 
---
            Rules:
              1. Initially all the players are at starting position i.e. 0. 
                 Take it in turns to roll the dice. 
                 Move forward the number of spaces shown on the dice.
              2. If you land at the bottom of a ladder, you can move up to the top of the ladder.
              3. If you land on the head of a snake, you must slide down to the bottom of the snake.
              4. The first player to get to the FINAL position is the winner.
              5. Hit enter to roll the dice.
              6. Sign up the number of players and names to begin

To make the game more enjoyable limit the number of users to between 1-4

