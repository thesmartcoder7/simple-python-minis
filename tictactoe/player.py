class Player:
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice

    def play(self):
        choice = input(f"It's your turn, {self.name}. Choose a slot between 1 and 9: ")
        return choice
