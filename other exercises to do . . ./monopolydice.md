# Monopoly Dice Simulator
### Create a dice simulator for the Monopoly Board Game
Monopoly is one of the hottest board games in the world. Howevr, one great problem people face is how to roll a dice when they have none. In this project, we'll be creating a virtual python dice to be used by any group of Monopoly players so that they don't have to use some irregular paper dice if they lack a proper one. 

To understand the rules of Monopoly, you can [read more from this Wiki How](https://www.wikihow.com/Play-Monopoly). However, you really don't need to be a pro or even have played the game for you to execute this project.

Follow the **instructions/guide** below to create a proper Monopoly Dice Simulator:
- First, you will utilise the random library to output a random number from 1-6. This is what will form your dice.
- Monopoly is different from most board games in that it requires two dice to be rolled at once. Therefore, from the first step modify your script to allow for two dice outputs to be printed out on any roll.
- If the outputs of the two dice are similar, the current player is forced to roll the dice once again. On your script, add this adjustment, that prints out "You have to roll again" and automatically rolls the two dice once again.
- At the end of every roll, print out the number of steps the player is supposed to move. This will be the output of dice 1 plus that of dice 2. If the player had to roll more than once, combine the total steps from each round and output the total steps the player is supposed to move.
- If the outputs of the three dice are similar for a third time, your program should print out "Go to jail" instead of the total steps as per the Monopoly rules.

I hope this description gives you an idea of how to build a monopoly dice simulator. Now go to the **main.py** file and start working on your Python script. There are no unittest or assert functions on this project but you'll have to aggregate your code under the function **roll()**

For additional details on how the Monopoly dice works, you can [visit this link](https://monopoly.fandom.com/wiki/Dice).
