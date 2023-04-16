# import player

# TODO 0. Steps for creating this game:

my_board = [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "]
game_is_running = True
current_player = " X "
winner = None
valid_input = True
player_1 = None
player_2 = None


# def get_players():
#     global player_1
#     global player_2
#     global current_player
#     print("Player 1: Enter name and what you'll play as.")
#     name = input("Name: ")
#     symbol = input("Choose to play either as X or O: ")
#     player_1 = player.Player(name.title(), symbol.upper())
#     current_player = f" {player_1.choice} "
#     print("")
#     print("Player 2: Enter name and what you'll play as.")
#     name = input("Name: ")
#     symbol = input("Choose to play either as X or O: ")
#     player_2 = player.Player(name, symbol)
#

# TODO 1. Create game display

def display_board(pieces):
    """
    this function is responsible for displaying the game board
    in the terminal.
    :param pieces: which is basically the "my_board" array
    :return:
    """
    print(f"\n {pieces[0]} | {pieces[1]} | {pieces[2]}")
    print(" ---------------")
    print(f" {pieces[3]} | {pieces[4]} | {pieces[5]}")
    print(" ---------------")
    print(f" {pieces[6]} | {pieces[7]} | {pieces[8]} \n")


# TODO 2. Get player input and display on game matrix

def user_input(board):
    """
    this function is responsible for taking in the player selection
    and places it in the selected spot
    :param board:
    :return:
    """
    global valid_input
    user_choice = input("Choose a slot between 1 and 9: ")
    try:
        if 1 <= int(user_choice) <= 9 and board[int(user_choice) - 1] == " - ":
            board[int(user_choice) - 1] = current_player
        else:
            print("Sorry, that spot is already occupied, you loose a round")
    except ValueError:
        print("That's an invalid input! Please choose a slot between 1 and 9: ")
        valid_input = False


# TODO 3. Check for a win or a tie

# TODO 5. Check for a win or a tie on player 2

def possible_horizontal(board):
    """
    this function checks for possible horizontal wins
    :param board:
    :return:
    """
    global winner
    if board[0] == board[1] == board[2] and board[0] != " - ":
        winner = my_board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != " - ":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != " - ":
        winner = board[6]
        return True


def possible_vertical(board):
    """
    this function checks for possible vertical wins
    :param board:
    :return:
    """
    global winner
    if board[0] == board[3] == board[6] and board[0] != " - ":
        winner = my_board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != " - ":
        winner = my_board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != " - ":
        winner = board[2]
        return True


def possible_diagonal(board):
    """
    this function checks for possible diagonal wins
    :param board:
    :return:
    """
    global winner
    if board[0] == board[4] == my_board[8] and board[0] != " - ":
        winner = my_board[0]
        return True
    elif my_board[2] == my_board[4] == my_board[6] and my_board[2] != " - ":
        winner = my_board[2]
        return True


def possible_tie(board):
    """
    this function checks for possible ties
    :param board:
    :return:
    """
    global game_is_running
    if " - " not in board:
        display_board(board)
        print("It's a tie! There are no more moves left! ")
        game_is_running = False


def possible_win():
    """
    this function basically checks to see which player has won
    :return:
    """
    global game_is_running
    if possible_horizontal(my_board) or possible_vertical(my_board) or possible_diagonal(my_board):
        if winner == " X ":
            print("\nPlayer 1 wins!")
            game_is_running = False
        else:
            print("\nPlayer 2 wins!")
            game_is_running = False


# TODO 4. Allow player 2 to make a move

def switch_player():
    """
    this function switches players based on the current player
    :return:
    """
    global current_player
    if current_player == " X ":
        current_player = " O "
    else:
        current_player = " X "


# get_players()

# TODO 6. Loop continuously until tie or win

while game_is_running:
    display_board(my_board)
    user_input(my_board)
    possible_win()
    possible_tie(my_board)

    # this allows the machine to only switch the players
    # if the last player's input is valid
    if valid_input:
        switch_player()
