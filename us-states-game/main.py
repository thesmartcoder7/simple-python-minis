from write_score import WriteState
import turtle
import data
import time

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

correct_states = []
game_is_not_over = True

while game_is_not_over:
    screen.update()
    time.sleep(0.1)
    answer = screen.textinput(title=f"{len(correct_states)} / {len(data.states_list)} States Correct",
                              prompt="which state do you know?").title()

    if len(correct_states) == 50 or answer == 'Exit':
        missed_states = []
        for state in data.states_list:
            if state not in correct_states:
                missed_states.append(state)
        print(f"Here are the states you missed:")
        for state in missed_states:
            print(state)
        game_is_not_over = False
    else:
        if answer not in data.states_list or answer in correct_states:
            pass
        else:
            state = data.SingleState(answer)
            write = WriteState(answer, state.get_x(), state.get_y())
            correct_states.append(answer)
            write.update_map()
